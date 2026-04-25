# SKILL: HackerOne Report Template
## Version: 1.0 | Domain: reporting

---

## TITLE FIELD
`[Bug class] in [endpoint] leading to [impact]`

## SUMMARY (top of report body)
2-3 lines describing the bug + impact. Triagers read this first.

## STEPS TO REPRODUCE
```
1. ...
2. ...
3. ...
```

## SUPPORTING MATERIAL/REFERENCES
- HTTP request/response (use HackerOne's code-fence with HTTP syntax)
- Screenshots (drag/drop into editor)
- Video (max 50MB; or external link to Loom/Vimeo unlisted)

## IMPACT
Concrete, quantified, with regulatory citation if applicable.

## SEVERITY
Use the H1 severity selector. CVSS calculator is built in. Use both Severity + Weakness fields.

## ASSET FIELDS
Pick the asset (e.g., `*.target.com`) — this matters for triage routing.

## H1-SPECIFIC TIPS
- Reference Hacktivity precedent for similar bugs ("see #123456 — same class, accepted as $X")
- Don't include 0-day in reports of any external issues unless explicitly requested
- For private programs — do not leak company name in public PoC URLs
- For SLA targets — note program SLA (Triage / Bounty / Resolution)
- Tag relevant CWE
- Use `h1-XXX` private link only for private engagement
- Confidential weakness toggle for sensitive data in body

## H1 TRIAGER NUDGES
- Triagers reject "self-XSS" — show cross-user impact.
- Triagers reject "no impact" SSRF — show metadata or internal service.
- Triagers reject "best-practice" CSP — show actual XSS.
- Provide impact bullets so triager can copy them when retriaging.

## REFERENCES
hackerone.com/disclosure-guidelines, HackerOne hacktivity
