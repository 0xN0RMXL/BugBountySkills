# SKILL: Cross-Site WebSocket Hijacking (CSWSH) — dedicated

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (cross-site websocket hijacking (cswsh) — dedicated) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Same as websocket_attacks.md CSWSH section but isolated for clarity.

---

## DETECTION
Origin not validated on WS handshake.

## EXPLOITATION
(see websocket_attacks.md)

## PAYLOADS (real, copy-paste, grouped)
(see websocket_attacks.md)

## BYPASS TECHNIQUES
(see websocket_attacks.md)

## CHAIN POTENTIAL
(see websocket_attacks.md)

## TOOLS
websocket-csrf-poc generator

## COMMANDS
Burp → Engagement Tools → WebSocket CSRF PoC

## EDGE CASES / NOT-A-BUG TRAPS
Cookie-based WS auth + missing Origin check is the only route. Token-in-Header WS auth is safe.

## TRIAGE ANGLE (per platform)
Show cross-site script subscribing as victim.

## SEVERITY & CVSS
8.0+.

## REFERENCES
PortSwigger CSWSH
