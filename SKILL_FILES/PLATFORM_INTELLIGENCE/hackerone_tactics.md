# SKILL: HackerOne Tactics
## Version: 1.0 | Domain: platform-intel

---

## PROGRAM SELECTION
- Filter `/directory/programs?response_efficiency=>=90`
- Filter by `bounty_table_value>=$X`
- Watch hacktivity for active triage
- Avoid programs with avg time to bounty >60 days unless justified

## TRIAGE PATTERNS
- H1 internal triagers (h1-001 etc.) handle most queue; some programs self-triage.
- Triagers reject self-XSS unless cross-user impact shown.
- Triagers love chained reports.
- Always cite Hacktivity precedent if disputing.

## SCOPE BOOSTERS
- `*.target.com` wildcard → enumerate aggressively
- Ineligible domains often still get accepted if impact is critical (ask before reporting low)
- `Plus all the new domains` clauses → first finder wins

## PAYOUT CALIBRATION
- H1 publishes program tier histograms (avg / median / range per severity).
- Hall of fame shows top earners — gauge program generosity.
- "Reputation only" programs — skip unless you're early career building rep.

## DUPES
- Use `state:NEW state:OPEN` filter before submitting → similar reports often disclosed.
- Search Hacktivity for the bug pattern + asset name → catch dupes early.

## REPORT STYLE
- Bold the impact line.
- Numbered repro, ≤10 steps.
- Keep summary to 3 sentences.
- Embed PoC code in fenced blocks with HTTP syntax.
- Always include "Tested on YYYY-MM-DD".

## H1-PRO / H1-CONFIDENTIAL
- Confidential reports never appear in Hacktivity.
- Some programs only invite via H1 ranks — submit quality reports to climb ranks.

## REFERENCES
hackerone.com/disclosure-guidelines, hackerone.com/leaderboard
