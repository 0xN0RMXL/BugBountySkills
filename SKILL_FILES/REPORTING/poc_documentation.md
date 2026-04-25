# SKILL: PoC Documentation
## Version: 1.0 | Domain: reporting

---

## CHECKLIST FOR EVERY PoC
- [ ] Single, minimal payload — no debug noise, no dead params
- [ ] All required headers / cookies (with sensitive parts redacted)
- [ ] Expected response excerpt (200/302/error message)
- [ ] Screenshot or video of trigger
- [ ] Statement of testing context (auth state, role, browser)
- [ ] Time/date of test (helps if patched between submission and triage)

## CURL TEMPLATE
```bash
# REQ
curl -sk 'https://target.tld/api/v2/users/12346/invoices' \
  -H 'Cookie: session=<REDACTED>' \
  -H 'User-Agent: Mozilla/5.0' \
  -i

# EXPECTED RESPONSE (excerpt)
HTTP/2 200
content-type: application/json

[{"id":1,"amount":42.00,"customer":"John Doe","email":"...","address":"..."}]
```

## HTML PoC TEMPLATE
```html
<!DOCTYPE html>
<html><head><title>PoC</title></head><body>
<h2>PoC — [Bug class] at [endpoint]</h2>
<form id=f action='https://target.tld/api/x' method='POST' enctype='text/plain'>
  <input name='{"email":"[email protected]","x":"' value='"}'>
</form>
<script>document.getElementById('f').submit()</script>
</body></html>
```

## VIDEO PoC GUIDELINES
- Resolution ≥ 1080p
- ≤ 60 seconds
- Show: scope page → tool/browser → trigger → result
- Narrate or use captions explaining each step
- Tool: OBS Studio (free, cross-platform), Loom (cloud, easy), asciinema (terminal)

## REDACTION
- Blur tokens, keys, PII, customer names
- Use `[REDACTED]` text marker

## REFERENCES
HackerOne / Bugcrowd reporting guidelines
