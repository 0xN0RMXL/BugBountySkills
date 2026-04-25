# SKILL: Android Dynamic Analysis
## Version: 1.0 | Domain: mobile

---

## TOOLS
- Frida (instrumentation)
- objection (Frida wrapper)
- Burp Suite (proxy)
- drozer (component analysis)
- magisk + trust-user-certs (system CA injection)
- logcat (runtime logging)

## METHODOLOGY
```bash
# Set up proxy
adb shell settings put global http_proxy 192.168.1.x:8080

# Bypass SSL pinning (Frida)
frida -U -f com.target.app -l ssl_pinning_bypass.js --no-pause

# objection SSL bypass + explore
objection -g com.target.app explore
# android sslpinning disable
# android clipboard monitor
# android keystore list

# Intercept all traffic in Burp — map every API endpoint

# drozer — test exported components
drozer console connect
run app.package.info -a com.target.app
run app.activity.info -a com.target.app -i
run app.provider.info -a com.target.app
run scanner.provider.injection -a com.target.app
run scanner.provider.traversal -a com.target.app

# logcat monitoring
adb logcat | grep -i "token\|password\|secret\|key\|auth"
```

## HIGH-VALUE FINDINGS
- API endpoints that don't exist in web app
- Hardcoded auth tokens in SharedPreferences
- Cleartext credentials in logcat
- Exported activities that skip auth screens
- ContentProvider SQL injection

## REFERENCES
OWASP MASTG — Dynamic Analysis
