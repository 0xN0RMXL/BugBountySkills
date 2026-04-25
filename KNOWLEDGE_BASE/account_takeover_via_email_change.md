# Account Takeover via Email Change

## 📌 What It Is
Email change endpoint vulnerable to CSRF or IDOR. Attacker changes victim's email → password reset → ATO.

## 🔍 How to Find It
Find email-change endpoint. Test for: CSRF, IDOR (change other user's email), missing re-auth, missing confirmation.

## 🧪 How to Test It
1. CSRF: craft auto-submit form to `/api/email/change?email=attacker`\n2. IDOR: PUT `/api/users/<victim>/email`\n3. No confirmation: change goes through immediately without verification email.

## 💣 How to Exploit It
→ trigger password reset → reset link to attacker email → ATO.

## 🔄 Bypass Techniques
If confirmation required — race the confirmation. Or chain XSS to autosubmit. Or use Open Redirect to leak confirmation token.

## 🛠️ Tools
- Burp Repeater\n- Custom Python script

## 🎯 Payloads
Auto-submit form (see PAYLOADS/csrf_payloads.md).

## 📝 Real-World Examples
Multiple H1 P1 reports — Shopify, Twitter, etc.

## 🚩 Common Mistakes / Traps
Trickiest variant: email change requires current password — but if change happens via OAuth-linked account that doesn't require password, bypass.

## 📊 Severity & Impact
Critical (CVSS 9.x).

## 🔗 References
OWASP ATO cheat sheet.

## ⚡ One-Liners
```bash\ncurl -X POST 'https://target/api/email/change' -H 'Cookie: ...' -d '[email protected]'\n```
