# SKILL: Shodan / Censys / FOFA / ZoomEye / Hunter.how / BinaryEdge / Quake360
## Version: 1.0 | Domain: recon | Trigger: any time; gold for finding Cloudflare-bypass origin IPs and exposed mgmt panels

---

## IDENTITY IN THIS SKILL
These engines have already scanned the entire IPv4 space. You query their database — fully passive — and pivot via fingerprints (favicon hash, JARM, TLS cert SAN, http title, http body hash) to discover assets you'd never find via DNS.

---

## TOOLS
- `shodan CLI + API`
- `censys CLI + API`
- `FOFA web UI / API + base64-encoded queries`
- `ZoomEye CLI`
- `BinaryEdge`
- `Hunter.how`
- `Netlas.io`
- `Quake360 (CN-only)`

## COMMANDS & WORKFLOWS
### Shodan find origin behind Cloudflare
```bash
# Cert SAN match but NOT in CF range
shodan search 'ssl.cert.subject.cn:"example.com" -country:"US"' | grep -v 'cloudflare'
# OR favicon match outside CF
fhash=$(python3 favicon_hash.py https://example.com)
shodan search "http.favicon.hash:$fhash"
```

### Censys cert SAN sweep
```bash
censys search 'services.tls.certificates.leaf_data.names: "example.com"' --pages 5 -o censys_results.json
```

### FOFA via Python
```bash
import base64, requests
q = 'cert="example.com"'
qb = base64.b64encode(q.encode()).decode()
r = requests.get(f'https://fofa.info/api/v1/search/all?email={EMAIL}&key={KEY}&qbase64={qb}&size=10000')
for line in r.json()['results']: print(line)
```

### Bulk JARM scan against shortlisted IPs
```bash
jarm -i ips.txt -o jarm.txt   # then group by JARM to identify shared infra
```



## QUERIES BY ENGINE

## Shodan
shodan domain example.com
shodan search 'ssl.cert.subject.cn:"example.com"'
shodan search 'ssl:"example.com" 200'
shodan search 'org:"Example Inc"'
shodan search 'hostname:.example.com'
shodan search 'http.favicon.hash:HASH'
shodan search 'http.title:"login" hostname:example.com'
shodan search 'http.html:"example.com" -hostname:example.com'   # finds origin IPs
shodan search 'product:Jenkins hostname:example.com'
shodan search 'product:Kubernetes hostname:example.com'
shodan search 'http.component:"WordPress" hostname:example.com'

## Censys (v2 API)
services.tls.certificates.leaf_data.subject.common_name: "example.com"
services.tls.certificates.leaf_data.names: "example.com"
autonomous_system.organization: "Example Inc"
services.http.response.html_title: "Login" and services.tls.certificates.leaf_data.subject.common_name: "example.com"
services.http.response.headers.set_cookie.value: "session=" and services.tls.certificates.leaf_data.subject.common_name: "example.com"
services.jarm.fingerprint: "07d14d16d21d21d00042d41d00041d24a458a375eef0c576d23a7bab9a9fb1"
ip: 1.2.3.0/24

## FOFA (queries are base64-encoded URL params)
domain="example.com"
cert="example.com"
host="example.com"
icon_hash="-1234567890"
title="Example Login"
header="example.com"
body="example.com"
type="subdomain" && cert="example.com"
ip="1.2.3.4"

## ZoomEye
hostname:"example.com"
ssl:"example.com"
title:"Example"
app:"Apache"
country:"US"
service:"http"
port:"8080"

## Hunter.how (huntedu.com)
domain.suffix="example.com"
domain="example.com"
header="X-Powered-By: Express"

## Netlas
A:1.2.3.4
domain:example.com
http.body:"example"


## Favicon Hash Pivot — find origin IPs / unrelated assets via icon

```python
import mmh3, requests, codecs, sys
def fhash(url):
    r = requests.get(url + "/favicon.ico", verify=False, timeout=8)
    return mmh3.hash(codecs.encode(r.content, "base64"))
print(fhash(sys.argv[1]))
```

Then query each engine:
- Shodan: `http.favicon.hash:HASH`
- FOFA: `icon_hash="HASH"` (base64-encode entire query for URL)
- ZoomEye: `iconhash:"HASH"`
- Censys (v2): `services.http.response.favicons.md5_hash: "..."` (Censys uses MD5 of icon, not mmh3)


## EDGE CASES
- **Stale Shodan data** — last seen 6 months ago; service may have moved. Confirm with live `httpx`.
- **FOFA query encoding** — must be base64; mistake = empty results.
- **Origin behind Cloudflare** — best signals: cert SAN match + non-CF ASN; favicon hash match + non-CF ASN; HTTP body hash match.
- **Internal services exposed** — Kibana 5601, Elasticsearch 9200, Jenkins 8080 unauth; Mongo 27017 — instant P1 if confirmed exposed.
- **Sensors / honeypots** — same banner across many IPs in different geos = likely honeypot grid.

## OUTPUT FORMAT
```
SHODAN___CENSYS___FOFA___ZOOMEYE___HUNTER.HOW___BINARYEDGE___QUAKE360({target}):
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
