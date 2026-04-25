# SKILL: Report Writing Methodology
## Version: 1.0 | Domain: reporting

---

## STRUCTURE — 5 sections, in this order
1. **Title** — `[Severity] [Bug class] in [endpoint] leading to [impact]`
2. **Summary** — 2-3 sentences. What, where, impact.
3. **Steps to reproduce** — numbered, copy-pasteable, ≤10 steps.
4. **Proof of Concept** — curl / HTML / video.
5. **Impact** — concrete, business-language.
6. **Remediation** — actionable, specific.

## TITLE EXAMPLES
- ✅ `[Critical] Stored XSS in /comments persists in admin dashboard, leading to admin ATO`
- ✅ `[High] IDOR on /api/v2/users/{id}/invoices allows reading invoices of any user`
- ❌ `XSS bug` (too vague)
- ❌ `Found IDOR` (no context)

## SUMMARY TEMPLATE
> The `/api/v2/users/{id}/invoices` endpoint does not enforce authorization and allows any authenticated user to read invoices belonging to any other user. This exposes PII (names, addresses, billing details) and financial data for all customers.

## STEPS — TEMPLATE
```
1. Log in as User A ([email protected]).
2. Capture the session cookie (`session=AAA...`).
3. Note that User A's user ID is `12345`.
4. Send the following request:

   curl -sk 'https://target.tld/api/v2/users/12346/invoices' \\
     -H 'Cookie: session=AAA...'

5. Observe that the response returns User B's invoices including PII.
```

## IMPACT — TEMPLATE
> A logged-in attacker can read every other customer's invoices including full name, mailing address, billing email, and total amount due. This affects all 4M+ customers (estimated from `/api/users/count`). This violates GDPR Art. 32 and PCI-DSS 7.x. There is no rate limit; an attacker can dump the entire user base in <1 hour.

## REMEDIATION
- Be specific: "Add `req.user.id == params.id` check in `routes/invoices.js:42`" instead of "Add proper authorization checks".

## TONE
- Professional, neutral, no hype.
- No insults to dev team / triage.
- Technical clarity > literary flair.

## REFERENCES
HackerOne report writing guide, Bugcrowd VRT
