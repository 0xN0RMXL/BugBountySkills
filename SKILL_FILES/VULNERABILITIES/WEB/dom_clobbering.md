# SKILL: DOM Clobbering

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (dom clobbering) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
HTML elements with `id`/`name` attributes shadow `window`/`document` properties → break security checks. Useful when CSP blocks scripts but allows HTML.

---

## DETECTION
Find code like `if (window.config && config.allow)` or `document.someName.foo` — clobbber these via injected HTML.

## EXPLOITATION
```html
<a id=defaultAvatar href=evil.tld>
<form id=user><input id=isAdmin value=true>
<img name=cookie src=//attacker.tld>
```

PortSwigger DOMPurify clobbering bypass via `<form><input id=attributes>`.

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Even sanitized HTML may permit <a id=...> and <input id=...>.

## CHAIN POTENTIAL
Combined with CSP-restricted XSS to bypass nonce validation when nonce is read from `document.x`.

## TOOLS
Burp DOM Invader

## COMMANDS
DOM Invader walks for clobberable globals automatically

## EDGE CASES / NOT-A-BUG TRAPS
Modern apps use Shadow DOM and `window.x` reads behind closures — clobbering doesn't shadow those.

## TRIAGE ANGLE (per platform)
Show end-to-end privilege escalation / XSS that required clobbering.

## SEVERITY & CVSS
6.5–8.5.

## REFERENCES
PortSwigger DOM Clobbering • s1r1us research
