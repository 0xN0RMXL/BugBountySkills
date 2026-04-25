# SKILL: Android Static Analysis
## Version: 1.0 | Domain: mobile

---

## TOOLS
- jadx-gui / jadx-cli — Java decompilation
- apktool — smali + resources (AndroidManifest)
- MobSF — automated full report
- APKiD — packer/protector detection
- androguard — Python scripting

## METHODOLOGY
```bash
# Decompile
apktool d -f app.apk -o apk_out/
jadx -d java_out/ app.apk

# Key files to review
cat apk_out/AndroidManifest.xml   # exported components, permissions, intents
grep -rn "http://" java_out/       # cleartext traffic
grep -rn "api_key\|secret\|password\|token" java_out/
grep -rn "firebase\|aws_secret\|client_secret" java_out/

# Find exported components
xmlstarlet sel -t -m '//activity[@android:exported="true"]' -v '@android:name' -n apk_out/AndroidManifest.xml
xmlstarlet sel -t -m '//provider[@android:exported="true"]' -v '@android:name' -n apk_out/AndroidManifest.xml
xmlstarlet sel -t -m '//receiver[@android:exported="true"]' -v '@android:name' -n apk_out/AndroidManifest.xml

# Check for debug/backup flags
grep 'debuggable\|allowBackup\|usesCleartextTraffic' apk_out/AndroidManifest.xml

# APKLeaks — automated secret scan
apkleaks -f app.apk -o apkleaks.txt

# MobSF
docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest
# Upload APK via browser
```

## HIGH-VALUE TARGETS
- Hardcoded Firebase DB URLs → `curl https://xxx.firebaseio.com/.json`
- AWS keys (AKIA...) → `aws sts get-caller-identity`
- Google Maps API keys → test for billing abuse
- Algolia admin keys vs search-only keys
- Internal API endpoints not in web app

## REFERENCES
OWASP MASTG — Static Analysis
