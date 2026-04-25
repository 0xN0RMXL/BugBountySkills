# SKILL: Bash Hunting Scripts
## Version: 1.0 | Domain: scripting

---

## ESSENTIAL ONE-LINERS

### Subdomain enumeration → alive
```bash
subfinder -d $T -all -silent | tee subs.txt | httpx -silent -threads 100 -o alive.txt
```

### Quick top-hit asset shot
```bash
echo $T | subfinder -all -silent | dnsx -silent -a -resp-only | sort -u
```

### Mass status-code triage
```bash
cat urls.txt | httpx -status-code -title -tech-detect -threads 100 -silent -no-color | tee httpx.txt
```

### Wayback URL pull → dedup → param URLs
```bash
echo $T | gau --threads 10 --subs | sort -u | grep -E '\?[a-zA-Z0-9_]+=' > params.txt
```

### Common files probe
```bash
for p in /.git/config /.env /robots.txt /sitemap.xml /server-status /actuator/env /api/swagger.json; do
  while read u; do echo "$u$p"; done < alive.txt
done | httpx -silent -mc 200 -path-stats
```

### Extract endpoints from JS
```bash
cat alive.txt | katana -d 3 -jc -kf all -f endpoint -silent
cat alive.txt | hakrawler -d 3 -subs | sort -u
```

### CORS probe
```bash
while read u; do
  o=$(curl -sk -H "Origin: https://evil.tld" -I "$u" | grep -i 'access-control-allow-origin' )
  [ -n "$o" ] && echo "$u → $o"
done < alive.txt
```

### Quick subdomain takeover
```bash
subzy run --targets alive.txt --hide_fails --concurrency 100
nuclei -l alive.txt -t ~/nuclei-templates/http/takeovers/ -severity high,critical
```

### CRLF probe
```bash
while read u; do
  echo "$u/%0d%0aSet-Cookie:%20pwn=1" | xargs curl -sik | grep -i 'set-cookie:.*pwn' && echo "CRLF: $u"
done < urls.txt
```

### Open redirect probe
```bash
cat params.txt | qsreplace 'https://evil.tld' | httpx -silent -follow-redirects -mr 'evil.tld' | tee redirect.txt
```

## TIPS
- `set -euo pipefail` — fail-fast on any error
- `xargs -P NUM -I {}` — parallel without spinning up Go
- `parallel ::: ` — gnu parallel for complex pipelines
- Always pipe through `anew` to dedup against last-known-state file

## REFERENCES
PortSwigger Lab solutions, tomnomnom/anew
