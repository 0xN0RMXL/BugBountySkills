# SKILL: Fingerprinting Tech Stack
## Version: 1.0 | Domain: recon | Trigger: you have a live HTTP service; need to know framework + WAF + libraries before payload crafting

---

## IDENTITY IN THIS SKILL
Identify framework, server, language, ORM, CMS, WAF, CDN, JS libs, and version numbers — these dictate which exploit primitives apply (e.g., Spring SpEL vs Twig SSTI vs Jinja2).

---

## TOOLS
- `httpx -tech-detect (Wappalyzer)`
- `wappalyzer CLI`
- `whatweb`
- `nuclei -t http/technologies/ (PD official)`
- `wafw00f, cdncheck, retire.js, JSDeps (Burp ext)`
- `Favicon hash → Shodan/FOFA pivot`
- `HTML comments + meta tags + cookie names + JS globals + error pages`

## COMMANDS & WORKFLOWS
### Tech detect at scale
```bash
httpx -l alive.txt -tech-detect -web-server -title -status-code -ip -cdn -follow-redirects -json -o tech.jsonl
cat tech.jsonl | jq -r 'select(.tech) | "\(.url)\t\(.tech | join(","))"' | sort -u
```

### WAF detection
```bash
wafw00f -i alive.txt -o wafw00f.txt
# Manual confirmation — Cloudflare leaks via Server: cloudflare; Akamai via X-Cache or AkamaiGHost; AWS WAF via x-amzn-RequestId on block; Imperva via X-Iinfo; Sucuri via X-Sucuri-ID; F5 via BIGipServer cookie.
```

### Favicon hash pivot
```bash
python3 -c '
import mmh3, requests, codecs, sys
for u in sys.argv[1:]:
  try:
    r = requests.get(u + "/favicon.ico", timeout=5, verify=False)
    if r.status_code == 200 and r.content:
      print(u, mmh3.hash(codecs.encode(r.content, "base64")))
  except: pass
' $(cat alive.txt)
# Then Shodan: http.favicon.hash:HASH
```

### Run nuclei tech detection templates
```bash
nuclei -l alive.txt -t http/technologies/ -severity info -silent -o tech_nuclei.txt
```

### Identify retired JS libs (CVE candidates)
```bash
# retire.js scan over saved JS
retire --jspath js/ --outputformat json --outputpath retire.json
# Or nuclei JS templates
nuclei -l alive.txt -t http/exposures/ -severity medium,high,critical
```

### Cookie + header forensics
```bash
for u in $(cat alive.txt); do
  curl -sk -D /dev/stdout -o /dev/null --max-time 8 "$u" | head -40
  echo "=== $u ==="
done > headers.txt
# Look for: Set-Cookie names (PHPSESSID, JSESSIONID, ASP.NET_SessionId, session, connect.sid (Express), laravel_session, _csrf, csrftoken (Django), AWSALB)
# X-Powered-By: PHP/X.Y, ASP.NET, Express, JBoss, Tomcat
# Server: Apache, nginx, IIS, Caddy, AmazonS3, AzureStorage, GoogleFrontend
```




## EDGE CASES
- **Multiple stacks behind reverse proxy** — `Server: nginx` upstream is Spring; `X-Powered-By: PHP` may be a sidecar. Hit different paths.
- **Generic WAF on top hides framework errors** — provoke a 500 by malformed JSON / large header / weird method, then read upstream error page directly.
- **CDN strips `Server` header** — pivot via TLS handshake fingerprinting (JA3/JARM).
- **JARM fingerprint** — `jarm example.com:443`; same JARM across hosts = same TLS stack vendor (e.g., Cloudflare-fronted).
- **HTTP/2 only services** — old WAFs / scanners ignore them; force HTTP/2 via `curl --http2` or `httpx -http2`.

## OUTPUT FORMAT
```
FINGERPRINTING_TECH_STACK({target}):
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
