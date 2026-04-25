# Prototype Pollution — Server-Side RCE

## 📌 What It Is
JS object property modified via __proto__ / constructor.prototype. Pollution leaks into every object; downstream gadget triggers RCE.

## 🔍 How to Find It
Find merge/extend/clone/path-set sink (lodash _.merge, jQuery $.extend, mongoose, util.assign). Submit `{"__proto__":{"x":1}}`. Probe `{}.x` after.

## 🧪 How to Test It
1. Identify pollution: `?__proto__[admin]=true` or JSON body.\n2. Probe `{}.admin` post-pollution.\n3. Find gadget — Express render options, child_process spawn options, JSONPath, etc.\n4. Pollute that gadget → RCE.

## 💣 How to Exploit It
Server: pollute `process.mainModule.require('child_process').exec`-adjacent property → RCE on next request handling.

## 🔄 Bypass Techniques
If `__proto__` filtered → use `constructor.prototype`. If JSON.parse strips → use querystring.

## 🛠️ Tools
- ppmap, ppfuzz, pp-finder\n- Burp DOM Invader

## 🎯 Payloads
See PAYLOADS/prototype_pollution_payloads.md

## 📝 Real-World Examples
PortSwigger 2022 PP research, hapi.js / fastify / nuxt CVEs.

## 🚩 Common Mistakes / Traps
Don't confuse client-side (XSS) and server-side (RCE) PP — different gadgets.

## 📊 Severity & Impact
Critical (CVSS 9.8) for RCE.

## 🔗 References
PortSwigger PP server-side research, BlackHat 2018 (Olivier Arteau).

## ⚡ One-Liners
```bash\ncurl 'https://target/api?__proto__[admin]=true'\n```
