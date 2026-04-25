# Web Cache Deception

## 📌 What It Is
Serving private (authenticated) content from a CDN cache that thinks the URL is static. Attacker tricks user into requesting URL like `/account/myinfo.css`; cache stores response as static .css; attacker fetches same URL anonymously.

## 🔍 How to Find It
Look for path-based cache. Test by requesting `/account.css` (or similar variation). If 200 with sensitive data → cached.

## 🧪 How to Test It
1. Logged in, GET `/account/myinfo`\n2. Logged in, GET `/account/myinfo.css` → if returns same private content → cacheable\n3. Open incognito, GET `/account/myinfo.css` → if returns first user's data → confirmed.

## 💣 How to Exploit It
1. Send victim crafted link `/profile/me.css?victim=user`\n2. Cache stores victim's profile\n3. Attacker fetches same URL → reads victim profile.

## 🔄 Bypass Techniques
Test: .css, .js, .jpg, .png, .ico, .pdf, .woff, .map, .json (cache rules vary). Test trailing slash. Test path traversal `/account/me/../style.css`.

## 🛠️ Tools
- Burp Param Miner\n- Nuclei cache deception template

## 🎯 Payloads
```\nGET /account/myprofile/x.css HTTP/1.1\n```

## 📝 Real-World Examples
Omer Gil's original disclosure (PayPal). Acquia, BunnyCDN, Cloudflare cases.

## 🚩 Common Mistakes / Traps
Don't confuse with cache poisoning. Don't test destructively (destruct cached entries).

## 📊 Severity & Impact
High (CVSS 7-8) for PII leak; Critical for tokens.

## 🔗 References
Omer Gil DEF CON, PortSwigger labs.

## ⚡ One-Liners
```bash\nfor ext in css js jpg png; do curl -sI "https://target/account/x.$ext" | grep -i 'x-cache\|cf-cache\|age:'; done\n```
