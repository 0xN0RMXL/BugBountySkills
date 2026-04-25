# SKILL: Bugcrowd Tactics
## Version: 1.0 | Domain: platform-intel

---

## VRT FOCUS
Bugcrowd's payouts hard-map to VRT. Memorize key categories you hunt:
- P1: Server-Side Injection — RCE; Remote Code Execution; Cleartext Transmission of Session Cookie
- P2: Subdomain Takeover; Server-Side Injection — SQL; SSRF (internal services)
- P3: Stored XSS; Reflected XSS (privileged); BOLA
- P4: CSRF (state-changing); Reflected XSS (low impact)

Always cite the VRT leaf in the report — fewer disputes.

## PRIORITIZATION RATING (PR)
Bugcrowd has both VRT (category) and Severity (P1-P5). PR helps map between them.
- PR1 = Critical, PR4 = Low

## TRIAGER NOTES
- Bugcrowd triagers (CrowdControl staff) tend to be stricter on duplicate detection.
- ASR (Application Security Researcher) certification gives priority queue access.
- Programs often have bonuses for "first finder" or "best chain of the month".

## QUEUE BEHAVIOR
- "MVP" and "Targeted" programs are private; build rep on public to get invites.
- Time-to-triage SLAs published per program — escalate if missed.

## DUPES
- Bugcrowd is stricter — same vuln class on same asset = dupe by default.
- But IDOR on `/api/x` and IDOR on `/api/y` are usually treated as separate (test both).

## SCOPE
- Out-of-scope assets are firmly rejected — no exception even for criticals.
- "Anything not listed" is in-scope NOT default; always confirm.

## REFERENCES
bugcrowd.com/researcher-docs, bugcrowd.com/vrt
