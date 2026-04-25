# Subdomain Takeover — S3

## 📌 What It Is
DNS CNAME pointing to a non-existent S3 bucket. Attacker registers the bucket and serves arbitrary content on the subdomain.

## 🔍 How to Find It
Enumerate subdomains. Check for CNAME → `*.s3.amazonaws.com`. If bucket returns NoSuchBucket → claimable.

## 🧪 How to Test It
1. `dig CNAME forgotten.target.tld` → `forgotten.target-bucket.s3.amazonaws.com`\n2. `curl https://forgotten.target.tld` → S3 NoSuchBucket error\n3. `aws s3 mb s3://forgotten.target-bucket --region us-east-1` → claim.

## 💣 How to Exploit It
Serve attacker HTML/JS on subdomain → cookies scoped to `*.target.tld` are exfiltrated. ATO.

## 🔄 Bypass Techniques
Region matters — try other regions if first fails. Some S3 names already taken — try with -1, -2 suffix.

## 🛠️ Tools
- subzy, nuclei takeovers, can-i-take-over-xyz repo

## 🎯 Payloads
Direct registration, no payload.

## 📝 Real-World Examples
Microsoft, GitHub, Heroku, Shopify takeovers.

## 🚩 Common Mistakes / Traps
Don't host malicious content; just put a benign placeholder + report.

## 📊 Severity & Impact
High to Critical (cookie scope = ATO).

## 🔗 References
github.com/EdOverflow/can-i-take-over-xyz, Detectify research.

## ⚡ One-Liners
```bash\nsubzy run --targets subs.txt --hide_fails --concurrency 100\n```
