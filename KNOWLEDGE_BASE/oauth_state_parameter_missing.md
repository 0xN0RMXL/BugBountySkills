# OAuth — state parameter missing

## 📌 What It Is
Authorization server doesn't validate `state`, enabling CSRF on the OAuth flow → forced linking attacker's social account to victim's.

## 🔍 How to Find It
Initiate flow without state param. If completion succeeds → not validated.

## 🧪 How to Test It
1. Attacker initiates OAuth flow on target as themselves\n2. Captures `?code=...` callback URL\n3. Sends victim crafted callback URL\n4. Victim is now linked to attacker's social account → attacker logs in as victim.

## 💣 How to Exploit It
ATO via login-with-google: victim's account now controlled by attacker's google account.

## 🔄 Bypass Techniques
If state validated only at endpoint level — try removing entirely. If random — bind to session check.

## 🛠️ Tools
- Burp manual\n- Nuclei OAuth misconfig

## 🎯 Payloads
Capture callback URL, send to victim.

## 📝 Real-World Examples
GitHub, Slack, multiple H1 reports.

## 🚩 Common Mistakes / Traps
Don't confuse with redirect_uri abuse — different control.

## 📊 Severity & Impact
High (CVSS 7-8).

## 🔗 References
RFC 6749 §10.12, Daniel Fett OAuth research.

## ⚡ One-Liners
```\nGET /oauth/callback?code=ATTACKER_CODE\n```
