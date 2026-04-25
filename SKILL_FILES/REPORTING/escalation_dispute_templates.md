# SKILL: Escalation / Dispute Templates
## Version: 1.0 | Domain: reporting

---

## SCENARIO 1 — Triager closed as N/A but bug is real

```
Hello [triager],

Thanks for the review. I'd like to respectfully request reconsideration.

In the closure rationale you stated [QUOTE]. However, my report demonstrates [SPECIFIC EVIDENCE] — see step [N] of reproduction, screenshot [N].

To reinforce: an attacker [CONCRETE ATTACK]. Compare to similar accepted reports:
- [#h1-12345] — same class, same impact, awarded $X
- [#h1-67890] — variant of this bug, accepted as Y severity

I'd appreciate a fresh look. Happy to provide additional PoC, video, or a synchronous walkthrough.

Best,
[handle]
```

## SCENARIO 2 — Severity too low

```
Hello,

Thank you for the bounty. I'd like to discuss the severity rating.

The current rating is [LOW]. Based on the impact:
1. [IMPACT POINT 1 — quantified, e.g., "1.2M users affected"]
2. [IMPACT POINT 2 — e.g., "PII / financial data"]
3. [IMPACT POINT 3 — e.g., "no auth required"]

CVSS v3.1: [HIGHER VECTOR] = [HIGHER SCORE]

Compared to:
- [HACKTIVITY LINK] — same class, similar impact, rated [HIGHER]
- Bugcrowd VRT category [X] would map to [HIGHER]

Would you reconsider [HIGHER] severity?

Thanks,
[handle]
```

## SCENARIO 3 — Marked duplicate but the original was for a different endpoint

```
Hi,

Thanks for the review. I'd like to clarify the duplicate determination.

This report is for [ENDPOINT/PARAM A] with [SPECIFIC IMPACT A].
The cited duplicate appears to be for [ENDPOINT B] with [DIFFERENT IMPACT B].

While both are [BUG CLASS], they are distinct instances requiring separate fixes:
- [DIFFERENCE 1]
- [DIFFERENCE 2]

The fix for [B] would not address [A]. Could you confirm whether [A] is being treated as a separate finding?

Best,
[handle]
```

## SCENARIO 4 — No response after SLA window

```
Hi team,

This report has been pending [STATUS] for [N] days, beyond the program's stated SLA of [SLA].

Could you provide an update? I'm happy to clarify or provide more PoC if needed.

Per program policy, I will hold disclosure pending your response.

Thanks,
[handle]
```

## TONE
- Professional, evidence-based, not emotional.
- Always cite hacktivity / VRT precedent.
- Don't threaten public disclosure unless program SLA explicitly violated.

## REFERENCES
HackerOne mediation, Bugcrowd disclosure policy
