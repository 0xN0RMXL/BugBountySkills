# SKILL: API Fuzzing Methodology
## Version: 1.0 | Domain: api

---

## IDENTITY
Systematic fuzzing of every parameter, header, body field, and path segment against an API.

## METHODOLOGY
1. **Inventory:** Collect all endpoints (Swagger, crawl, JS, mobile, kiterunner).
2. **Auth matrix:** Run every endpoint as: unauthenticated, low-priv user, admin. Compare.
3. **Parameter fuzz:** For each param, inject:
   - SQLi: `' OR 1=1-- -`, `" OR 1=1-- -`
   - XSS: `<svg/onload=alert(1)>`
   - SSRF: `http://169.254.169.254/`
   - SSTI: `{{7*7}}`
   - LFI: `../../../../etc/passwd`
   - Command injection: `; id`
   - NoSQL: `{"$ne":null}`
   - Type juggling: int→string, string→array, null, empty
4. **Content-Type fuzz:** Same body as JSON, XML, form, multipart.
5. **Method fuzz:** GET/POST/PUT/PATCH/DELETE/OPTIONS/HEAD.
6. **Header fuzz:** Inject auth-bypass headers per endpoint.
7. **Rate limit test:** 100 rapid-fire identical requests.

## TOOLS
```bash
# Nuclei API templates
nuclei -l api_endpoints.txt -t http/cves/ -t http/exposures/ -t http/vulnerabilities/ -severity medium,high,critical

# kiterunner
kr scan https://target -A=apiroutes-210126:20210126

# ffuf param brute
ffuf -u 'https://target/api/search?FUZZ=test' -w ~/wordlists/SecLists/Discovery/Web-Content/burp-parameter-names.txt -mc 200

# Arjun
arjun -u 'https://target/api/data' -m GET POST
```

## REFERENCES
OWASP API Security Testing Guide
