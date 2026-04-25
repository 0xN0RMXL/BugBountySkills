# SKILL: Bugcrowd Report Template
## Version: 1.0 | Domain: reporting

---

## VRT (Vulnerability Rating Taxonomy)
Bugcrowd uses VRT for severity. Find your bug at https://bugcrowd.com/vulnerability-rating-taxonomy.
- VRT category determines payout, not your CVSS.
- If VRT lists a category that fits, cite it explicitly.

## TITLE
`[VRT cat] in [endpoint] - [impact summary]`

## DESCRIPTION
- Summary
- Reproduction Steps (numbered)
- Proof of Concept (curl / HTML / video)
- Impact (concrete)
- Suggested Fix

## TARGETS FIELD
- Pick the asset from program scope.
- If asset is wildcard, specify the exact subdomain.

## BUG TYPE FIELD
Bugcrowd autocompletes from VRT — choose the closest leaf, not the top-level.

## TIPS
- Bugcrowd encourages chaining — show full chain explicitly with each link's CVSS / VRT.
- Bugcrowd is stricter on duplicate detection — search ASR / your collisions before submitting.
- Provide a PoC video for any client-side bug.
- Bugcrowd Submit Page has tag fields (CWE, OWASP) — fill them.

## REFERENCES
bugcrowd.com/vulnerability-rating-taxonomy, Bugcrowd Researcher Docs
