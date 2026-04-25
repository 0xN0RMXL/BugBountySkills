# SKILL: Duplicate Avoidance
## Version: 1.0 | Domain: mindset

---

## PRE-SUBMISSION CHECKS
1. Search Hacktivity for the program: bug class + endpoint
2. Search Bugcrowd Hacktivity API
3. Search Twitter / blog posts for "writeup [target] [class]"
4. Check program's last 30 days disclosed bugs
5. Check #infosec channels mentioning the target

## STRATEGIES TO MINIMIZE DUPES
- **First-mover**: monitor new scope additions and report within hours.
- **Variant analysis**: take a public bug class report, find the exact same class on a different endpoint of the same target.
- **Deep over wide**: 100 hours on one bug = lower dupe rate than 100 hours on 10 surface scans.
- **Off-the-beaten-path**: focus on subdomains <10 ranking on H1's bug report counts.
- **Specialize**: GraphQL bugs, OAuth misconfigs, race conditions — fewer hunters do these well.

## BUG CLASSES WITH HIGH DUPE RATES
- Reflected XSS in obvious params
- Subdomain takeover on common services
- Open S3 buckets named `target-*`
- Default-creds on common admin paths

## BUG CLASSES WITH LOW DUPE RATES
- Race conditions
- Server-side prototype pollution
- Logical chains across multiple bugs
- Custom auth schemes (SAML / OAuth)
- WebSocket / postMessage handlers
- File upload edge cases (mime confusion, path manipulation)
- Cache deception with custom param

## IF YOU SUSPECT DUPE
- Submit anyway with thorough impact (sometimes original was lower-severity).
- Cite the suspected dupe in your report — shows good faith.

## REFERENCES
Hacktivity dupe analysis blogs, Critical thinking podcast
