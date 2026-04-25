# SKILL: Iframe-based Attacks (sandbox escape, srcdoc XSS, frame busting bypass)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (iframe-based attacks (sandbox escape, srcdoc xss, frame busting bypass)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Sandboxed iframes have policy quirks. srcdoc + missing CSP yields cross-origin XSS in sandboxed contexts.

---

## DETECTION
Map all iframes. Check sandbox attributes, CSP frame-ancestors, postMessage flow.

## EXPLOITATION
- `sandbox="allow-scripts allow-same-origin"` is effectively no sandbox.
- iframe `srcdoc` has same-origin context → `<iframe srcdoc='<script>...'></script>` runs as parent.
- Frame busting via `top.location` blocked by sandbox="allow-top-navigation" missing → still embedded for clickjacking.

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
(see above)

## CHAIN POTENTIAL
Iframe XSS in third-party widget embedded by target → mass XSS on target's own users.

## TOOLS
manual

## COMMANDS
manual

## EDGE CASES / NOT-A-BUG TRAPS
Modern browsers added Strict-Transport / Cross-Origin-Embedder; check support per browser.

## TRIAGE ANGLE (per platform)
Show actual XSS firing in target's main origin.

## SEVERITY & CVSS
7.0–8.5.

## REFERENCES
MDN iframe sandbox • PortSwigger labs
