# SKILL: Asset Discovery
## Version: 1.0 | Domain: recon | Trigger: you have a domain list; need to convert to live web/api/service inventory

---

## IDENTITY IN THIS SKILL
From resolved hostnames → a full inventory of HTTP services, ports, technologies, screenshots, and notable response signatures.

---

## TOOLS
- `httpx (PD): -status-code -title -tech-detect -ip -cname -tls-grab -web-server -content-length -response-time -follow-redirects`
- `naabu (PD): top ports + custom port spec, fast SYN-style`
- `masscan / rustscan: bulk full-range port scan`
- `nmap: deep service detection (version + script scan)`
- `aquatone / gowitness / eyewitness: screenshot grids`
- `tlsx (PD): TLS metadata extraction`

## COMMANDS & WORKFLOWS
### Probe HTTP on common web ports
```bash
httpx -l all_subs.txt -ports 80,443,81,591,2082,2087,2095,2096,3000,3128,4243,4567,4711,4712,4993,5000,5104,5108,5800,6543,7000,7396,7474,8000,8001,8008,8014,8042,8060,8069,8080,8081,8083,8088,8090,8091,8118,8123,8172,8222,8243,8280,8281,8333,8443,8500,8834,8880,8888,8983,9000,9043,9060,9080,9090,9091,9200,9443,9800,9981,12443,16080,18091,18092,20720,28017 \
  -threads 100 -timeout 7 -retries 1 -follow-redirects \
  -status-code -title -tech-detect -ip -cname -tls-grab -web-server -content-length -response-time -websocket \
  -json -o httpx.jsonl
```

### Full port scan (bulk via naabu, then service-detect via nmap)
```bash
naabu -list resolved.txt -top-ports 1000 -rate 10000 -o naabu.txt
naabu -list resolved.txt -p - -rate 5000 -exclude-cdn -o naabu_full.txt   # full 65k
# nmap version-detect on the alive ports
naabu -list resolved.txt -top-ports 1000 -nmap-cli 'nmap -sV -sC -O --script=banner,vulners --max-retries 1' -o naabu_nmap.xml
```

### rustscan alternative (fast)
```bash
rustscan -a $(cat resolved.txt | tr '\n' ',') -r 1-65535 --ulimit 5000 -- -sV -sC --script=vulners
```

### Screenshot grid
```bash
cat httpx.jsonl | jq -r .url | gowitness file -f - --threads 50 --disable-db -P screenshots/
# OR aquatone
cat httpx.jsonl | jq -r .url | aquatone -threads 50 -out aquatone/
```

### TLS cert metadata sweep (find cert reuse → related infra)
```bash
tlsx -l resolved.txt -san -cn -ja3 -ja3s -tls-version -cipher -o tls.txt
# Extract all SAN entries → feed back into subdomain pool
tlsx -l resolved.txt -san -resp-only -silent | tr ',' '\n' | sort -u >> all_subs.txt
```

### Detect WAF / CDN per host (informs payload strategy later)
```bash
wafw00f -i httpx_urls.txt -o wafw00f.txt
cdncheck -i httpx_urls.txt -o cdn.txt   # PD's CDN identifier
```




## EDGE CASES
- **Cloudflare-fronted hosts** — origin IP often leaked via: historical DNS (SecurityTrails), MX records, mail headers, cert transparency for the origin's own cert (not CF's), favicon hash search on Shodan.
- **Akamai-fronted hosts** — Akamai prepends `X-Akamai-*` headers; pivot via DNS lookups for `e1234.x.akamaiedge.net` style.
- **Default 404/403 across many hosts** — could be virtual host routing. Try `Host:` header swap with each known sub against same IP.
- **WebSocket-only services** — httpx flag `-websocket` catches; otherwise looks like 404. Worth a separate pass.
- **Container orchestration ports** — 2375 (Docker), 6443/8443/10250 (k8s), 4243 (Docker), 9999 (k8s dashboard) → cluster takeover.

## OUTPUT FORMAT
```
ASSET_DISCOVERY({target}):
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
