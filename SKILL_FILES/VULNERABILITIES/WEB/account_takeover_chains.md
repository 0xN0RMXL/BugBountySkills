# SKILL: Account Takeover (ATO) Chains

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (account takeover (ato) chains) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
ATO is the impact, not the bug. I chain XSS / IDOR / OAuth / 2FA / password reset / email change / session fixation into ATO.

---

## DETECTION
(map every modify-account endpoint and chain)

## EXPLOITATION
### Email change → password reset
1. XSS / CSRF → POST /api/email/change `attacker@tld`.
2. Forgot password → reset link to attacker@tld.
3. Login as victim.

### Password reset token in email subject (URL leak via Referer)
1. Find external img link in reset email page.
2. Token leaks via Referer to attacker domain.

### OAuth account merge squatting
1. Pre-create account using `victim@target.com` via Google sign-in (no email verification).
2. Victim later signs up with same email → accounts merged.

### 2FA bypass + password reset
1. Bypass 2FA (see 2fa_mfa_bypass.md).
2. Use password reset.

### Session fixation
1. Force victim to use attacker's session ID (CSRF login).
2. Attacker has same session.

### Cookie scope abuse
1. Subdomain takeover or XSS on related sub gives access to parent-domain cookies.

### Cross-account bleed via 'reset by phone'
1. Change phone number to attacker's via missing-MFA endpoint.
2. SMS OTP reset.

## PAYLOADS (real, copy-paste, grouped)
(behavior chains)

## BYPASS TECHNIQUES
(see component skills)

## CHAIN POTENTIAL
End → ATO.

## TOOLS
Burp Repeater + state diagram

## COMMANDS
Manual

## EDGE CASES / NOT-A-BUG TRAPS
Triagers want literal account ATO PoC: log in as victim, see their data.

## TRIAGE ANGLE (per platform)
Show login dashboard of victim, with timestamp matching exploit.

## SEVERITY & CVSS
9.0+.

## REFERENCES
bb_kb/Account_Takeover/
