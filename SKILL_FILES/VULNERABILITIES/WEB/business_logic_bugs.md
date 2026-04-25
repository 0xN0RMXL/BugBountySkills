# SKILL: Business Logic Bugs

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (business logic bugs) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Highest-paid bugs in 2024. No payload — just creative misuse of the app's own state machine. I always look for: integer overflow / negative numbers, race conditions, multi-step skip, replay, ID swap in workflows, voucher/coupon abuse, refund manipulation, point/balance skew.

---

## DETECTION
Map the state machine. List every transition and verify it can only happen from the prior state. Test replay, skip, branch.

## EXPLOITATION
Common patterns:
- **Negative quantity** in cart → negative balance → company pays you.
- **Multiplier overflow** — quantity × price overflows 32-bit signed → wraps negative.
- **Replay successful checkout** — backend doesn't dedup `payment_intent_id` → double credit.
- **Skip step** — POST to step 5 directly without 1–4 → state machine accepts.
- **Voucher reuse** — same voucher across items / accounts.
- **Race in sign-up** — same email signs up 2× simultaneously, both verified.
- **Forced state transition** — `PATCH /order/123 {state:'paid'}` works because no state guard.
- **Identity confusion** — `creator_id` accepts any user; victim's content owned by you.
- **Subscription downgrade preserves features** — downgrade does not revoke; pay free, get pro.

## PAYLOADS (real, copy-paste, grouped)
(no payloads — see exploitation)

## BYPASS TECHNIQUES
(no bypasses — logic only)

## CHAIN POTENTIAL
Logic → financial loss / data exfil / privilege escalation.

## TOOLS
Burp Repeater + state diagram + creativity

## COMMANDS
Manual + Postman/Bruno

## EDGE CASES / NOT-A-BUG TRAPS
Triagers are picky — show concrete loss/gain quantified ($X gain).

## TRIAGE ANGLE (per platform)
Always quantify dollar / point / data impact.

## SEVERITY & CVSS
Up to 9.8 (financial fraud).

## REFERENCES
PortSwigger Business Logic Vulnerabilities
