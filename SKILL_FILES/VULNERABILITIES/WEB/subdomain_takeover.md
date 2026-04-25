# SKILL: Subdomain Takeover

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (subdomain takeover) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Sub CNAMEs to a service the org no longer owns (S3, Heroku, Github Pages, Vercel, Netlify, Azure CDN, Fastly, Cloudfront, Shopify, Tilda). Register that resource → host content under target.com.

---

## DETECTION
`dnsx -cname -resp` then for each CNAME, fetch and look for the service's "unclaimed" fingerprint (e.g., S3 'NoSuchBucket', Heroku 'no-such-app').

## EXPLOITATION
1. Find dangling CNAME.
2. Identify service from the response error.
3. Register/claim that resource on the third-party service.
4. Host content / serve cookies under `target.com`.

## PAYLOADS (real, copy-paste, grouped)
(no payloads)

## BYPASS TECHNIQUES
(some services moved to per-account claim verification — Heroku, Github Pages now require domain verification; legacy still works.)

## CHAIN POTENTIAL
Takeover → cookie/CORS-trust abuse (cookies set on parent domain become accessible) → cross-site authenticated XSS / ATO.

## TOOLS
subjack, nuclei (http/takeovers/), takeover, Project Discovery 'subzy'

## COMMANDS
```bash
subjack -w subs.txt -t 100 -timeout 30 -ssl -c ~/tools/subjack/fingerprints.json -v -o takeovers.txt
nuclei -l alive.txt -t http/takeovers/ -severity high,critical
subzy run --targets subs.txt --hide_fails
```

## EDGE CASES / NOT-A-BUG TRAPS
Vercel/Netlify added strict domain verification; old `_vercel` TXT-style targets still claimable. Test before declaring.

## TRIAGE ANGLE (per platform)
Show served content from your account on target's domain.

## SEVERITY & CVSS
8.0+ (high if cookie/CORS-trust applies).

## REFERENCES
EdOverflow can-i-take-over-xyz • PayloadsAllTheThings/Subdomain Takeover
