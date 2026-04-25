# SKILL: Staying Ahead of Patches
## Version: 1.0 | Domain: mindset

---

## METHODOLOGY
Bugs get patched. To stay finding bugs:
1. Subscribe to security mailing lists (oss-security, full-disclosure, project-specific advisories).
2. Watch GitHub Security Advisories DB → daily.
3. Monitor Twitter / Mastodon / Bluesky for #InfoSec / #BugBounty.
4. Read PortSwigger Research, Detectify Labs, Truffle Security blog, Snyk blog, Doyensec, NCC Group.
5. Read ALL P1/P2 H1 disclosures within 48h of disclosure.
6. Subscribe to nuclei-templates GitHub releases — new templates = new known patterns.

## VARIANT ANALYSIS
- When a CVE drops, search the codebase for similar patterns elsewhere.
- When a bug class is disclosed (e.g., HTTP/2 desync) — try it on every target you know.
- When a tool releases (e.g., new Nuclei template) — run against your saved scope.

## LEARNING SOURCES (RANKED)
1. PortSwigger Web Security Academy — labs (free)
2. PortSwigger Research blog
3. HackerOne / Bugcrowd hacktivity
4. NahamSec / Stök / InsiderPhD / IppSec / LiveOverflow YouTube
5. Trail of Bits / Doyensec / NCC blogs
6. Twitter — @albinowax, @garethheyes, @james_kettle, @samwcyo, @nahamsec
7. The Daily Swig
8. Critical Thinking — Bug Bounty Podcast

## OWN RESEARCH
- When you find a novel pattern, write it up + variant-analyze.
- Publish (with permission) → builds rep → invites + freelance → more bugs.

## REFERENCES
PortSwigger Top 10 Web Hacking Techniques (annual)
