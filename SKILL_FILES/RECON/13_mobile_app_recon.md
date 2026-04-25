# SKILL: Mobile App Recon (Android / iOS)
## Version: 1.0 | Domain: recon | Trigger: any program with a mobile app in scope; OR pivot from a web target's app

---

## IDENTITY IN THIS SKILL
Pull APK/IPA, decompile, scrape URLs/secrets/intent filters/deep links, identify backend API endpoints not exposed in the web app.

---

## TOOLS
- `apkmd / Raccoon — pull APK from Play Store URL`
- `ipa-extractor — pull IPA via Apple Configurator or AppDb / iMazing`
- `apkleaks — secret scanner`
- `jadx-gui / jadx-cli — decompile to Java`
- `apktool — smali + resources`
- `MobSF — full static + dynamic analysis (browser UI)`
- `androguard — Python lib for programmatic analysis`
- `frida + objection — dynamic instrumentation`
- `burp + magisk-trust-user-certs / Frida cert pin bypass`

## COMMANDS & WORKFLOWS
### Pull APK by package name
```bash
pip install raccoon-apkmd
apkmd download com.example.app -o example.apk
```

### Static URL + secret extraction
```bash
apkleaks -f example.apk -o apkleaks.txt
# Manual
apktool d -f example.apk -o ext/
rg -nIE 'https?://[a-zA-Z0-9./_?=&%-]+' ext/ | sort -u > urls_in_apk.txt
rg -nIE '(api[_-]?key|secret|token|password|jwt|firebase|aws_(access|secret)|sk_(live|test)_)["\'`:= ]' ext/ > secrets_in_apk.txt
```

### Find Firebase databases (often misconfig)
```bash
rg -oE '[a-z0-9-]+\.firebaseio\.com' ext/ | sort -u | while read fb; do
  curl -s "https://$fb/.json" | head -c 200
  echo " <- $fb"
done
```

### Dump intent filters + deep links + exported components (Android)
```bash
apktool d example.apk -o ext/
# AndroidManifest.xml — exported activities/services/providers
xmlstarlet sel -t -m '//activity[@android:exported="true"]' -v '@android:name' -n ext/AndroidManifest.xml
# OR drozer
drozer console connect
  # run app.activity.info -a com.example.app -i
  # run app.provider.info -a com.example.app
  # run scanner.provider.injection -a com.example.app
  # run scanner.provider.traversal -a com.example.app
```

### iOS — class-dump + frida
```bash
# Get IPA → dump classes
class-dump-z -H Example.ipa -o classes/
# Frida bypass cert pin (universal script)
frida -U -f com.example.app -l ios-cert-pin-bypass.js --no-pause
```

### MobSF full report
```bash
docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest
# Upload APK/IPA in browser at http://localhost:8000
```

### Capture mobile traffic in Burp
```bash
# Android: install Burp CA as system cert via magisk-trust-user-certs module
# Set proxy: WiFi → Modify Network → Proxy Manual → 192.168.x.y:8080
# For SSL pinning bypass:
frida -U -l ssl-pinning-bypass.js -f com.example.app --no-pause
# objection alternative
objection -g com.example.app explore
  # android sslpinning disable
  # ios sslpinning disable
```




## EDGE CASES
- **App-only API endpoints** — backend exposes `/api/v3/internal/...` only used by mobile, no auth on some routes assuming "only mobile clients hit this". Frequent finding.
- **Hardcoded API keys** — Firebase web API key (low risk by itself, but combined with Firestore rules misconfig = full DB read), Algolia search keys (admin vs search-only), Mapbox keys (often abused for DoS).
- **Insecure deep links** — `example://login?token=<attacker_token>` chains to ATO if app accepts arbitrary token.
- **Exported ContentProvider** — `content://com.example.app.provider/users` SQL injectable via `path` URI param.
- **WebView with `setJavaScriptEnabled(true)` + `addJavascriptInterface`** — any XSS in the loaded page = JS-to-native RCE.
- **Cleartext traffic flag** — `android:usesCleartextTraffic="true"` in manifest = data interception viable.

## OUTPUT FORMAT
```
MOBILE_APP_RECON_(ANDROID___IOS)({target}):
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
