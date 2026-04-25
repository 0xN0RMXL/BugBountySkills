# Mass Assignment — JSON

## 📌 What It Is
API endpoint binds request body to model directly without field allow-list. Attacker adds extra field (`isAdmin`, `verified`, `balance`) and gets it persisted.

## 🔍 How to Find It
Look for PUT/POST/PATCH endpoints that update objects. Inspect response when fetching the same object — note all fields.

## 🧪 How to Test It
1. Submit normal request body\n2. Add extra fields: `isAdmin`, `role:admin`, `verified:true`, `balance:99999`\n3. Refetch object → check if persisted.

## 💣 How to Exploit It
User → admin role. Free tier → paid tier. Verified status, etc.

## 🔄 Bypass Techniques
If `isAdmin` filtered → try `is_admin`, `admin`, `roles[]`. If at JSON top level filtered → try nested `{user:{isAdmin:true}}`.

## 🛠️ Tools
- Burp Param Miner\n- ParamSpider\n- Custom mass-assign fuzzer

## 🎯 Payloads
```json\n{"name":"foo","email":"a@b","isAdmin":true,"role":"admin","balance":999999}\n```

## 📝 Real-World Examples
GitHub Rails 2012 (`is_admin`), Bitcoin exchange ATO.

## 🚩 Common Mistakes / Traps
Don't confuse with prototype pollution. Make sure the field actually persists (refetch after).

## 📊 Severity & Impact
Critical when admin escalation; High for free→paid.

## 🔗 References
OWASP Mass Assignment cheat sheet.

## ⚡ One-Liners
```bash\ncurl -X PUT https://target/api/me -d '{"name":"a","isAdmin":true}' -H 'Content-Type: application/json'\n```
