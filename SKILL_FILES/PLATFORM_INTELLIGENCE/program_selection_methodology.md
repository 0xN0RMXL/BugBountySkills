# SKILL: Program Selection
## Version: 1.0 | Domain: platform-intel

---

## DECISION FRAMEWORK
For each candidate program, score:

| Factor | Weight | Source |
|--------|--------|--------|
| Avg bounty for your bug class | 30% | hacktivity histogram |
| Scope size (large = more bugs) | 20% | scope page |
| Time-to-triage | 15% | program SLA + recent reports |
| Duplicate density | 15% | recent disclosed reports vs scope |
| Asset interest match | 10% | personal interest / specialty |
| Triage friendliness | 10% | hacktivity disputes / forum chatter |

Pick programs with score >70%.

## RED FLAGS
- "Subjective" severity language → triagers downgrade
- "We may award bounty at our discretion" → no SLA
- Resolution time >180 days median
- Active community complaints (Twitter, BB Discord)

## GREEN FLAGS
- Public hall of fame with active researchers
- Detailed scope with examples of in/out-of-scope
- Recently increased bounty tier
- Multiple H1/BC programs from same company (engineering culture aware of security)

## TIME ALLOCATION
- 70% on 2-3 deep targets you know well
- 20% on rotating new programs (first-mover)
- 10% on big-name public programs (rep, hall of fame)

## SPECIALIZATION
- If you specialize (e.g., GraphQL, OAuth, mobile), filter to programs with that surface.
- "Generalist" hunters spread thin → high dupe rate.

## REFERENCES
hackerone.com/programs/search, bugcrowd.com/programs
