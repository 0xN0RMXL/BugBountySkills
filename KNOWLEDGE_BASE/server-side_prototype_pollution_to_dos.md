# Server-Side Prototype Pollution → DoS

## 📌 What It Is
Pollute Node global object with malformed value → crashes downstream operations across all users.

## 🔍 How to Find It
Find PP sink. Pollute with `{__proto__:{toString:null}}`.

## 🧪 How to Test It
Subsequent JSON.stringify or template render crashes server.

## 💣 How to Exploit It
Server crash = DoS for all users until restart.

## 🔄 Bypass Techniques
If server isolates per-request — only requests within same Node process affected.

## 🛠️ Tools
- ppfuzz, custom Burp matchers

## 🎯 Payloads
```json\n{"__proto__":{"toString":null}}\n```

## 📝 Real-World Examples
Multiple npm package CVEs.

## 🚩 Common Mistakes / Traps
Don't run on production — actually crashes the server. Use staging.

## 📊 Severity & Impact
Medium-High (DoS).

## 🔗 References
PortSwigger PP, Snyk advisories.

## ⚡ One-Liners
```bash\ncurl -X POST -d '{"__proto__":{"toString":null}}' -H 'Content-Type: application/json' https://target/api/x\n```
