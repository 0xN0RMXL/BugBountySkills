# SKILL: API Discovery
## Version: 1.0 | Domain: recon | Trigger: after web crawl + JS analysis; or 'find APIs on TARGET'

---

## IDENTITY IN THIS SKILL
Identify REST endpoints, GraphQL schemas, gRPC services, WebSocket endpoints, internal APIs leaked in mobile/JS, and undocumented versions/methods. APIs are where business logic — and bug bounties — live.

---

## TOOLS
- `katana / hakrawler / gospider crawls + JS endpoint extraction (jsluice, linkfinder)`
- `kiterunner — wordlist-based API endpoint discovery (uses SecLists/Discovery/Web-Content/api/)`
- `ffuf with API wordlists`
- `graphql-cop / clairvoyance / inql / graphw00f — GraphQL discovery + schema introspection`
- `grpcurl / grpc-tools — gRPC service discovery`
- `Burp 'API Discovery' (Pro feature) + JS Miner ext`
- `Postman / Insomnia / Bruno — for replay + fuzzing`
- `Swagger / OpenAPI / WSDL parser scripts`

## COMMANDS & WORKFLOWS
### Crawl + extract endpoints from JS
```bash
katana -list alive.txt -d 5 -jc -kf all -aff -o crawl.txt
find js/ -name '*.js' -exec jsluice urls -m '*' {} \; | sort -u > endpoints_jsluice.txt
cat crawl.txt endpoints_jsluice.txt | sort -u > all_endpoints.txt
```

### Find docs / schemas
```bash
# Common paths
for path in api openapi.json openapi.yaml swagger.json swagger.yaml swagger-ui swagger-ui.html api-docs api/v1 api/v2 api/v3 docs redoc graphql graphiql playground apollo wsdl actuator actuator/beans actuator/mappings actuator/env actuator/health; do
  ffuf -u "https://$TARGET/$path" -mc 200,401,403 -ac -of csv -o /tmp/r.csv
done
# nuclei has templates for these
nuclei -l alive.txt -t http/exposures/apis/ -severity info,low,medium,high,critical
```

### kiterunner — better than ffuf for APIs (does HEAD + scrambled methods)
```bash
# Use the curated routes-large.kite
kr scan https://example.com -A=apiroutes-210126:20210126 -o kr_results.txt
kr brute https://example.com -w ~/wordlists/api/api-endpoints.txt -o kr_brute.txt
```

### GraphQL discovery + introspection
```bash
# Find GraphQL endpoints
for path in graphql graphiql api/graphql v1/graphql v2/graphql query subgraph; do
  curl -sk -X POST "https://$TARGET/$path" -H 'Content-Type: application/json' \
    -d '{"query":"{__typename}"}' -o /dev/null -w "%{http_code} https://$TARGET/$path\n"
done
# Introspect (often disabled in prod, but try)
curl -sk -X POST https://$TARGET/graphql -H 'Content-Type: application/json' \
  --data '{"query":"query IntrospectionQuery { __schema { queryType { name } mutationType { name } subscriptionType { name } types { ...FullType } directives { name description locations args { ...InputValue } } } } fragment FullType on __Type { kind name description fields(includeDeprecated: true) { name description args { ...InputValue } type { ...TypeRef } isDeprecated deprecationReason } inputFields { ...InputValue } interfaces { ...TypeRef } enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason } possibleTypes { ...TypeRef } } fragment InputValue on __InputValue { name description type { ...TypeRef } defaultValue } fragment TypeRef on __Type { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name } } } } } } } }"}' \
  | jq . > schema.json
# If introspection disabled → use clairvoyance to brute-force
clairvoyance -o schema.json -w ~/wordlists/graphql/graphql-words.txt https://$TARGET/graphql
# graphw00f — fingerprint engine (Apollo, Hasura, Relay, AWS AppSync, GraphQL Yoga, etc.)
graphw00f -t https://$TARGET/graphql -d
```

### gRPC discovery
```bash
grpcurl -plaintext $HOST:$PORT list   # if reflection enabled
grpcurl -plaintext $HOST:$PORT list mypackage.MyService
# Without reflection — need .proto files; sometimes leaked in JS / mobile / GitHub
```

### WebSocket discovery + connection
```bash
# Find WS handshake endpoints in crawl
rg -oE 'wss?://[^\s"\'<>]+' js/ alive.txt > ws_endpoints.txt
# Connect with wscat
wscat -c "wss://example.com/ws" -H "Authorization: Bearer $TOKEN"
```

### Detect API versioning
```bash
# Same endpoint, different versions sometimes have different auth
for v in 1 2 3 v1 v2 v3 latest internal beta legacy old; do
  curl -sk -o /dev/null -w "$v: %{http_code}\n" "https://$TARGET/api/$v/users"
done
```

### Find OpenAPI / Swagger via favicon hash → Shodan
```bash
# Many Swagger UIs share favicon hash. Pivot like this for org-wide discovery.
shodan search 'http.favicon.hash:1606627656'   # default Swagger UI hash
shodan search 'http.title:"Swagger UI" hostname:example.com'
```




## EDGE CASES
- **Path versioning vs Header versioning** — `Accept: application/vnd.example.v1+json`. Test all variants.
- **Internal-only API hosts** — leaked in mobile/JS as fallback. `https://api-internal.example.com` may be reachable from internet despite naming.
- **Method confusion** — `GET /api/admin/users` returns 403, `POST` returns 200. Always test all methods (`OPTIONS` to enumerate, then HEAD/GET/POST/PUT/PATCH/DELETE).
- **Trailing slash behavior** — `/api/users` 401 vs `/api/users/` 200 — common framework routing inconsistency.
- **HTTP/2 method whitelist bypass** — some WAFs only know HTTP/1.1; send same request via HTTP/2 with `httpx --http2`.
- **GraphQL aliases** — bypass per-field rate limit with batched aliases (`x: user(id:1) y: user(id:2)`); also defense-evasion for IDOR.
- **Documentation rot** — Swagger lists endpoints that no longer exist; missing endpoints exist. Diff `/openapi.json` against actual probe.

## OUTPUT FORMAT
```
API_DISCOVERY({target}):
  <key>: <value>
  ...
NEXT: handoff to next stage
```

## SOURCES
- Bug Hunters Methodology Live Day One Recon (jhaddix)
- zseanos-methodology
- Elite_BugBounty_Methodology
- ProjectDiscovery / Assetnote / SecLists
- HackTricks recon section
- PortSwigger Research blog
