# SKILL: Certificate Pinning Bypass
## Version: 1.0 | Domain: mobile

---

## ANDROID
```bash
# Method 1: Frida (universal)
frida -U -f com.target.app --codeshare pcipolloni/universal-android-ssl-pinning-bypass-with-frida --no-pause

# Method 2: objection
objection -g com.target.app explore
android sslpinning disable

# Method 3: Magisk module (permanent for device)
# Install "Move Certificates" or "trust-user-certs" magisk module
# Then Burp CA is system-trusted

# Method 4: apktool + patch
# Decompile → modify network_security_config.xml → rebuild → sign
apktool d app.apk -o patched/
# Edit patched/res/xml/network_security_config.xml:
# <trust-anchors><certificates src="user" /></trust-anchors>
apktool b patched/ -o patched.apk
jarsigner -keystore my.keystore patched.apk alias
```

## iOS
```bash
# Method 1: Frida
frida -U -f com.target.app -l ios-ssl-pinning-bypass.js --no-pause

# Method 2: SSL Kill Switch 2 (Cydia tweak, jailbroken)

# Method 3: objection
objection -g com.target.app explore
ios sslpinning disable
```

## EDGE CASES
- **OkHttp CertificatePinner** — Frida script must hook `okhttp3.CertificatePinner.check$okhttp`.
- **TrustManager** — custom TrustManagerFactory — hook `checkServerTrusted`.
- **Flutter apps** — pinning compiled into native code; use `reFlutter` tool to patch.

## REFERENCES
OWASP MASTG — Network Communication Testing
