# Cache Poisoning via Header

## 📌 What It Is
CDN/cache stores response keyed on URL only; an unkeyed header (X-Forwarded-Host, X-Original-URL, etc.) influences response. Attacker poisons cache for all users.

## 🔍 How to Find It
Probe with Param Miner: send unique `X-Forwarded-Host: attacker.tld` header → see if reflected in cached response.

## 🧪 How to Test It
1. Find unkeyed header that influences output\n2. Inject XSS / redirect via that header\n3. Wait for cache to serve next user

## 💣 How to Exploit It
Mass XSS to all visitors. Mass redirect. Persistent injection of attacker JS.

## 🔄 Bypass Techniques
If header sanitized — try variations: `X-Original-URL`, `X-Forwarded-Scheme`, `X-Host`, `Forwarded`, `X-Forwarded-Proto`.

## 🛠️ Tools
- Burp Param Miner\n- web-cache-poisoning research

## 🎯 Payloads
```\nGET /home HTTP/1.1\nHost: target.tld\nX-Forwarded-Host: attacker.tld\n```

## 📝 Real-World Examples
James Kettle's 2018-2020 cache poisoning research.

## 🚩 Common Mistakes / Traps
Don't poison production; use unique cache buster `?cb=<random>` to test.

## 📊 Severity & Impact
Critical for stored XSS via cache.

## 🔗 References
PortSwigger cache poisoning labs.

## ⚡ One-Liners
```bash\ncurl -H 'X-Forwarded-Host: evil.tld' 'https://target/'\n```
