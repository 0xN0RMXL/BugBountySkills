# SKILL: JavaScript Analysis
## Version: 1.0 | Domain: recon | Trigger: any web target has bundled JS; especially SPAs and admin panels

---

## IDENTITY IN THIS SKILL
Frontend JavaScript leaks endpoints, parameters, secrets, business logic, role enums, hidden routes, internal API hosts, analytics keys, and (occasionally) full backend code via sourcemaps.

---

## TOOLS
- `katana / hakrawler / gospider: crawl + extract JS`
- `subjs: extract JS URLs from a domain`
- `linkfinder / jsluice / mantra / jsleak: extract endpoints + secrets from JS`
- `secretfinder: regex-based secret scan`
- `GAP (Burp ext): parameter mining from JS`
- `JS Miner (Burp ext): inline secret + endpoint mining`
- `trufflehog filesystem: regex / verifier secret scan over downloaded JS`
- `sourcemapper / unwebpack-sourcemap: pull source from .js.map`
- `uglify-restore / prettier --parser babel: deobfuscate`

## COMMANDS & WORKFLOWS
### Crawl + collect all JS files from target
```bash
katana -list alive.txt -d 5 -jc -kf all -aff -o crawl.txt
cat crawl.txt | grep -E '\.js(\?|$)' | sort -u > js_urls.txt
# add gau / waybackurls historical JS
cat alive.txt | gau --subs --threads 10 | grep -E '\.js(\?|$)' >> js_urls.txt
sort -u js_urls.txt -o js_urls.txt
```

### Download all JS for offline analysis
```bash
mkdir -p js && cd js && cat ../js_urls.txt | xargs -I{} -P 20 curl -sk --max-time 15 -o "$(echo {} | md5sum | cut -d' ' -f1).js" "{}"
```

### Extract endpoints from JS
```bash
for f in js/*.js; do
  python3 ~/tools/LinkFinder/linkfinder.py -i "$f" -o cli
done | sort -u > endpoints_from_js.txt
# OR jsluice (Tom Hudson) — best in 2024
find js/ -name '*.js' | xargs -I{} jsluice urls -m '*' {} | sort -u >> endpoints_from_js.txt
find js/ -name '*.js' | xargs -I{} jsluice secrets {} > js_secrets.txt
```

### Secret scanning on downloaded JS
```bash
trufflehog filesystem --json js/ > js_truffle.json
secretfinder -i js/ -o cli > js_secretfinder.txt
# Custom regex sweep for things truffle misses
rg -i 'aws_secret|aws_access|stripe_(test|live)|sk_live_|sk_test_|xoxb-|xoxp-|xapp-|pk_live_|pk_test_|api[_-]?key|client[_-]?secret|firebase|sendgrid|twilio|mailgun|github_token|ghp_|ghu_|ghs_|jwt|bearer\s+[a-z0-9]+|password\s*[:=]\s*["\']' js/
```

### Sourcemap recovery (gold mine)
```bash
for u in $(cat js_urls.txt); do
  curl -sk --max-time 10 "$u.map" -o /tmp/x.map && [ -s /tmp/x.map ] && echo "FOUND .map: $u.map"
done
# Then unpack:
npx sourcemap-explorer file.js.map
# OR
git clone https://github.com/denandz/sourcemapper && go run sourcemapper.go -url "https://example.com/main.js.map" -output recovered/
```

### DOM XSS sink hunting in client JS
```bash
rg -n 'document\.write|innerHTML\s*=|outerHTML\s*=|insertAdjacentHTML|\.html\(|eval\(|setTimeout\(["\']\\$|setInterval\(["\']|Function\(|setAttribute\((?:["\'](?:on|src|href))|location\s*=|location\.href|location\.replace|location\.assign|window\.open|postMessage' js/
```

### postMessage handlers (great for XSS / DOM clobbering chains)
```bash
rg -n 'addEventListener\(["\']message["\']' js/ -A 10
```

### Webpack bundle deobfuscation (when source maps unavailable)
```bash
# Unminify visually
find js/ -name '*.js' -size +50k -exec js-beautify -o {}.pretty {} \;
# Try debowerify / unwebpack
npx unminify js/main.js > main.unminified.js
```




## EDGE CASES
- **Lazy-loaded chunks** — main bundle dynamically imports `/static/js/chunk-*.js`. Crawl + the manifest in `runtime.*.js` gives you the chunk graph.
- **Source maps in prod** — devs forget to strip them. Always check for `//# sourceMappingURL=` at the bottom of every JS file.
- **Service workers** — `sw.js` often caches API URLs and lists endpoints not used in the visible app.
- **`window.__INITIAL_STATE__`** — Server-rendered SPAs leak full user objects, role lists, feature flags. Grep page source for `__INITIAL_STATE__`, `__APOLLO_STATE__`, `__NEXT_DATA__`, `__NUXT__`.
- **Internal API hostnames** — leaked in client JS as fallback URLs. `https://api-internal.corp.example.com` not in your subdomain list = recon win.

## OUTPUT FORMAT
```
JAVASCRIPT_ANALYSIS({target}):
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
