# HTTP Request Smuggling (CL.TE)

## 📌 What It Is
Frontend uses Content-Length, backend uses Transfer-Encoding (or vice versa). Misalignment lets an attacker prepend a request to the next user's connection.

## 🔍 How to Find It
Probe with timing differential: send `Transfer-Encoding: chunked` + body that ends early — if response delays, backend used TE. Alternatively send `Content-Length: 4`, body `1\r\n...`. Use HTTP Request Smuggler ext (Burp).

## 🧪 How to Test It
1. Send probe (CL.TE or TE.CL) → measure timing.\n2. If delay >5s → confirmed.\n3. Test for cross-user impact: prepend request that affects next request on connection.

## 💣 How to Exploit It
Smuggled request → admin endpoint → cache poisoning → ATO. Bypass auth via internal headers (X-Forwarded-User: admin) injected by smuggling.

## 🔄 Bypass Techniques
- Use TE: chunked\nfoo\nbar (variant TE values, like `Transfer-Encoding: \tchunked`, `Transfer-Encoding: chunked\r\nTransfer-Encoding: identity`)\n- HTTP/2 → H1 downgrade smuggling\n- HTTP/2 CRLF in pseudo-headers

## 🛠️ Tools
- Burp HTTP Request Smuggler\n- smuggler.py (defparam)\n- nuclei smuggling templates

## 🎯 Payloads
```\nPOST / HTTP/1.1\nHost: target\nContent-Length: 4\nTransfer-Encoding: chunked\n\n1\nA\nQ\n```

## 📝 Real-World Examples
PortSwigger James Kettle research; CVE-2019-XXX (CDN smuggling).

## 🚩 Common Mistakes / Traps
Don't rely on intermittent delays; confirm with cross-user smuggle. Don't smuggle destructive requests in production.

## 📊 Severity & Impact
Critical (CVSS 9.0+) when admin compromise possible.

## 🔗 References
PortSwigger HTTP Request Smuggling, James Kettle DEF CON 27 talk.

## ⚡ One-Liners
```bash\necho 'https://target' | nuclei -t ~/nuclei-templates/http/smuggling/\n```
