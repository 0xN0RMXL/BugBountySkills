# SKILL: SAML Attacks (XML signature wrap / XXE / comments / replay)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (saml attacks (xml signature wrap / xxe / comments / replay)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
SAML XML is famously prone to signature-wrapping (SAMLraider), XXE in metadata, comment-injection (CVE-2018-0114-style).

---

## DETECTION
Burp + SAMLRaider extension. Decode and pretty-print every assertion.

## EXPLOITATION
### XML Signature Wrapping
Move the signed `<Assertion>` to a different position; insert your unsigned attacker assertion at the location the verifier reads.

### XXE in SAML metadata or assertion
See xxe_all_types.md — same payloads. Often metadata fetch is unauthenticated.

### Comment injection in NameID
Old XML parsers truncate at comment when extracting username:
```xml
<NameID>admin<!--injected-->@target.com</NameID>
```
Verifier extracts `admin@target.com` after stripping comment, but signature was over the full string — bypass.

### Assertion replay
SAML assertion has no nonce → reuse old one if NotOnOrAfter not enforced.

### XSLT injection
Malicious `<ds:Transform>` with XSLT that calls Java methods → RCE.

## PAYLOADS (real, copy-paste, grouped)
(see exploitation)

## BYPASS TECHNIQUES
(see exploitation)

## CHAIN POTENTIAL
SAML forgery → ATO across all federated apps.

## TOOLS
SAMLRaider (Burp), python3-saml debug, xmllint

## COMMANDS
Burp → SAMLRaider tab → Manipulate SAML request

## EDGE CASES / NOT-A-BUG TRAPS
Modern OpenSAML and python3-saml are hardened; rolled-your-own SAML on PHP is a goldmine.

## TRIAGE ANGLE (per platform)
Show admin assertion forged from valid user assertion.

## SEVERITY & CVSS
9.0+.

## REFERENCES
Duo Labs SAML pitfalls • Ivan Ristic SAML
