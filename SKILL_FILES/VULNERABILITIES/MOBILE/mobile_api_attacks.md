# SKILL: Mobile API Attacks
## Version: 1.0 | Domain: mobile

---

## IDENTITY
Mobile apps often use API endpoints not present in the web app, with weaker auth.

## METHODOLOGY
1. Proxy all traffic through Burp (bypass SSL pinning first).
2. Map every endpoint hit by the app.
3. Compare with web app endpoints — note mobile-only ones.
4. Test each for: missing auth, BOLA, mass assignment, version downgrade.
5. Test hardcoded API keys found in static analysis.

## COMMON FINDINGS
- Mobile-only endpoints without auth.
- API versioning: mobile uses v1, web uses v3 — v1 has no rate limit.
- Hardcoded admin API key in APK/IPA.
- Device registration endpoint accepting arbitrary device_id → push notification hijack.
- File upload endpoint with no content-type validation.

## REFERENCES
OWASP MASTG + API Security Top 10
