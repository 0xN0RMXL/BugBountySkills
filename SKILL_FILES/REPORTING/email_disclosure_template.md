# SKILL: Email Disclosure Template
## Version: 1.0 | Domain: reporting

---

For programs without a platform (security@target.tld, security.txt).

## SUBJECT
`[Security] [Severity] [Bug class] in [endpoint] - [Brief impact]`

## BODY
```
Hello [Security Team / Name from security.txt],

I am a security researcher and would like to responsibly disclose the following vulnerability in [Asset].

═══════════════════════════════════════════
Bug class:    [e.g., SQL Injection]
Severity:     [e.g., Critical (CVSS 9.8)]
CVSS vector:  AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
Affected:     https://target.tld/api/v1/...
Discovered:   YYYY-MM-DD
═══════════════════════════════════════════

## SUMMARY
[2 sentences]

## STEPS TO REPRODUCE
[numbered list]

## PROOF OF CONCEPT
[curl / minimal payload]

## IMPACT
[concrete, business-language paragraph]

## SUGGESTED REMEDIATION
[specific]

## DISCLOSURE TIMELINE
- I'm sharing this report privately, in good faith.
- Please confirm receipt within 5 business days.
- I propose a coordinated disclosure timeline of 90 days from initial confirmation.
- I will not publish details, share with third parties, or test further until acknowledged.

Best regards,
[Your name / handle]
PGP: [link to public key, optional]
```

## TIPS
- Always check `https://target.tld/.well-known/security.txt` first.
- Encrypt sensitive details with their PGP key if provided.
- Don't ask "is there a bounty" upfront — focus on disclosure first.
- Keep tone formal; some companies have legal teams reading.

## REFERENCES
disclose.io, securitytxt.org, GDPR Art 33 timelines
