# SKILL: Race Conditions (Single-Packet Attack / Sub-State / TOCTOU)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (race conditions (single-packet attack / sub-state / toctou)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Modern race-window is 50ms. Single-packet attack (PortSwigger) collapses to 1ms. I send 30 parallel requests in one TCP packet via HTTP/2 multiplex.

---

## DETECTION
Anywhere `check → mutate` happens: balance check + transfer, coupon redeem, vote, like, account creation, follow, friend invite, file rename.

## EXPLOITATION
1. Identify check-and-act endpoint.
2. Use Turbo Intruder `race-single-packet-attack` template (HTTP/2). Or BurpSuite Repeater 'Send group in parallel (single packet)'.
3. Submit 30 identical requests in one TCP packet. Server's check passes for each in parallel before any mutation lands.

## PAYLOADS (real, copy-paste, grouped)
(no payloads — race window is the primitive)

## BYPASS TECHNIQUES
Some apps require warm-up request to keep connection cooked; pre-send a benign HEAD.

## CHAIN POTENTIAL
Race → infinite coupon redemption / double-spend / role escalate via concurrent invites.

## TOOLS
Turbo Intruder (Burp), `frogger`, custom Python with `httpx.AsyncClient` + h2

## COMMANDS
```python
# Turbo Intruder race-single-packet-attack
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=1, engine=Engine.BURP2)
    engine.queue(target.req, gate='race1')
    for i in range(29):
        engine.queue(target.req, gate='race1')
    engine.openGate('race1')
def handleResponse(req, interesting): table.add(req)
```

## EDGE CASES / NOT-A-BUG TRAPS
Cloudfront / nginx may serialize via single connection; force parallelism with 30 distinct TCP connections OR multiplex via HTTP/2.

## TRIAGE ANGLE (per platform)
Show 1 → N effect (e.g., balance change once expected, but happened 5×).

## SEVERITY & CVSS
Financial: 9.0; non-fin: 6.0+.

## REFERENCES
PortSwigger Single-Packet Attack research
