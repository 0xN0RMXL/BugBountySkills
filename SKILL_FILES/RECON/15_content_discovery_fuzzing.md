# SKILL: Content Discovery & Fuzzing
## Version: 1.0 | Domain: recon | Trigger: after recon; need hidden paths, params, files, methods

---

## IDENTITY IN THIS SKILL
Wordlist-based brute force of paths, files, parameters, headers, HTTP methods, vhost names — discover content that's not linked anywhere.

---

## TOOLS
- `ffuf — fast, recursive, scriptable`
- `feroxbuster — Rust, async, recursion built-in`
- `dirsearch — Python, has good wordlists bundled`
- `gobuster — fewer features but stable`
- `x8 — parameter discovery via response analysis`
- `arjun — parameter brute via diff`
- `ParamMiner (Burp ext) — by-product when you browse`
- `kiterunner — API-aware`

## COMMANDS & WORKFLOWS
### ffuf — recursive directory + extension brute
```bash
ffuf -u "https://$TARGET/FUZZ" \
  -w ~/wordlists/SecLists/Discovery/Web-Content/raft-large-directories.txt \
  -mc all -fc 404,403 -ac -recursion -recursion-depth 2 \
  -e .json,.xml,.bak,.old,.zip,.tar.gz,.tar,.7z,.rar,.git,.svn,.env,.yml,.yaml,.txt,.log,.sql,.bak,.swp,.tmp,.orig,.dist,.example,.config,.conf,.ini,.cfg \
  -t 50 -timeout 7 -p 0.05 -of json -o ffuf.json
```

### Fuzz HTTP methods
```bash
for m in GET POST PUT PATCH DELETE OPTIONS HEAD TRACE CONNECT PROPFIND MKCOL COPY MOVE LOCK UNLOCK; do
  curl -sk -o /dev/null -w "$m %{http_code}\n" -X "$m" "https://$TARGET/api/admin"
done
```

### Vhost / Host header brute
```bash
ffuf -u "https://$TARGET/" -H "Host: FUZZ.example.com" \
  -w ~/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt \
  -mc 200,301,302 -fs 0 -ac -t 50 -of csv -o vhost.csv
```

### Parameter brute (arjun)
```bash
arjun -u 'https://example.com/api/data' -m POST --json --headers "Authorization: Bearer $T" --stable
# x8 alternative
x8 -u 'https://example.com/api/data' -X POST -m GET POST -w ~/wordlists/SecLists/Discovery/Web-Content/burp-parameter-names.txt
```

### Header brute (find hidden auth bypass headers)
```bash
ffuf -u 'https://example.com/admin' -H 'FUZZ: 127.0.0.1' \
  -w ~/wordlists/headers.txt -mc 200,302 -fc 403,404 -ac
# headers.txt sample:
# X-Forwarded-For
# X-Real-IP
# X-Originating-IP
# X-Remote-IP
# X-Remote-Addr
# X-Client-IP
# X-Host
# X-Forwarded-Host
# X-Original-URL
# X-Rewrite-URL
# X-Custom-IP-Authorization
# X-Originating-IP
# True-Client-IP
# Cluster-Client-IP
# CF-Connecting-IP
```

### Recursive feroxbuster (better than ffuf for deep recursion)
```bash
feroxbuster -u https://$TARGET -w ~/wordlists/raft-large-directories.txt \
  -t 50 -d 5 --auto-tune --auto-bail \
  -x .json .bak .old .zip .git .env .yml \
  -C 404 -F 403 \
  -o ferox.txt
```

### Filter-Bypass content discovery (when 403 / 404 are wildcards)
```bash
# Discover via response size variance
ffuf -u 'https://example.com/FUZZ' -w big.txt -mc all -fs 0,1234   # exclude default 1234-byte 404
# OR by response time
ffuf -u 'https://example.com/FUZZ' -w big.txt -mc all -p 0.1 -of csv | awk '$N{print}'  # custom analysis
```



## WORDLISTS

## Default wordlist set (place in ~/wordlists/)
SecLists:
  Discovery/Web-Content/raft-large-directories.txt
  Discovery/Web-Content/raft-large-files.txt
  Discovery/Web-Content/raft-large-words.txt
  Discovery/Web-Content/big.txt
  Discovery/Web-Content/Common-PHP-Filenames.txt
  Discovery/Web-Content/CMS/wp_plugins.txt
  Discovery/Web-Content/api/api-endpoints.txt
  Discovery/Web-Content/api/objects.txt
  Discovery/Web-Content/api/api-endpoints-res.txt
  Fuzzing/LFI/LFI-Jhaddix.txt
  Fuzzing/SQLi/Generic-SQLi.txt
  Fuzzing/XSS/XSS-Jhaddix.txt
  Discovery/DNS/subdomains-top1million-110000.txt
  Passwords/Common-Credentials/10-million-password-list-top-10000.txt
  Discovery/Web-Content/burp-parameter-names.txt
  Discovery/Web-Content/AWS.txt

assetnote-wordlists (https://wordlists.assetnote.io):
  ApiObjects.txt
  parameters_top_1m.txt
  bruteforce-lists/api-endpoints.txt
  longtail/raft-large-files.txt

Onelistforall:
  https://github.com/six2dez/OneListForAll

Custom:
  one4all.txt = combine + sort -u all of the above


## EDGE CASES
- **Wildcard responses** — every path returns 200 with the SPA shell. Use `-fs <size>` to filter, or `-fr <regex>` to filter response bodies. Or `-mc 200 -fl <line count>`.
- **Soft 404** — `200 OK` with body `Not Found`. Use `-fr 'Not Found'` or compare body MD5 against known 404.
- **Rate limit on big wordlist** — chunk wordlist + sleep between waves; rotate `-x` proxy list.
- **WAF false positives on payload-shaped wordlist entries** — neutral wordlists like `raft-large-directories` are fine; using SQLi/XSS payload lists for content discovery triggers WAF and gets you blocked.
- **GET vs POST diff** — `-X POST` reveals `/api/users` only handles POST; GET returns 405. Always run both.
- **JSON body fuzz** — for APIs, `-X POST -d '{"FUZZ":"x"}'` to find hidden keys.

## OUTPUT FORMAT
```
CONTENT_DISCOVERY_&_FUZZING({target}):
  <key>: <value>
  ...
NEXT: handoff to next stage
```

## SOURCES
- Bug Hunters Methodology Live Day One Recon (jhaddix)
- zseanos-methodology
- Elite_BugBounty_Methodology
- ProjectDiscovery / Assetnote / SecLists
- HackTricks recon section
- PortSwigger Research blog
