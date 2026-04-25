# JWT — alg:none

## 📌 What It Is
JWT library accepts `alg: none` header, allowing token forgery without secret.

## 🔍 How to Find It
Decode the JWT. If the server parses `alg` from the header dynamically → vulnerable.

## 🧪 How to Test It
Forge a token with `alg:none` header, modify payload, drop signature.

## 💣 How to Exploit It
Modify `sub`/`role` in payload → submit forged token → access admin.

## 🔄 Bypass Techniques
Case variants: `none`, `None`, `NONE`, `nOnE`, `none ` (trailing space).

## 🛠️ Tools
- jwt_tool, jwt.io, custom Python with PyJWT

## 🎯 Payloads
```\neyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJhZG1pbiJ9.\n```

## 📝 Real-World Examples
Auth0 advisory 2015, multiple H1 reports.

## 🚩 Common Mistakes / Traps
Don't forget to remove signature entirely (or include trailing dot).

## 📊 Severity & Impact
Critical (CVSS 9.8) when full ATO.

## 🔗 References
PortSwigger JWT labs, jwt_tool wiki.

## ⚡ One-Liners
```bash\npython3 -c "import jwt; print(jwt.encode({'sub':'admin'}, key='', algorithm='none'))"\n```
