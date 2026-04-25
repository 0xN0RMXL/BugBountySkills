# SKILL: iOS Dynamic Analysis
## Version: 1.0 | Domain: mobile

---

## TOOLS
- Frida (jailbroken device)
- objection
- Burp + SSL Kill Switch 2
- Cycript (runtime manipulation)
- lldb (debugger)

## METHODOLOGY
```bash
# SSL pinning bypass
frida -U -f com.target.app -l ios-ssl-bypass.js --no-pause

# objection
objection -g com.target.app explore
# ios sslpinning disable
# ios cookies get
# ios keychain dump
# ios pboard monitor

# Keychain dump (gold — often contains auth tokens)
objection -g com.target.app explore --startup-command "ios keychain dump"

# Runtime class manipulation
frida -U -f com.target.app -l <<'JS'
var cls = ObjC.classes.AuthManager;
Interceptor.attach(cls['- isAuthenticated'].implementation, {
  onLeave: function(retval) { retval.replace(ptr(1)); }
});
JS
```

## HIGH-VALUE FINDINGS
- Auth tokens in Keychain accessible to other apps (wrong kSecAttrAccessGroup)
- Biometric bypass via Frida hook
- Cleartext PII in NSUserDefaults

## REFERENCES
OWASP MASTG — iOS Dynamic Analysis
