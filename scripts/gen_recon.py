#!/usr/bin/env python3
"""Generate the remaining RECON skill files with rich per-topic content."""
import os
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "SKILL_FILES" / "RECON"
OUT.mkdir(parents=True, exist_ok=True)

FILES = {
    "03_dns_analysis.md": {
        "title": "DNS Analysis",
        "trigger": "after subdomain resolution; or 'analyze DNS for X'",
        "what": "Beyond A/CNAME — pull every record type, look for misconfig, takeover candidates, mail spoofing primitives, and zone-transfer leftovers.",
        "tools": [
            "dnsx -a -aaaa -cname -ns -mx -txt -soa -ptr -axfr -resp",
            "dig +short any example.com @1.1.1.1",
            "dnsrecon -d example.com -t std,brt,srv,axfr,goo,bing,zonewalk",
            "fierce -dns example.com",
            "nsec3walker / ldns-walk for DNSSEC NSEC enum",
        ],
        "commands": [
            ("Pull ALL record types in parallel",
             "dnsx -l alive.txt -a -aaaa -cname -ns -mx -txt -soa -ptr -resp -silent -o dns_records.txt"),
            ("Detect dangling CNAMEs (takeover candidates)",
             "dnsx -l alive.txt -cname -resp-only | tee cnames.txt\n"
             "# Flag CNAMEs that point to NXDOMAIN or unclaimed third-party services:\n"
             "for c in $(cat cnames.txt); do dig +short $c @1.1.1.1 | grep -q '^$' && echo \"DANGLING: $c\"; done"),
            ("Test for AXFR (zone transfer) on every NS",
             "for ns in $(dig +short ns example.com); do\n"
             "  echo \"=== $ns ===\"\n"
             "  dig @\"$ns\" example.com AXFR +noidnout\n"
             "done | tee axfr.txt"),
            ("DNSSEC NSEC zone walk (pulls every record without AXFR)",
             "ldns-walk -s 1.1.1.1 example.com\n"
             "# or nsec3walker for NSEC3 (slower but works on most modern setups)"),
            ("Find SPF/DMARC misconfig (email spoofing primitive)",
             "dig +short txt example.com | grep -i spf\n"
             "dig +short txt _dmarc.example.com\n"
             "# SPF too permissive (+all, ?all, ~all + open relay) → spoofable\n"
             "# DMARC missing/p=none → no rejection of forged mail"),
            ("CAA records (cert pinning bypass research)",
             "dig +short caa example.com"),
            ("Reverse DNS sweep on netblocks",
             "prips $(cat netblocks.txt) | dnsx -ptr -resp-only -silent | sort -u > rdns.txt"),
        ],
        "edge": [
            "**Wildcard CNAMEs** — `*.example.com → cdn.thirdparty.com`. The wildcard itself isn't takeover-able; specific named subs that go through the wildcard might be. Test each.",
            "**Split-horizon DNS** — internal vs external view. You only see external. Pivot via leaked /etc/hosts in S3 or GitHub.",
            "**DNSSEC NSEC walking** — yields full zone for free if NSEC (not NSEC3). Always try first.",
            "**Cloudflare/Akamai-fronted MX** — origin server IP often leaked via MX record (mail server).",
            "**Email security misconfig (high-impact P3-P2):** SPF too permissive + DMARC `p=none` + missing DKIM = phishing primitive. Send forged email from `payments@target.com` to triager.",
        ],
    },
    "04_asset_discovery.md": {
        "title": "Asset Discovery",
        "trigger": "you have a domain list; need to convert to live web/api/service inventory",
        "what": "From resolved hostnames → a full inventory of HTTP services, ports, technologies, screenshots, and notable response signatures.",
        "tools": [
            "httpx (PD): -status-code -title -tech-detect -ip -cname -tls-grab -web-server -content-length -response-time -follow-redirects",
            "naabu (PD): top ports + custom port spec, fast SYN-style",
            "masscan / rustscan: bulk full-range port scan",
            "nmap: deep service detection (version + script scan)",
            "aquatone / gowitness / eyewitness: screenshot grids",
            "tlsx (PD): TLS metadata extraction",
        ],
        "commands": [
            ("Probe HTTP on common web ports",
             "httpx -l all_subs.txt -ports 80,443,81,591,2082,2087,2095,2096,3000,3128,4243,4567,4711,4712,4993,5000,5104,5108,5800,6543,7000,7396,7474,8000,8001,8008,8014,8042,8060,8069,8080,8081,8083,8088,8090,8091,8118,8123,8172,8222,8243,8280,8281,8333,8443,8500,8834,8880,8888,8983,9000,9043,9060,9080,9090,9091,9200,9443,9800,9981,12443,16080,18091,18092,20720,28017 \\\n"
             "  -threads 100 -timeout 7 -retries 1 -follow-redirects \\\n"
             "  -status-code -title -tech-detect -ip -cname -tls-grab -web-server -content-length -response-time -websocket \\\n"
             "  -json -o httpx.jsonl"),
            ("Full port scan (bulk via naabu, then service-detect via nmap)",
             "naabu -list resolved.txt -top-ports 1000 -rate 10000 -o naabu.txt\n"
             "naabu -list resolved.txt -p - -rate 5000 -exclude-cdn -o naabu_full.txt   # full 65k\n"
             "# nmap version-detect on the alive ports\n"
             "naabu -list resolved.txt -top-ports 1000 -nmap-cli 'nmap -sV -sC -O --script=banner,vulners --max-retries 1' -o naabu_nmap.xml"),
            ("rustscan alternative (fast)",
             "rustscan -a $(cat resolved.txt | tr '\\n' ',') -r 1-65535 --ulimit 5000 -- -sV -sC --script=vulners"),
            ("Screenshot grid",
             "cat httpx.jsonl | jq -r .url | gowitness file -f - --threads 50 --disable-db -P screenshots/\n"
             "# OR aquatone\n"
             "cat httpx.jsonl | jq -r .url | aquatone -threads 50 -out aquatone/"),
            ("TLS cert metadata sweep (find cert reuse → related infra)",
             "tlsx -l resolved.txt -san -cn -ja3 -ja3s -tls-version -cipher -o tls.txt\n"
             "# Extract all SAN entries → feed back into subdomain pool\n"
             "tlsx -l resolved.txt -san -resp-only -silent | tr ',' '\\n' | sort -u >> all_subs.txt"),
            ("Detect WAF / CDN per host (informs payload strategy later)",
             "wafw00f -i httpx_urls.txt -o wafw00f.txt\n"
             "cdncheck -i httpx_urls.txt -o cdn.txt   # PD's CDN identifier"),
        ],
        "edge": [
            "**Cloudflare-fronted hosts** — origin IP often leaked via: historical DNS (SecurityTrails), MX records, mail headers, cert transparency for the origin's own cert (not CF's), favicon hash search on Shodan.",
            "**Akamai-fronted hosts** — Akamai prepends `X-Akamai-*` headers; pivot via DNS lookups for `e1234.x.akamaiedge.net` style.",
            "**Default 404/403 across many hosts** — could be virtual host routing. Try `Host:` header swap with each known sub against same IP.",
            "**WebSocket-only services** — httpx flag `-websocket` catches; otherwise looks like 404. Worth a separate pass.",
            "**Container orchestration ports** — 2375 (Docker), 6443/8443/10250 (k8s), 4243 (Docker), 9999 (k8s dashboard) → cluster takeover.",
        ],
    },
    "05_javascript_analysis.md": {
        "title": "JavaScript Analysis",
        "trigger": "any web target has bundled JS; especially SPAs and admin panels",
        "what": "Frontend JavaScript leaks endpoints, parameters, secrets, business logic, role enums, hidden routes, internal API hosts, analytics keys, and (occasionally) full backend code via sourcemaps.",
        "tools": [
            "katana / hakrawler / gospider: crawl + extract JS",
            "subjs: extract JS URLs from a domain",
            "linkfinder / jsluice / mantra / jsleak: extract endpoints + secrets from JS",
            "secretfinder: regex-based secret scan",
            "GAP (Burp ext): parameter mining from JS",
            "JS Miner (Burp ext): inline secret + endpoint mining",
            "trufflehog filesystem: regex / verifier secret scan over downloaded JS",
            "sourcemapper / unwebpack-sourcemap: pull source from .js.map",
            "uglify-restore / prettier --parser babel: deobfuscate",
        ],
        "commands": [
            ("Crawl + collect all JS files from target",
             "katana -list alive.txt -d 5 -jc -kf all -aff -o crawl.txt\n"
             "cat crawl.txt | grep -E '\\.js(\\?|$)' | sort -u > js_urls.txt\n"
             "# add gau / waybackurls historical JS\n"
             "cat alive.txt | gau --subs --threads 10 | grep -E '\\.js(\\?|$)' >> js_urls.txt\n"
             "sort -u js_urls.txt -o js_urls.txt"),
            ("Download all JS for offline analysis",
             "mkdir -p js && cd js && cat ../js_urls.txt | xargs -I{} -P 20 curl -sk --max-time 15 -o \"$(echo {} | md5sum | cut -d' ' -f1).js\" \"{}\""),
            ("Extract endpoints from JS",
             "for f in js/*.js; do\n"
             "  python3 ~/tools/LinkFinder/linkfinder.py -i \"$f\" -o cli\n"
             "done | sort -u > endpoints_from_js.txt\n"
             "# OR jsluice (Tom Hudson) — best in 2024\n"
             "find js/ -name '*.js' | xargs -I{} jsluice urls -m '*' {} | sort -u >> endpoints_from_js.txt\n"
             "find js/ -name '*.js' | xargs -I{} jsluice secrets {} > js_secrets.txt"),
            ("Secret scanning on downloaded JS",
             "trufflehog filesystem --json js/ > js_truffle.json\n"
             "secretfinder -i js/ -o cli > js_secretfinder.txt\n"
             "# Custom regex sweep for things truffle misses\n"
             "rg -i 'aws_secret|aws_access|stripe_(test|live)|sk_live_|sk_test_|xoxb-|xoxp-|xapp-|pk_live_|pk_test_|api[_-]?key|client[_-]?secret|firebase|sendgrid|twilio|mailgun|github_token|ghp_|ghu_|ghs_|jwt|bearer\\s+[a-z0-9]+|password\\s*[:=]\\s*[\"\\']' js/"),
            ("Sourcemap recovery (gold mine)",
             "for u in $(cat js_urls.txt); do\n"
             "  curl -sk --max-time 10 \"$u.map\" -o /tmp/x.map && [ -s /tmp/x.map ] && echo \"FOUND .map: $u.map\"\n"
             "done\n"
             "# Then unpack:\n"
             "npx sourcemap-explorer file.js.map\n"
             "# OR\n"
             "git clone https://github.com/denandz/sourcemapper && go run sourcemapper.go -url \"https://example.com/main.js.map\" -output recovered/"),
            ("DOM XSS sink hunting in client JS",
             "rg -n 'document\\.write|innerHTML\\s*=|outerHTML\\s*=|insertAdjacentHTML|\\.html\\(|eval\\(|setTimeout\\([\"\\']\\\\$|setInterval\\([\"\\']|Function\\(|setAttribute\\((?:[\"\\'](?:on|src|href))|location\\s*=|location\\.href|location\\.replace|location\\.assign|window\\.open|postMessage' js/"),
            ("postMessage handlers (great for XSS / DOM clobbering chains)",
             "rg -n 'addEventListener\\([\"\\']message[\"\\']' js/ -A 10"),
            ("Webpack bundle deobfuscation (when source maps unavailable)",
             "# Unminify visually\n"
             "find js/ -name '*.js' -size +50k -exec js-beautify -o {}.pretty {} \\;\n"
             "# Try debowerify / unwebpack\n"
             "npx unminify js/main.js > main.unminified.js"),
        ],
        "edge": [
            "**Lazy-loaded chunks** — main bundle dynamically imports `/static/js/chunk-*.js`. Crawl + the manifest in `runtime.*.js` gives you the chunk graph.",
            "**Source maps in prod** — devs forget to strip them. Always check for `//# sourceMappingURL=` at the bottom of every JS file.",
            "**Service workers** — `sw.js` often caches API URLs and lists endpoints not used in the visible app.",
            "**`window.__INITIAL_STATE__`** — Server-rendered SPAs leak full user objects, role lists, feature flags. Grep page source for `__INITIAL_STATE__`, `__APOLLO_STATE__`, `__NEXT_DATA__`, `__NUXT__`.",
            "**Internal API hostnames** — leaked in client JS as fallback URLs. `https://api-internal.corp.example.com` not in your subdomain list = recon win.",
        ],
    },
    "06_wayback_historical.md": {
        "title": "Wayback / Historical URL Mining",
        "trigger": "after passive recon; before content discovery",
        "what": "Archive.org, CommonCrawl, AlienVault OTX, URLScan.io, and CertSpotter store snapshots of URLs that may no longer be in the live app — but the parameters, paths, and behaviors often still work, sometimes more vulnerable than current code.",
        "tools": [
            "gau (gauplus) — pulls from waybackmachine + AlienVault + CommonCrawl + URLScan.io",
            "waybackurls — archive.org only",
            "urlhunter — date-bounded archive search",
            "github-endpoints — pull URL strings from leaked code",
            "katana (PD) — has -jsl flag to also pull from JS",
            "uro — dedup URLs by template",
        ],
        "commands": [
            ("Pull all historical URLs",
             "echo example.com | gau --subs --threads 10 > wayback_gau.txt\n"
             "echo example.com | waybackurls > wayback_wbu.txt\n"
             "echo example.com | urlhunter -d 30d > wayback_uh.txt\n"
             "cat wayback_*.txt | sort -u > all_historical.txt\n"
             "wc -l all_historical.txt"),
            ("Dedup by URL template (reduce N×same param to 1)",
             "uro < all_historical.txt > all_historical_uniq.txt"),
            ("Filter to interesting extensions / signs of leak",
             "cat all_historical_uniq.txt | grep -E '\\.(php|asp|aspx|jsp|do|action|cgi|json|xml|env|bak|old|orig|backup|swp|tmp|sql|tar|tar\\.gz|zip|7z|rar|log|conf|config|cnf|ini|yml|yaml|pem|key|crt|p12|pfx|properties|rb|py|pl|sh|wsdl|wadl|swagger|openapi)(\\?|$)' > sus_extensions.txt"),
            ("Extract parameters",
             "cat all_historical_uniq.txt | unfurl --unique keys > param_names.txt\n"
             "cat all_historical_uniq.txt | qsreplace FUZZ > urls_for_fuzzing.txt"),
            ("Diff: historical vs current (find resurrected endpoints / removed-but-still-live)",
             "comm -23 <(sort all_historical_uniq.txt) <(sort current_crawl.txt) > only_in_historical.txt\n"
             "# Test if any of these still respond\n"
             "httpx -l only_in_historical.txt -mc 200,401,403 -threads 100 -silent > resurrected.txt"),
            ("Pull historical JS specifically (often dropped in newer builds, still hosted)",
             "cat all_historical_uniq.txt | grep -E '\\.js(\\?|$)' > historical_js.txt\n"
             "wget -i historical_js.txt -P historical_js/  # download for secret scan\n"
             "trufflehog filesystem historical_js/ > historical_js_secrets.txt"),
            ("Pull historical robots.txt + sitemap.xml diffs (often disclose admin paths)",
             "for snap in $(curl -s \"http://web.archive.org/cdx/search/cdx?url=example.com/robots.txt&output=text&fl=timestamp,original&from=20150101\" | awk '{print $1}'); do\n"
             "  echo \"=== $snap ===\"; curl -s \"https://web.archive.org/web/$snap/https://example.com/robots.txt\"\n"
             "done > robots_history.txt"),
        ],
        "edge": [
            "**Soft 404 in archives** — archive page may render but be archived during a maintenance redirect. Spot-check before fuzzing.",
            "**Private archive pages** — some are not crawled because of `robots.txt`; URLScan.io often has them.",
            "**API contract leakage** — old `/swagger.json`, `/openapi.json`, `/api-docs` paths often hosted historically; fetch via wayback timetravel.",
            "**JS files with secrets** — old JS bundles may still have `apiKey: '...'` that was rotated, but sometimes wasn't (rotation is hard). Always test live.",
            "**Internal staging URLs** — `staging.example.com` might be archived even if no longer DNS-live; pivot for new subdomains.",
        ],
    },
    "07_port_scanning_services.md": {
        "title": "Port Scanning & Service Discovery",
        "trigger": "you have a netblock or IP list; need full TCP/UDP service map",
        "what": "Beyond top-1000 web ports — find management interfaces, admin panels, queue brokers, DBs, internal services that drift onto the public IP space.",
        "tools": [
            "naabu (PD) — fast SYN-style discovery",
            "masscan — full /16 in minutes if rate is high",
            "rustscan — fast wrapper that hands off to nmap",
            "nmap — version + script + OS detection (gold standard)",
            "smap — shodan-backed nmap-compatible (returns Shodan's already-scanned data; fully passive)",
        ],
        "commands": [
            ("Full TCP scan, exclude CDN ranges (avoid noise)",
             "naabu -list netblocks.txt -p - -rate 10000 -exclude-cdn -o ports_full.txt"),
            ("masscan alternative",
             "sudo masscan -p1-65535 --rate 25000 -iL netblocks.txt -oG masscan.gnmap"),
            ("Nmap version + script scan against discovered open ports",
             "# Build target spec from naabu output\n"
             "awk -F: '{print $1\":\"$2}' ports_full.txt > host_port.txt\n"
             "# Run nmap with vuln scripts\n"
             "nmap -sV -sC -O -Pn --script=vulners,vuln,banner,http-enum,smb-enum-shares,ftp-anon,smb-vuln-* \\\n"
             "  -iL <(awk -F: '{print $1}' ports_full.txt | sort -u) -p $(awk -F: '{print $2}' ports_full.txt | sort -u | tr '\\n' ',') \\\n"
             "  -oA nmap_full"),
            ("Targeted hunt for HIGH-VALUE management ports",
             "# 9200,9300 (Elasticsearch), 27017 (MongoDB), 6379 (Redis), 5432 (PG), 3306 (MySQL),\n"
             "# 11211 (Memcached), 5984 (CouchDB), 1521 (Oracle), 1433 (MSSQL),\n"
             "# 8500 (Consul), 4040 (Spark), 6066 (Spark master), 7077 (Spark master),\n"
             "# 8086 (InfluxDB), 5601 (Kibana), 15672 (RabbitMQ mgmt), 8161 (ActiveMQ),\n"
             "# 9000 (SonarQube/Portainer), 3000 (Grafana), 8081 (Jenkins UNCONF), 8080 (Jenkins/Tomcat),\n"
             "# 7474 (neo4j), 9090 (Prometheus), 8888 (Jupyter), 9870/50070 (Hadoop),\n"
             "# 2375/2376 (Docker daemon), 6443/10250 (k8s), 4243 (Docker), 28017 (MongoDB http),\n"
             "# 8443/8888 (admin web), 50000 (DB2/SAP), 5985/5986 (WinRM), 5900-5902 (VNC)\n"
             "naabu -list netblocks.txt -p 9200,9300,27017,6379,5432,3306,11211,5984,1521,1433,8500,8086,5601,15672,8161,9000,3000,8081,8080,7474,9090,8888,9870,50070,2375,2376,6443,10250,4243,28017,8443,50000,5985,5986,5900,5901,5902 -rate 5000 -o highvalue_ports.txt"),
            ("Passive port scan via Shodan (no packets to target)",
             "smap -iL netblocks.txt -oG smap.gnmap   # uses Shodan API"),
            ("UDP top-100 (slow but catches DNS, SNMP, NTP, IPMI, MikroTik)",
             "sudo nmap -sU --top-ports 100 -sV -iL netblocks.txt -oA nmap_udp"),
        ],
        "edge": [
            "**WAF / IPS triggers** — masscan at >50k pps will get IP blacklisted. Throttle. Use VPS rotation.",
            "**Filtered ports** — `filtered` ≠ closed. Sometimes service is alive but firewalled. Re-test from VPS in different region.",
            "**Cloud LB ranges** — AWS/Azure/GCP LB ranges scan-noisy and meaningless. Filter via `cdncheck`.",
            "**Honeypots** — if every port responds and banners are generic, suspect honeypot. Confirm via `nmap --script=http-honeypot` or `shodan honeyscore IP`.",
            "**Wildcard SNI** — same IP serves many vhosts; need to swap `Host:` header to find the live one.",
        ],
    },
    "08_fingerprinting_tech_stack.md": {
        "title": "Fingerprinting Tech Stack",
        "trigger": "you have a live HTTP service; need to know framework + WAF + libraries before payload crafting",
        "what": "Identify framework, server, language, ORM, CMS, WAF, CDN, JS libs, and version numbers — these dictate which exploit primitives apply (e.g., Spring SpEL vs Twig SSTI vs Jinja2).",
        "tools": [
            "httpx -tech-detect (Wappalyzer)",
            "wappalyzer CLI",
            "whatweb",
            "nuclei -t http/technologies/ (PD official)",
            "wafw00f, cdncheck, retire.js, JSDeps (Burp ext)",
            "Favicon hash → Shodan/FOFA pivot",
            "HTML comments + meta tags + cookie names + JS globals + error pages",
        ],
        "commands": [
            ("Tech detect at scale",
             "httpx -l alive.txt -tech-detect -web-server -title -status-code -ip -cdn -follow-redirects -json -o tech.jsonl\n"
             "cat tech.jsonl | jq -r 'select(.tech) | \"\\(.url)\\t\\(.tech | join(\",\"))\"' | sort -u"),
            ("WAF detection",
             "wafw00f -i alive.txt -o wafw00f.txt\n"
             "# Manual confirmation — Cloudflare leaks via Server: cloudflare; Akamai via X-Cache or AkamaiGHost; AWS WAF via x-amzn-RequestId on block; Imperva via X-Iinfo; Sucuri via X-Sucuri-ID; F5 via BIGipServer cookie."),
            ("Favicon hash pivot",
             "python3 -c '\n"
             "import mmh3, requests, codecs, sys\n"
             "for u in sys.argv[1:]:\n"
             "  try:\n"
             "    r = requests.get(u + \"/favicon.ico\", timeout=5, verify=False)\n"
             "    if r.status_code == 200 and r.content:\n"
             "      print(u, mmh3.hash(codecs.encode(r.content, \"base64\")))\n"
             "  except: pass\n"
             "' $(cat alive.txt)\n"
             "# Then Shodan: http.favicon.hash:HASH"),
            ("Run nuclei tech detection templates",
             "nuclei -l alive.txt -t http/technologies/ -severity info -silent -o tech_nuclei.txt"),
            ("Identify retired JS libs (CVE candidates)",
             "# retire.js scan over saved JS\n"
             "retire --jspath js/ --outputformat json --outputpath retire.json\n"
             "# Or nuclei JS templates\n"
             "nuclei -l alive.txt -t http/exposures/ -severity medium,high,critical"),
            ("Cookie + header forensics",
             "for u in $(cat alive.txt); do\n"
             "  curl -sk -D /dev/stdout -o /dev/null --max-time 8 \"$u\" | head -40\n"
             "  echo \"=== $u ===\"\n"
             "done > headers.txt\n"
             "# Look for: Set-Cookie names (PHPSESSID, JSESSIONID, ASP.NET_SessionId, session, connect.sid (Express), laravel_session, _csrf, csrftoken (Django), AWSALB)\n"
             "# X-Powered-By: PHP/X.Y, ASP.NET, Express, JBoss, Tomcat\n"
             "# Server: Apache, nginx, IIS, Caddy, AmazonS3, AzureStorage, GoogleFrontend"),
        ],
        "edge": [
            "**Multiple stacks behind reverse proxy** — `Server: nginx` upstream is Spring; `X-Powered-By: PHP` may be a sidecar. Hit different paths.",
            "**Generic WAF on top hides framework errors** — provoke a 500 by malformed JSON / large header / weird method, then read upstream error page directly.",
            "**CDN strips `Server` header** — pivot via TLS handshake fingerprinting (JA3/JARM).",
            "**JARM fingerprint** — `jarm example.com:443`; same JARM across hosts = same TLS stack vendor (e.g., Cloudflare-fronted).",
            "**HTTP/2 only services** — old WAFs / scanners ignore them; force HTTP/2 via `curl --http2` or `httpx -http2`.",
        ],
    },
    "09_github_dorks_code_leaks.md": {
        "title": "GitHub / GitLab / Bitbucket Dorks & Code Leaks",
        "trigger": "any target with employees on GitHub; almost always",
        "what": "Public code search reveals: hardcoded creds, internal hostnames, API keys, JWT signing secrets, OAuth client_secret, AWS keys, DB strings, internal Slack webhooks, PII test fixtures.",
        "tools": [
            "gitdorker — automated dork runner with multi-token rotation",
            "trufflehog — secret scanner with verifiers",
            "gitleaks — fast regex-based secret scanner",
            "github-search (gwen001) — by-organization scrape",
            "github-subdomains (gwen001) — pulls subs from leaked code",
            "git-hound — recursive scan + verify",
            "goop — diff-based GitHub recon",
            "Pastebin / paste.ee / 0bin / ghostbin — keep an eye via bin scrapers (psbdmp, pastebeen)",
        ],
        "commands": [
            ("Run dorks via gitdorker (handles rate limiting + token rotation)",
             "gitdorker -tf ~/.config/gitdorker/tokens.txt -q example.com -d ~/tools/gitdorker/Dorks/medium_dorks.txt -o gitdorker_results/ -ev 0.5"),
            ("Truffle org scan with verifiers",
             "trufflehog github --org=examplecorp --json --concurrency=8 --only-verified > truffle_examplecorp.json\n"
             "# Per-user (employees you found via LinkedIn)\n"
             "for u in $(cat employees_github_handles.txt); do\n"
             "  trufflehog github --user=\"$u\" --json --only-verified >> truffle_users.json\n"
             "done"),
            ("Manual API code search (granular)",
             "for q in 'password' 'api_key' 'secret' 'jwt' 'token' 'aws_secret' 'BEGIN RSA PRIVATE KEY' 'authorization: bearer' 'Set-Cookie:' 'admin' 'staging' 'internal'; do\n"
             "  curl -s -H \"Authorization: token $GITHUB_TOKEN\" \\\n"
             "    \"https://api.github.com/search/code?q=%22example.com%22+$q&per_page=100\" \\\n"
             "    | jq -r '.items[] | \"[\\(.repository.full_name)] \\(.html_url)\"'\n"
             "done > gh_code_search.txt"),
            ("GitLab + Bitbucket equivalents",
             "# GitLab API (key in $GITLAB_TOKEN)\n"
             "curl -s --header \"PRIVATE-TOKEN: $GITLAB_TOKEN\" \\\n"
             "  \"https://gitlab.com/api/v4/search?scope=blobs&search=example.com&per_page=100\"\n"
             "# Bitbucket\n"
             "curl -s -u \"$BB_USER:$BB_TOKEN\" \\\n"
             "  \"https://api.bitbucket.org/2.0/repositories/?role=member&q=name~%22example%22\""),
            ("Find deleted commits (gitleaks --redact -v + reflog)",
             "git clone --mirror https://github.com/example/repo.git\n"
             "cd repo.git\n"
             "gitleaks detect --no-git -v\n"
             "# To get every blob, including dangling:\n"
             "git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(rest)' | awk '$1==\"blob\" {print $2}' > all_blobs.txt"),
            ("Pastebin scrape (live)",
             "psbdmp search example.com\n"
             "# OR scrape paste.ee API\n"
             "curl -s 'https://paste.ee/api/v1/pastes/?key=$PASTEEE_KEY&q=example.com'"),
            ("Dockerhub leaked images",
             "# Find images tagged with company name\n"
             "curl -s 'https://hub.docker.com/v2/search/repositories/?query=example' | jq -r '.results[].repo_name'\n"
             "# Pull + extract layers + grep for secrets\n"
             "docker pull example/app:latest\n"
             "docker save example/app:latest | tar -xv -O '*.tar' | tar -xv | grep -rE 'AKIA|password|secret' /tmp/extracted/"),
            ("npm / PyPI / RubyGems search by org email",
             "# npm packages with author email matching @example.com\n"
             "npm search --json author:example.com | jq '.[] | .name'\n"
             "# PyPI\n"
             "curl -s 'https://pypi.org/search/?q=example' | grep -oE '/project/[^/]+/' | sort -u"),
        ],
        "dorks": """
# Place these in `dorks/medium_dorks.txt` and rotate via gitdorker

# Auth / Secrets
"example.com" password
"example.com" api_key
"example.com" apikey
"example.com" "secret_key"
"example.com" "client_secret"
"example.com" "auth_token"
"example.com" jwt
"example.com" "Bearer"
"example.com" "aws_secret_access_key"
"example.com" "aws_access_key_id"
"example.com" AKIA
"example.com" SLACK_TOKEN
"example.com" "stripe_api_key"
"example.com" "twilio_auth_token"
"example.com" "github_token"
"example.com" "ghp_"
"example.com" "ghs_"
"example.com" "gho_"
"example.com" "BEGIN RSA PRIVATE KEY"
"example.com" "BEGIN OPENSSH PRIVATE KEY"
"example.com" "BEGIN DSA PRIVATE KEY"
"example.com" "BEGIN EC PRIVATE KEY"
"example.com" "BEGIN PGP PRIVATE KEY"

# Files
"example.com" filename:.env
"example.com" filename:.npmrc _auth
"example.com" filename:.dockercfg auth
"example.com" filename:.git-credentials
"example.com" filename:wp-config.php
"example.com" filename:credentials aws_access_key_id
"example.com" filename:id_rsa
"example.com" filename:id_dsa
"example.com" filename:id_ecdsa
"example.com" filename:id_ed25519
"example.com" filename:.htpasswd
"example.com" extension:pem private
"example.com" extension:ppk private
"example.com" extension:p12
"example.com" extension:pfx
"example.com" extension:sql
"example.com" extension:bak
"example.com" extension:log
"example.com" extension:conf
"example.com" extension:cnf
"example.com" extension:config
"example.com" extension:sh "ssh"

# Internal infra
"example.com" "internal"
"example.com" "staging"
"example.com" "dev"
"example.com" "test.example.com"
"example.com" "vpn"
"example.com" "ldap"
"example.com" "mongodb://"
"example.com" "postgres://"
"example.com" "mysql://"
"example.com" "redis://"
"example.com" "amqp://"
"example.com" "smtp.example.com"
"example.com" "DB_PASSWORD"
"example.com" "DATABASE_URL"

# Cloud-specific
"example.com" s3://
"example.com" "s3.amazonaws.com"
"example.com" "*.s3.amazonaws.com"
"example.com" "ec2-"
"example.com" "blob.core.windows.net"
"example.com" "googleapis.com"
"example.com" "storage.googleapis.com"
""",
        "edge": [
            "**Forks / mirrors / bots** — same secret may live in 10 forks. Dedup by file hash to triage faster.",
            "**Private repos accidentally public** — check the repo's history; sometimes was private then made public — old commits leak secrets.",
            "**Verified vs unverified** — trufflehog `--only-verified` is conservative. Run without first, then validate the high-conf ones.",
            "**Slack token live test** — `curl -s -X POST https://slack.com/api/auth.test -H \"Authorization: Bearer $token\"`; if `ok:true`, working — instant P1.",
            "**AWS creds live test** — `aws sts get-caller-identity` with the keys; if account ID matches the target, P1. Don't escalate beyond `sts:GetCallerIdentity` in PoC — triagers love minimum-impact PoCs.",
            "**Dependency Confusion candidates** — internal package names leaked in `package.json`, `requirements.txt`, `pom.xml`, `Gemfile.lock` → see `dependency_confusion.md`.",
        ],
    },
    "10_google_dorks.md": {
        "title": "Google / Bing / DuckDuckGo / Yandex Dorks",
        "trigger": "any time; but especially when starting on a new program",
        "what": "Search-engine dorks surface admin panels, exposed endpoints, leaked docs, public buckets, sub-zone exposures. Free, fast, and the engines have indexed things you'd never find via crawl.",
        "tools": [
            "Google search operators",
            "Bing operators (slightly different syntax)",
            "DuckDuckGo (less rate-limited; bangs to other engines)",
            "Yandex (best for Russian-speaking targets / less indexed corners)",
            "uDork — automates dork lists",
            "GoogD0rker (script to rotate UAs + proxies)",
        ],
        "dorks_by_category": """
## Subdomain / Asset Discovery
site:*.example.com -www
site:example.com -site:www.example.com
site:example.com -site:blog.example.com -site:docs.example.com   # find unusual subs
site:example.com inurl:dev
site:example.com inurl:staging
site:example.com inurl:test
site:example.com inurl:internal
site:example.com -inurl:www -inurl:blog -inurl:docs

## Login Pages & Admin Panels
site:example.com inurl:login
site:example.com inurl:admin
site:example.com inurl:wp-admin
site:example.com inurl:dashboard
site:example.com intitle:"admin login"
site:example.com intitle:"sign in"
site:example.com inurl:portal
site:example.com inurl:console
site:example.com inurl:management

## Sensitive Files
site:example.com ext:env
site:example.com ext:log
site:example.com ext:bak | ext:old | ext:sql | ext:zip | ext:tar | ext:tar.gz | ext:rar
site:example.com ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini
site:example.com ext:json
site:example.com ext:xml
site:example.com ext:pdf "confidential"
site:example.com ext:pdf "internal use only"
site:example.com filetype:pdf "password"

## Backup / Sourcecode Disclosure
site:example.com ext:bak
site:example.com ext:swp
site:example.com inurl:.git
site:example.com inurl:.svn
site:example.com inurl:.hg
site:example.com inurl:.DS_Store
site:example.com inurl:.idea
site:example.com inurl:wp-content/backup
site:example.com inurl:dump.sql
site:example.com inurl:db.sql

## API / Swagger / GraphQL
site:example.com inurl:api
site:example.com inurl:swagger
site:example.com inurl:swagger-ui
site:example.com inurl:openapi
site:example.com inurl:redoc
site:example.com inurl:api-docs
site:example.com inurl:graphql
site:example.com inurl:graphiql
site:example.com inurl:playground
site:example.com inurl:apollo
site:example.com inurl:wsdl

## Errors / Stack Traces (vuln signal)
site:example.com "stack trace"
site:example.com "Whitelabel Error Page"
site:example.com "PHP Parse error"
site:example.com "Warning: include"
site:example.com "Fatal error"
site:example.com "ORA-00921"
site:example.com "Microsoft OLE DB Provider"
site:example.com "java.lang.NullPointerException"
site:example.com "Traceback (most recent call last)"
site:example.com intext:"sql syntax near"
site:example.com intext:"Microsoft VBScript runtime error"
site:example.com intext:"Server.MapPath"

## Cloud Buckets via Search
"example" site:s3.amazonaws.com
"example" inurl:storage.googleapis.com
"example" inurl:blob.core.windows.net
inurl:s3.amazonaws.com "example"
inurl:digitaloceanspaces.com "example"
inurl:linodeobjects.com "example"

## Document Disclosure
site:example.com filetype:xls | filetype:xlsx
site:example.com filetype:doc | filetype:docx
site:example.com filetype:csv "password"
site:example.com filetype:txt password

## SSO / OAuth Misconfig
site:example.com inurl:redirect_uri
site:example.com inurl:callback
site:example.com inurl:oauth
site:example.com inurl:saml
site:example.com inurl:sso

## Reflected Param Reflection (for XSS hunting)
site:example.com inurl:redirect=
site:example.com inurl:url=
site:example.com inurl:returnTo=
site:example.com inurl:next=
site:example.com inurl:dest=
site:example.com inurl:return=

## Open Redirect Indicators
site:example.com inurl:redir=
site:example.com inurl:goto=
site:example.com inurl:return_url=
site:example.com inurl:rurl=

## SSRF Indicators
site:example.com inurl:url=
site:example.com inurl:fetch=
site:example.com inurl:img=
site:example.com inurl:image=
site:example.com inurl:proxy=
site:example.com inurl:webhook=

## File Upload Indicators
site:example.com inurl:upload
site:example.com inurl:fileupload
site:example.com inurl:attach
site:example.com intitle:"upload" "file"

## Hidden Subdirs / Index of
site:example.com intitle:"index of /"
site:example.com intitle:"index of" "parent directory"
site:example.com intitle:"index of" backup
site:example.com intitle:"index of" .git

## Vendor-Specific (Jira, Confluence, Jenkins, GitLab, Bamboo, Crowd, Slack)
site:example.com inurl:jira
site:example.com inurl:confluence
site:example.com inurl:jenkins
site:example.com inurl:gitlab
site:example.com inurl:bamboo
site:example.com inurl:crowd
site:example.com inurl:slack

## Pastebin-leaked
site:pastebin.com example.com
site:gist.github.com example.com
site:paste.ee example.com
site:0bin.net example.com
""",
        "commands": [
            ("uDork — automate a dork list",
             "udork -t example.com -d ~/tools/uDork/dorks.txt -o results.html"),
            ("Manual rate-limited rotation (custom Python)",
             "# scripts/google_dorks.py reads dorks.txt, uses serpapi or googlesearch-python\n"
             "python3 scripts/google_dorks.py -d example.com -i dorks.txt -o dork_hits.txt"),
        ],
        "edge": [
            "**Captcha after 20 queries** — rotate user agent + proxy + add 5–15s sleep. SerpApi or Bing API are paid alternatives.",
            "**Site sometimes blocks robots** — pages exist but don't appear in Google. Use Bing/Yandex/Baidu/Naver — different crawlers.",
            "**`-www` bias** — operators normalize, so `-site:www.example.com` may not strip all variants. Combine with `-inurl:www`.",
            "**Cached versions** — even after the site removes a page, Google's cache may still hold it; click `Cached` link or use `cache:` operator (deprecated but archive.org timetravel works similarly).",
        ],
    },
    "11_shodan_censys_fofa.md": {
        "title": "Shodan / Censys / FOFA / ZoomEye / Hunter.how / BinaryEdge / Quake360",
        "trigger": "any time; gold for finding Cloudflare-bypass origin IPs and exposed mgmt panels",
        "what": "These engines have already scanned the entire IPv4 space. You query their database — fully passive — and pivot via fingerprints (favicon hash, JARM, TLS cert SAN, http title, http body hash) to discover assets you'd never find via DNS.",
        "tools": [
            "shodan CLI + API",
            "censys CLI + API",
            "FOFA web UI / API + base64-encoded queries",
            "ZoomEye CLI",
            "BinaryEdge",
            "Hunter.how",
            "Netlas.io",
            "Quake360 (CN-only)",
        ],
        "queries_by_engine": """
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
""",
        "favicon_pivot": """
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
""",
        "commands": [
            ("Shodan find origin behind Cloudflare",
             "# Cert SAN match but NOT in CF range\n"
             "shodan search 'ssl.cert.subject.cn:\"example.com\" -country:\"US\"' | grep -v 'cloudflare'\n"
             "# OR favicon match outside CF\n"
             "fhash=$(python3 favicon_hash.py https://example.com)\n"
             "shodan search \"http.favicon.hash:$fhash\""),
            ("Censys cert SAN sweep",
             "censys search 'services.tls.certificates.leaf_data.names: \"example.com\"' --pages 5 -o censys_results.json"),
            ("FOFA via Python",
             "import base64, requests\n"
             "q = 'cert=\"example.com\"'\n"
             "qb = base64.b64encode(q.encode()).decode()\n"
             "r = requests.get(f'https://fofa.info/api/v1/search/all?email={EMAIL}&key={KEY}&qbase64={qb}&size=10000')\n"
             "for line in r.json()['results']: print(line)"),
            ("Bulk JARM scan against shortlisted IPs",
             "jarm -i ips.txt -o jarm.txt   # then group by JARM to identify shared infra"),
        ],
        "edge": [
            "**Stale Shodan data** — last seen 6 months ago; service may have moved. Confirm with live `httpx`.",
            "**FOFA query encoding** — must be base64; mistake = empty results.",
            "**Origin behind Cloudflare** — best signals: cert SAN match + non-CF ASN; favicon hash match + non-CF ASN; HTTP body hash match.",
            "**Internal services exposed** — Kibana 5601, Elasticsearch 9200, Jenkins 8080 unauth; Mongo 27017 — instant P1 if confirmed exposed.",
            "**Sensors / honeypots** — same banner across many IPs in different geos = likely honeypot grid.",
        ],
    },
    "12_cloud_recon_aws_gcp_azure.md": {
        "title": "Cloud Recon (AWS / GCP / Azure)",
        "trigger": "any modern target; almost always cloud-hosted",
        "what": "Discover exposed S3 buckets, public Azure blobs, GCP Cloud Storage, dangling subdomains pointing at decommissioned cloud resources, exposed Lambda function URLs, public Cognito user pools, exposed App Runner / ECS / GKE services.",
        "tools": [
            "cloud_enum (initstring) — sweep AWS / GCP / Azure for permutations of company names",
            "s3scanner — bucket existence + perms + listing",
            "GCPBucketBrute — GCP equivalent",
            "MicroBurst — Azure-specific (PS module)",
            "scoutsuite — when you have read creds, audits everything",
            "prowler — same",
            "pacu — AWS post-exploit framework (READ-ONLY modules for recon)",
            "trufflehog — over downloaded bucket contents",
        ],
        "commands": [
            ("cloud_enum — broad sweep",
             "cloud_enum --keyword example --keyword examplecorp --keyword example-prod --keyword example-dev --keyword example-staging --keyword example-internal --logfile cloud_enum.log"),
            ("S3 bucket enumeration with naming permutations",
             "# Build wordlist\n"
             "for prefix in '' 'dev-' 'prod-' 'staging-' 'qa-' 'test-' 'backup-' 'data-' 'logs-' 'media-' 'static-' 'assets-' 'public-' 'private-' 'internal-' 'cdn-' 'images-' 'uploads-' 'web-' 'api-' 'app-'; do\n"
             "  for suffix in '' '-dev' '-prod' '-staging' '-qa' '-test' '-backup' '-data' '-logs' '-prd'; do\n"
             "    echo \"${prefix}example${suffix}\"; echo \"${prefix}examplecorp${suffix}\"\n"
             "  done\n"
             "done | sort -u > bucket_names.txt\n"
             "# Test\n"
             "s3scanner -bucket-file bucket_names.txt -enumerate-bucket-objects -threads 50 -output s3_results.json"),
            ("Test for AWS Cognito leaks",
             "# Any unauth identity pool?\n"
             "aws cognito-identity get-id --identity-pool-id us-east-1:xxxx --no-sign-request   # if returns IdentityId, pool is open\n"
             "aws cognito-identity get-credentials-for-identity --identity-id $ID --no-sign-request   # creds = AssumeRole into account"),
            ("Azure storage blob enumeration",
             "# DNS-based existence test\n"
             "for n in example examplecorp examplestg exampledev; do\n"
             "  for variant in storage data backup logs files; do\n"
             "    h=\"${n}${variant}.blob.core.windows.net\"\n"
             "    dig +short \"$h\" @1.1.1.1 | head -1 | grep -q '\\.' && echo \"EXISTS: $h\"\n"
             "  done\n"
             "done\n"
             "# Then test list\n"
             "for h in $exists; do curl -sI \"https://$h/?comp=list\"; done"),
            ("GCP Cloud Storage",
             "# Bucket existence\n"
             "for n in example example-prod example-data; do\n"
             "  curl -sI \"https://storage.googleapis.com/$n/\" | head -1\n"
             "done\n"
             "# GCPBucketBrute\n"
             "python3 gcpbucketbrute.py -k example -u   # -u = unauth"),
            ("Lambda function URL discovery",
             "# Look for *.lambda-url.<region>.on.aws hostnames in: JS files, wayback, sub enum, GitHub\n"
             "rg -oE '[a-z0-9]+\\.lambda-url\\.[a-z0-9-]+\\.on\\.aws' js/ wayback/ -h | sort -u"),
            ("CloudFront distribution discovery",
             "# Sub points to *.cloudfront.net but distribution is unclaimed → takeover\n"
             "for sub in $(cat alive.txt); do\n"
             "  cname=$(dig +short cname \"$sub\" @1.1.1.1 | tail -1)\n"
             "  if echo \"$cname\" | grep -q 'cloudfront.net'; then\n"
             "    code=$(curl -sk -o /dev/null -w '%{http_code}' \"https://$sub/\")\n"
             "    [ \"$code\" = \"403\" ] && curl -sk \"https://$sub/\" | grep -q 'Bad request' && echo \"DANGLING: $sub → $cname\"\n"
             "  fi\n"
             "done"),
            ("AWS access key validity test (passive — only sts:GetCallerIdentity)",
             "AWS_ACCESS_KEY_ID=AKIA... AWS_SECRET_ACCESS_KEY=... aws sts get-caller-identity --no-paginate"),
            ("Azure AD tenant discovery (no auth needed)",
             "curl -sI \"https://login.microsoftonline.com/example.com/.well-known/openid-configuration\"\n"
             "# Returns tenant ID + endpoints. Pivot to MSGraph for user enum if guest invite is open."),
        ],
        "edge": [
            "**Bucket exists but ListObjects denied** — try `?max-keys=0` or `Range:` header tricks; sometimes individual GET on guessed key paths works. Generate keys from JS file references.",
            "**Lambda function URL with `AuthType: NONE`** — instant unauth RCE proxy if function logic eval-uates input.",
            "**Azure storage `?comp=list`** — anonymous-read containers expose every blob name.",
            "**GCP IAM scoped only to `roles/viewer`** — still grants `compute.instances.list`, `secretmanager.secrets.list` (sometimes), `storage.objects.list` — material disclosure.",
            "**CloudFront `Bad request: Unable to forward to host`** — origin host header doesn't match — distribution may still be claimable.",
            "**S3 takeover via 'NoSuchBucket'** — sub CNAMEs to `bucket.s3.amazonaws.com`, returns NoSuchBucket → register that bucket name → takeover.",
        ],
    },
    "13_mobile_app_recon.md": {
        "title": "Mobile App Recon (Android / iOS)",
        "trigger": "any program with a mobile app in scope; OR pivot from a web target's app",
        "what": "Pull APK/IPA, decompile, scrape URLs/secrets/intent filters/deep links, identify backend API endpoints not exposed in the web app.",
        "tools": [
            "apkmd / Raccoon — pull APK from Play Store URL",
            "ipa-extractor — pull IPA via Apple Configurator or AppDb / iMazing",
            "apkleaks — secret scanner",
            "jadx-gui / jadx-cli — decompile to Java",
            "apktool — smali + resources",
            "MobSF — full static + dynamic analysis (browser UI)",
            "androguard — Python lib for programmatic analysis",
            "frida + objection — dynamic instrumentation",
            "burp + magisk-trust-user-certs / Frida cert pin bypass",
        ],
        "commands": [
            ("Pull APK by package name",
             "pip install raccoon-apkmd\n"
             "apkmd download com.example.app -o example.apk"),
            ("Static URL + secret extraction",
             "apkleaks -f example.apk -o apkleaks.txt\n"
             "# Manual\n"
             "apktool d -f example.apk -o ext/\n"
             "rg -nIE 'https?://[a-zA-Z0-9./_?=&%-]+' ext/ | sort -u > urls_in_apk.txt\n"
             "rg -nIE '(api[_-]?key|secret|token|password|jwt|firebase|aws_(access|secret)|sk_(live|test)_)[\"\\'`:= ]' ext/ > secrets_in_apk.txt"),
            ("Find Firebase databases (often misconfig)",
             "rg -oE '[a-z0-9-]+\\.firebaseio\\.com' ext/ | sort -u | while read fb; do\n"
             "  curl -s \"https://$fb/.json\" | head -c 200\n"
             "  echo \" <- $fb\"\n"
             "done"),
            ("Dump intent filters + deep links + exported components (Android)",
             "apktool d example.apk -o ext/\n"
             "# AndroidManifest.xml — exported activities/services/providers\n"
             "xmlstarlet sel -t -m '//activity[@android:exported=\"true\"]' -v '@android:name' -n ext/AndroidManifest.xml\n"
             "# OR drozer\n"
             "drozer console connect\n"
             "  # run app.activity.info -a com.example.app -i\n"
             "  # run app.provider.info -a com.example.app\n"
             "  # run scanner.provider.injection -a com.example.app\n"
             "  # run scanner.provider.traversal -a com.example.app"),
            ("iOS — class-dump + frida",
             "# Get IPA → dump classes\n"
             "class-dump-z -H Example.ipa -o classes/\n"
             "# Frida bypass cert pin (universal script)\n"
             "frida -U -f com.example.app -l ios-cert-pin-bypass.js --no-pause"),
            ("MobSF full report",
             "docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest\n"
             "# Upload APK/IPA in browser at http://localhost:8000"),
            ("Capture mobile traffic in Burp",
             "# Android: install Burp CA as system cert via magisk-trust-user-certs module\n"
             "# Set proxy: WiFi → Modify Network → Proxy Manual → 192.168.x.y:8080\n"
             "# For SSL pinning bypass:\n"
             "frida -U -l ssl-pinning-bypass.js -f com.example.app --no-pause\n"
             "# objection alternative\n"
             "objection -g com.example.app explore\n"
             "  # android sslpinning disable\n"
             "  # ios sslpinning disable"),
        ],
        "edge": [
            "**App-only API endpoints** — backend exposes `/api/v3/internal/...` only used by mobile, no auth on some routes assuming \"only mobile clients hit this\". Frequent finding.",
            "**Hardcoded API keys** — Firebase web API key (low risk by itself, but combined with Firestore rules misconfig = full DB read), Algolia search keys (admin vs search-only), Mapbox keys (often abused for DoS).",
            "**Insecure deep links** — `example://login?token=<attacker_token>` chains to ATO if app accepts arbitrary token.",
            "**Exported ContentProvider** — `content://com.example.app.provider/users` SQL injectable via `path` URI param.",
            "**WebView with `setJavaScriptEnabled(true)` + `addJavascriptInterface`** — any XSS in the loaded page = JS-to-native RCE.",
            "**Cleartext traffic flag** — `android:usesCleartextTraffic=\"true\"` in manifest = data interception viable.",
        ],
    },
    "14_api_discovery.md": {
        "title": "API Discovery",
        "trigger": "after web crawl + JS analysis; or 'find APIs on TARGET'",
        "what": "Identify REST endpoints, GraphQL schemas, gRPC services, WebSocket endpoints, internal APIs leaked in mobile/JS, and undocumented versions/methods. APIs are where business logic — and bug bounties — live.",
        "tools": [
            "katana / hakrawler / gospider crawls + JS endpoint extraction (jsluice, linkfinder)",
            "kiterunner — wordlist-based API endpoint discovery (uses SecLists/Discovery/Web-Content/api/)",
            "ffuf with API wordlists",
            "graphql-cop / clairvoyance / inql / graphw00f — GraphQL discovery + schema introspection",
            "grpcurl / grpc-tools — gRPC service discovery",
            "Burp 'API Discovery' (Pro feature) + JS Miner ext",
            "Postman / Insomnia / Bruno — for replay + fuzzing",
            "Swagger / OpenAPI / WSDL parser scripts",
        ],
        "commands": [
            ("Crawl + extract endpoints from JS",
             "katana -list alive.txt -d 5 -jc -kf all -aff -o crawl.txt\n"
             "find js/ -name '*.js' -exec jsluice urls -m '*' {} \\; | sort -u > endpoints_jsluice.txt\n"
             "cat crawl.txt endpoints_jsluice.txt | sort -u > all_endpoints.txt"),
            ("Find docs / schemas",
             "# Common paths\n"
             "for path in api openapi.json openapi.yaml swagger.json swagger.yaml swagger-ui swagger-ui.html api-docs api/v1 api/v2 api/v3 docs redoc graphql graphiql playground apollo wsdl actuator actuator/beans actuator/mappings actuator/env actuator/health; do\n"
             "  ffuf -u \"https://$TARGET/$path\" -mc 200,401,403 -ac -of csv -o /tmp/r.csv\n"
             "done\n"
             "# nuclei has templates for these\n"
             "nuclei -l alive.txt -t http/exposures/apis/ -severity info,low,medium,high,critical"),
            ("kiterunner — better than ffuf for APIs (does HEAD + scrambled methods)",
             "# Use the curated routes-large.kite\n"
             "kr scan https://example.com -A=apiroutes-210126:20210126 -o kr_results.txt\n"
             "kr brute https://example.com -w ~/wordlists/api/api-endpoints.txt -o kr_brute.txt"),
            ("GraphQL discovery + introspection",
             "# Find GraphQL endpoints\n"
             "for path in graphql graphiql api/graphql v1/graphql v2/graphql query subgraph; do\n"
             "  curl -sk -X POST \"https://$TARGET/$path\" -H 'Content-Type: application/json' \\\n"
             "    -d '{\"query\":\"{__typename}\"}' -o /dev/null -w \"%{http_code} https://$TARGET/$path\\n\"\n"
             "done\n"
             "# Introspect (often disabled in prod, but try)\n"
             "curl -sk -X POST https://$TARGET/graphql -H 'Content-Type: application/json' \\\n"
             "  --data '{\"query\":\"query IntrospectionQuery { __schema { queryType { name } mutationType { name } subscriptionType { name } types { ...FullType } directives { name description locations args { ...InputValue } } } } fragment FullType on __Type { kind name description fields(includeDeprecated: true) { name description args { ...InputValue } type { ...TypeRef } isDeprecated deprecationReason } inputFields { ...InputValue } interfaces { ...TypeRef } enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason } possibleTypes { ...TypeRef } } fragment InputValue on __InputValue { name description type { ...TypeRef } defaultValue } fragment TypeRef on __Type { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name } } } } } } } }\"}' \\\n"
             "  | jq . > schema.json\n"
             "# If introspection disabled → use clairvoyance to brute-force\n"
             "clairvoyance -o schema.json -w ~/wordlists/graphql/graphql-words.txt https://$TARGET/graphql\n"
             "# graphw00f — fingerprint engine (Apollo, Hasura, Relay, AWS AppSync, GraphQL Yoga, etc.)\n"
             "graphw00f -t https://$TARGET/graphql -d"),
            ("gRPC discovery",
             "grpcurl -plaintext $HOST:$PORT list   # if reflection enabled\n"
             "grpcurl -plaintext $HOST:$PORT list mypackage.MyService\n"
             "# Without reflection — need .proto files; sometimes leaked in JS / mobile / GitHub"),
            ("WebSocket discovery + connection",
             "# Find WS handshake endpoints in crawl\n"
             "rg -oE 'wss?://[^\\s\"\\'<>]+' js/ alive.txt > ws_endpoints.txt\n"
             "# Connect with wscat\n"
             "wscat -c \"wss://example.com/ws\" -H \"Authorization: Bearer $TOKEN\""),
            ("Detect API versioning",
             "# Same endpoint, different versions sometimes have different auth\n"
             "for v in 1 2 3 v1 v2 v3 latest internal beta legacy old; do\n"
             "  curl -sk -o /dev/null -w \"$v: %{http_code}\\n\" \"https://$TARGET/api/$v/users\"\n"
             "done"),
            ("Find OpenAPI / Swagger via favicon hash → Shodan",
             "# Many Swagger UIs share favicon hash. Pivot like this for org-wide discovery.\n"
             "shodan search 'http.favicon.hash:1606627656'   # default Swagger UI hash\n"
             "shodan search 'http.title:\"Swagger UI\" hostname:example.com'"),
        ],
        "edge": [
            "**Path versioning vs Header versioning** — `Accept: application/vnd.example.v1+json`. Test all variants.",
            "**Internal-only API hosts** — leaked in mobile/JS as fallback. `https://api-internal.example.com` may be reachable from internet despite naming.",
            "**Method confusion** — `GET /api/admin/users` returns 403, `POST` returns 200. Always test all methods (`OPTIONS` to enumerate, then HEAD/GET/POST/PUT/PATCH/DELETE).",
            "**Trailing slash behavior** — `/api/users` 401 vs `/api/users/` 200 — common framework routing inconsistency.",
            "**HTTP/2 method whitelist bypass** — some WAFs only know HTTP/1.1; send same request via HTTP/2 with `httpx --http2`.",
            "**GraphQL aliases** — bypass per-field rate limit with batched aliases (`x: user(id:1) y: user(id:2)`); also defense-evasion for IDOR.",
            "**Documentation rot** — Swagger lists endpoints that no longer exist; missing endpoints exist. Diff `/openapi.json` against actual probe.",
        ],
    },
    "15_content_discovery_fuzzing.md": {
        "title": "Content Discovery & Fuzzing",
        "trigger": "after recon; need hidden paths, params, files, methods",
        "what": "Wordlist-based brute force of paths, files, parameters, headers, HTTP methods, vhost names — discover content that's not linked anywhere.",
        "tools": [
            "ffuf — fast, recursive, scriptable",
            "feroxbuster — Rust, async, recursion built-in",
            "dirsearch — Python, has good wordlists bundled",
            "gobuster — fewer features but stable",
            "x8 — parameter discovery via response analysis",
            "arjun — parameter brute via diff",
            "ParamMiner (Burp ext) — by-product when you browse",
            "kiterunner — API-aware",
        ],
        "wordlists": """
## Default wordlist set (place in ~/wordlists/)
SecLists:
  Discovery/Web-Content/raft-large-directories.txt
  Discovery/Web-Content/raft-large-files.txt
  Discovery/Web-Content/raft-large-words.txt
  Discovery/Web-Content/big.txt
  Discovery/Web-Content/Common-PHP-Filenames.txt
  Discovery/Web-Content/CMS/wp_plugins.txt
  Discovery/Web-Content/api/api-endpoints.txt
  Discovery/Web-Content/api/objects.txt
  Discovery/Web-Content/api/api-endpoints-res.txt
  Fuzzing/LFI/LFI-Jhaddix.txt
  Fuzzing/SQLi/Generic-SQLi.txt
  Fuzzing/XSS/XSS-Jhaddix.txt
  Discovery/DNS/subdomains-top1million-110000.txt
  Passwords/Common-Credentials/10-million-password-list-top-10000.txt
  Discovery/Web-Content/burp-parameter-names.txt
  Discovery/Web-Content/AWS.txt

assetnote-wordlists (https://wordlists.assetnote.io):
  ApiObjects.txt
  parameters_top_1m.txt
  bruteforce-lists/api-endpoints.txt
  longtail/raft-large-files.txt

Onelistforall:
  https://github.com/six2dez/OneListForAll

Custom:
  one4all.txt = combine + sort -u all of the above
""",
        "commands": [
            ("ffuf — recursive directory + extension brute",
             "ffuf -u \"https://$TARGET/FUZZ\" \\\n"
             "  -w ~/wordlists/SecLists/Discovery/Web-Content/raft-large-directories.txt \\\n"
             "  -mc all -fc 404,403 -ac -recursion -recursion-depth 2 \\\n"
             "  -e .json,.xml,.bak,.old,.zip,.tar.gz,.tar,.7z,.rar,.git,.svn,.env,.yml,.yaml,.txt,.log,.sql,.bak,.swp,.tmp,.orig,.dist,.example,.config,.conf,.ini,.cfg \\\n"
             "  -t 50 -timeout 7 -p 0.05 -of json -o ffuf.json"),
            ("Fuzz HTTP methods",
             "for m in GET POST PUT PATCH DELETE OPTIONS HEAD TRACE CONNECT PROPFIND MKCOL COPY MOVE LOCK UNLOCK; do\n"
             "  curl -sk -o /dev/null -w \"$m %{http_code}\\n\" -X \"$m\" \"https://$TARGET/api/admin\"\n"
             "done"),
            ("Vhost / Host header brute",
             "ffuf -u \"https://$TARGET/\" -H \"Host: FUZZ.example.com\" \\\n"
             "  -w ~/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt \\\n"
             "  -mc 200,301,302 -fs 0 -ac -t 50 -of csv -o vhost.csv"),
            ("Parameter brute (arjun)",
             "arjun -u 'https://example.com/api/data' -m POST --json --headers \"Authorization: Bearer $T\" --stable\n"
             "# x8 alternative\n"
             "x8 -u 'https://example.com/api/data' -X POST -m GET POST -w ~/wordlists/SecLists/Discovery/Web-Content/burp-parameter-names.txt"),
            ("Header brute (find hidden auth bypass headers)",
             "ffuf -u 'https://example.com/admin' -H 'FUZZ: 127.0.0.1' \\\n"
             "  -w ~/wordlists/headers.txt -mc 200,302 -fc 403,404 -ac\n"
             "# headers.txt sample:\n"
             "# X-Forwarded-For\n# X-Real-IP\n# X-Originating-IP\n# X-Remote-IP\n# X-Remote-Addr\n# X-Client-IP\n# X-Host\n# X-Forwarded-Host\n# X-Original-URL\n# X-Rewrite-URL\n# X-Custom-IP-Authorization\n# X-Originating-IP\n# True-Client-IP\n# Cluster-Client-IP\n# CF-Connecting-IP"),
            ("Recursive feroxbuster (better than ffuf for deep recursion)",
             "feroxbuster -u https://$TARGET -w ~/wordlists/raft-large-directories.txt \\\n"
             "  -t 50 -d 5 --auto-tune --auto-bail \\\n"
             "  -x .json .bak .old .zip .git .env .yml \\\n"
             "  -C 404 -F 403 \\\n"
             "  -o ferox.txt"),
            ("Filter-Bypass content discovery (when 403 / 404 are wildcards)",
             "# Discover via response size variance\n"
             "ffuf -u 'https://example.com/FUZZ' -w big.txt -mc all -fs 0,1234   # exclude default 1234-byte 404\n"
             "# OR by response time\n"
             "ffuf -u 'https://example.com/FUZZ' -w big.txt -mc all -p 0.1 -of csv | awk '$N{print}'  # custom analysis"),
        ],
        "edge": [
            "**Wildcard responses** — every path returns 200 with the SPA shell. Use `-fs <size>` to filter, or `-fr <regex>` to filter response bodies. Or `-mc 200 -fl <line count>`.",
            "**Soft 404** — `200 OK` with body `Not Found`. Use `-fr 'Not Found'` or compare body MD5 against known 404.",
            "**Rate limit on big wordlist** — chunk wordlist + sleep between waves; rotate `-x` proxy list.",
            "**WAF false positives on payload-shaped wordlist entries** — neutral wordlists like `raft-large-directories` are fine; using SQLi/XSS payload lists for content discovery triggers WAF and gets you blocked.",
            "**GET vs POST diff** — `-X POST` reveals `/api/users` only handles POST; GET returns 405. Always run both.",
            "**JSON body fuzz** — for APIs, `-X POST -d '{\"FUZZ\":\"x\"}'` to find hidden keys.",
        ],
    },
    "16_recon_automation_pipeline.md": {
        "title": "Recon Automation Pipeline",
        "trigger": "scaling — running recon across N programs continuously",
        "what": "Stitch all recon stages into a single repeatable pipeline. Trigger on: program scope changes, new subdomain CT log entry, new GitHub commit. Notify via Telegram/Discord. Persist deltas in Git. Re-run every 6h.",
        "stack": """
## Reference architecture

```
                                       ┌──────────────────────────────┐
[CronJob 6h] ──► recon_pipeline.sh ──► │  artifacts/<target>/<date>/  │
       │                               │   subs.txt, alive.txt,        │
       │                               │   tech.json, urls.txt,        │
       │                               │   nuclei.json, secrets.json   │
       │                               └──────────────┬───────────────┘
       │                                              │
       │                                              ▼
       │                                       diff against last run
       │                                              │
       │                                              ▼
       └─► [scope-monitor] ──► program-scope.txt ──► diff_handler.py ──► Telegram bot
                                                                       └► Discord webhook
                                                                       └► commit deltas to Git
```

Use **[axiom](https://github.com/pry0cc/axiom)** for distributed scanning across cheap VPSes (DigitalOcean / Linode).
""",
        "commands": [
            ("Skeleton recon_pipeline.sh",
             """#!/usr/bin/env bash
set -euo pipefail
TARGET=$1
DATE=$(date +%Y%m%d-%H%M)
OUT=$HOME/hunting/$TARGET/$DATE
mkdir -p "$OUT" && cd "$OUT"

# 1. Passive subs
subfinder -d "$TARGET" -all -silent | tee subs_subfinder.txt
chaos-client -d "$TARGET" -silent | tee subs_chaos.txt
github-subdomains -d "$TARGET" -t "$GITHUB_TOKEN" -o subs_github.txt
cat subs_*.txt | sort -u > subs.txt

# 2. Permute + resolve
alterx -l subs.txt -enrich -silent > permutations.txt
puredns resolve permutations.txt -r ~/.config/resolvers.txt --wildcard-batch 1500000 -q > resolved.txt
cat subs.txt resolved.txt | sort -u > all_subs.txt

# 3. Probe
httpx -l all_subs.txt -threads 100 -timeout 7 -follow-redirects \\
      -status-code -title -tech-detect -ip -cdn -tls-grab -web-server \\
      -json -o httpx.jsonl
cat httpx.jsonl | jq -r .url > alive.txt

# 4. Crawl + URLs
katana -list alive.txt -d 3 -jc -kf all -silent -o crawl.txt
cat alive.txt | gau --threads 10 --subs > gau.txt
cat crawl.txt gau.txt | sort -u | uro > all_urls.txt

# 5. JS analysis
mkdir -p js
grep -E '\\.js(\\?|$)' all_urls.txt | sort -u > js_urls.txt
cat js_urls.txt | xargs -I{} -P 20 curl -sk --max-time 10 -o "js/$(echo {} | md5sum | cut -d' ' -f1).js" "{}"
trufflehog filesystem js --only-verified --json > js_secrets.json

# 6. Vuln scan
nuclei -l alive.txt -severity medium,high,critical -t ~/nuclei-templates/ -t ~/custom-templates/ -rl 100 -timeout 10 -silent -o nuclei.txt -json -store-resp -store-resp-dir nuclei_resp/

# 7. Diff vs last run
PREV=$(ls -1 ~/hunting/$TARGET/ | sort | grep -v "^$DATE" | tail -1)
if [ -n "$PREV" ]; then
    comm -23 <(sort all_subs.txt) <(sort ~/hunting/$TARGET/$PREV/all_subs.txt) > new_subs.txt
    comm -23 <(sort all_urls.txt) <(sort ~/hunting/$TARGET/$PREV/all_urls.txt) > new_urls.txt
fi

# 8. Notify
[ -s nuclei.txt ] && python3 ~/scripts/notify_tg.py --file nuclei.txt --title "[$TARGET] nuclei findings"
[ -s new_subs.txt ] && python3 ~/scripts/notify_tg.py --file new_subs.txt --title "[$TARGET] new subdomains"
"""),
            ("Cron entry",
             "# Run every 6 hours at 5 minutes past\n"
             "5 */6 * * * /home/ubuntu/scripts/recon_pipeline.sh example.com >> /var/log/recon-example.log 2>&1"),
            ("Telegram notifier (Python)",
             """import os, sys, requests, argparse
TOKEN = os.environ['TG_BOT_TOKEN']
CHAT  = os.environ['TG_CHAT_ID']
ap = argparse.ArgumentParser()
ap.add_argument('--file', required=True)
ap.add_argument('--title', required=True)
a = ap.parse_args()
text = open(a.file).read()[:3500]
requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',
              data={'chat_id': CHAT, 'text': f'*{a.title}*\\n```\\n{text}\\n```', 'parse_mode': 'Markdown'})
"""),
            ("Discord notifier",
             """import os, sys, requests
WH = os.environ['DISCORD_WEBHOOK']
title = sys.argv[1]; body = open(sys.argv[2]).read()[:1900]
requests.post(WH, json={'content': f'**{title}**\\n```\\n{body}\\n```'})
"""),
            ("certstream live-listener (new cert hit → trigger)",
             """import certstream, re, requests, os, json
TARGETS = open('~/hunting/targets.txt').read().splitlines()
def cb(msg, ctx):
    if msg['message_type'] != 'certificate_update': return
    for d in msg['data']['leaf_cert']['all_domains']:
        for t in TARGETS:
            if d.endswith(t):
                requests.post(os.environ['DISCORD_WEBHOOK'],
                              json={'content': f'NEW CERT: {d} (issuer: {msg[\"data\"][\"chain\"][0][\"subject\"][\"CN\"]})'})
                # trigger pipeline
                os.system(f'/home/ubuntu/scripts/recon_pipeline.sh {t} &')
certstream.listen_for_events(cb, url='wss://certstream.calidog.io')
"""),
            ("axiom — distributed across N VPSes",
             "axiom-init mybox && axiom-fleet hunt -i 5\n"
             "axiom-scan all_subs.txt -m httpx -p 80,443,8080,8443\n"
             "axiom-scan alive.txt -m nuclei -t ~/nuclei-templates/\n"
             "axiom-rm '*' -f"),
        ],
        "edge": [
            "**Token rotation** — gitdorker / GitHub API gets you to ~5K req/h per token; rotate 5+ to keep up.",
            "**Resolver poisoning** — public resolvers occasionally return wildcards / poisoned A records. Use a curated resolver list (trickest/resolvers).",
            "**False-positive flood from nuclei** — keep a `~/.nuclei-ignore.yaml` to silence templates that always alert (e.g. CSP misconfig info-level on every host).",
            "**Notify spam** — diff before notifying. Only ping when the delta has lines.",
            "**State drift** — pipeline writes to a dated dir; diff against `last`. Symlink `last → <newest>` after each run.",
            "**Self-DoS** — running this against your own production targets at high concurrency may breach program rate-limit clauses. Throttle.",
        ],
    },
}


TEMPLATE = """# SKILL: {title}
## Version: 1.0 | Domain: recon | Trigger: {trigger}

---

## IDENTITY IN THIS SKILL
{what}

---

## TOOLS
{tools_section}

## COMMANDS & WORKFLOWS
{commands_section}

{extras}

## EDGE CASES
{edge_section}

## OUTPUT FORMAT
```
{title_upper}({{target}}):
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
"""


def fmt_tools(tools):
    return "\n".join(f"- `{t}`" for t in tools)

def fmt_commands(cmds):
    out = []
    for desc, cmd in cmds:
        out.append(f"### {desc}\n```bash\n{cmd}\n```\n")
    return "\n".join(out)

def fmt_edge(edges):
    return "\n".join(f"- {e}" for e in edges)


for fname, data in FILES.items():
    extras = ""
    if "dorks" in data:
        extras += "\n## DORKS\n```\n" + data["dorks"].strip() + "\n```\n"
    if "dorks_by_category" in data:
        extras += "\n## DORK LIBRARY\n" + data["dorks_by_category"]
    if "queries_by_engine" in data:
        extras += "\n## QUERIES BY ENGINE\n" + data["queries_by_engine"]
    if "favicon_pivot" in data:
        extras += "\n" + data["favicon_pivot"]
    if "wordlists" in data:
        extras += "\n## WORDLISTS\n" + data["wordlists"]
    if "stack" in data:
        extras += "\n## STACK\n" + data["stack"]

    body = TEMPLATE.format(
        title=data["title"],
        trigger=data["trigger"],
        what=data["what"],
        tools_section=fmt_tools(data["tools"]) if "tools" in data else "(see commands)",
        commands_section=fmt_commands(data["commands"]),
        extras=extras,
        edge_section=fmt_edge(data["edge"]),
        title_upper=data["title"].upper().replace("/", "_").replace(" ", "_"),
    )
    (OUT / fname).write_text(body)
    print(f"wrote {fname} ({len(body)} chars)")

print(f"\nTotal recon files in {OUT}: {len(list(OUT.glob('*.md')))}")
