# SKILL: iOS Static Analysis
## Version: 1.0 | Domain: mobile

---

## TOOLS
- class-dump / class-dump-z — dump ObjC headers
- Hopper / IDA / Ghidra — binary disassembly
- MobSF — automated analysis
- plutil — plist parsing

## METHODOLOGY
```bash
# Extract IPA (rename .ipa → .zip)
unzip app.ipa -d ipa_out/

# Info.plist — URL schemes, permissions, ATS config
plutil -p ipa_out/Payload/App.app/Info.plist

# Check App Transport Security (ATS) exceptions
# NSAppTransportSecurity → NSAllowsArbitraryLoads = true → cleartext allowed

# Extract strings
strings ipa_out/Payload/App.app/App | grep -i "api\|key\|secret\|token\|password\|http://"

# class-dump
class-dump-z -H ipa_out/Payload/App.app/App -o classes/
grep -rn "password\|secret\|token" classes/

# Check for embedded frameworks with known CVEs
ls ipa_out/Payload/App.app/Frameworks/
```

## REFERENCES
OWASP MASTG — iOS Static Analysis
