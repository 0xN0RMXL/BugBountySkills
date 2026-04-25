# Stored XSS in PDF / SVG / DOC Render

## 📌 What It Is
Application accepts user-uploaded PDF/SVG and renders inline; or generates PDF server-side from user HTML. JS executes when victim views.

## 🔍 How to Find It
Upload SVG containing `<script>alert(1)</script>` → if rendered inline (not as image), executes.\nFor PDF generation: inject HTML/JS into fields rendered with wkhtmltopdf, weasyprint, etc.

## 🧪 How to Test It
1. Try SVG with embedded JS\n2. Try PDF with `<script>` (Acrobat-supported)\n3. For server-side rendering: inject `<iframe src=file:///etc/passwd>` (LFI) or `<script>fetch('http://internal/api')</script>` (SSRF)

## 💣 How to Exploit It
When server renders user HTML to PDF using browser engine, injected JS runs in server context → SSRF / LFI / token exfil.

## 🔄 Bypass Techniques
Bypasses: Content-Type tampering (`image/svg+xml` vs `text/xml`), filename extension trick (`.png.svg`).

## 🛠️ Tools
- Burp Upload Scanner\n- exiftool to embed metadata\n- custom SVG/PDF templates

## 🎯 Payloads
```svg\n<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"></svg>\n```

## 📝 Real-World Examples
Multiple Shopify, Salesforce, Snapchat reports.

## 🚩 Common Mistakes / Traps
Don't confuse SVG XSS with stored XSS in profile bio. Server-side PDF render via Chrome → very different attack model.

## 📊 Severity & Impact
High to Critical (server-side context = SSRF/LFI).

## 🔗 References
PortSwigger XSS in upload labs.

## ⚡ One-Liners
```bash\ncurl -F 'file=@evil.svg' https://target/upload\n```
