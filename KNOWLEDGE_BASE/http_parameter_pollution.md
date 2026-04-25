# HTTP Parameter Pollution

## 📌 What It Is
Multiple parameters with same name handled differently by frontend vs backend (or different backends). Last-wins, first-wins, concat — divergence enables filter bypass.

## 🔍 How to Find It
Test: `?id=1&id=2`. Observe which value the server uses.

## 🧪 How to Test It
1. Map parser behavior per endpoint.\n2. If WAF processes first occurrence and backend processes last → smuggle malicious value as second.\n3. Bypass authorization checks: `?role=user&role=admin`.

## 💣 How to Exploit It
Bypass WAF by hiding payload in second occurrence. Bypass auth by overriding role.

## 🔄 Bypass Techniques
Path/method inconsistencies. JSON arrays handled as scalars in some parsers.

## 🛠️ Tools
- Burp manual + Param Miner

## 🎯 Payloads
```\n?id=1&id=' OR 1=1-- -\n?role=user&role=admin\n```

## 📝 Real-World Examples
OWASP HPP cheat sheet, real-world WAF bypasses (Akamai, Cloudflare).

## 🚩 Common Mistakes / Traps
Don't assume HPP works — test each parser. Some normalize early.

## 📊 Severity & Impact
Variable, depends on chained impact.

## 🔗 References
OWASP HPP, Sec-1 HPP research.

## ⚡ One-Liners
```bash\ncurl 'https://target/?id=1&id=2'\n```
