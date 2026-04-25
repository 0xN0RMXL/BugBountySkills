# SKILL: 2FA / MFA Bypass

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (2fa / mfa bypass) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
MFA layers fail in many places: missing on critical endpoints, brute-able codes, race conditions, response manipulation, code reuse, fallback weakness.

---

## DETECTION
Map every authenticated endpoint after MFA. Strip MFA cookie/header — does sensitive action still succeed?

## EXPLOITATION
1. **MFA missing on sensitive endpoints** — `/api/email/change`, `/api/2fa/disable`, `/api/password/change` reachable with auth-only cookie pre-MFA.
2. **Brute-force code** — no rate-limit on `/api/2fa/verify`. 6-digit = 10⁶; race: 100 req/sec finishes in 167min (often in scope).
3. **Response manipulation** — change `{"verified":false}` → `{"verified":true}` in response (only works if client trusts JSON, which is a bug class itself).
4. **Status code swap** — 401 → 200; client redirects on 200 only.
5. **Multiple session token reuse** — verify with one token, but the pre-MFA token still grants full access.
6. **Code reuse** — same code valid across multiple verify calls.
7. **Race condition** — submit verify + sensitive action in parallel; pre-MFA token may complete the action before MFA check.
8. **Backup code list** — predictable backup codes; or admin-resettable.
9. **SMS fallback** — request OTP via SMS to attacker number after a phone-number-change endpoint that itself is MFA-not-required.
10. **OAuth bypass** — sign in via Google account that already verifies email; 2FA enforcement may not apply to OAuth path.

## PAYLOADS (real, copy-paste, grouped)
(behavior-based — see above)

## BYPASS TECHNIQUES
- Send `code: ''` (empty) — sometimes parses as bypass.
- Send `code: null` (json) — same.
- Send `code: [1,2,3]` (array) — type confusion in some frameworks.
- Send the OTP twice to verify and to reset endpoints simultaneously.
- Replace `code` with `code[]=` array.

## CHAIN POTENTIAL
MFA bypass → ATO; or MFA bypass → admin → tenant takeover.

## TOOLS
Turbo Intruder for race conditions; Burp Repeater; intruder for code brute.

## COMMANDS
```python
# Turbo Intruder template for code brute
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=20)
    for i in range(0, 1000000):
        engine.queue(target.req, str(i).zfill(6))
def handleResponse(req, interesting):
    if 'success' in req.response or req.status == 200:
        table.add(req)
```

## EDGE CASES / NOT-A-BUG TRAPS
Some 2FA failures simply set a session flag — need to chain with another request to manifest.

## TRIAGE ANGLE (per platform)
Show end-to-end ATO without OTP knowledge.

## SEVERITY & CVSS
8.5–9.5.

## REFERENCES
2FA Bypass.pdf (uploaded) • HackTricks 2FA bypass • bb_kb/Account_Takeover/
