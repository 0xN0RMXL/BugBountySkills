# SKILL: ffuf Automation
## Version: 1.0 | Domain: automation

---

## RECIPE — content discovery wrapper
```bash
#!/usr/bin/env bash
TARGET=$1
WL=${2:-~/wordlists/raft-large-directories.txt}
ffuf -u "https://${TARGET}/FUZZ" \
  -w "$WL" \
  -mc all -fc 404 -ac \
  -e .json,.xml,.bak,.old,.zip,.git,.env,.yml,.yaml,.txt,.log,.sql \
  -recursion -recursion-depth 2 \
  -t 50 -timeout 7 -p 0.05 \
  -of json -o "${TARGET//\//_}.json"
```

## RECIPE — parameter discovery
```bash
ffuf -u "https://target/api?FUZZ=test" -w ~/wordlists/burp-parameter-names.txt -mc 200 -fs 0 -ac
```

## RECIPE — Vhost discovery
```bash
ffuf -u "https://${IP}/" -H "Host: FUZZ.${TARGET}" -w ~/wordlists/subdomains-top1million-110000.txt -mc 200,301,302 -fs 0 -ac
```

## RECIPE — header bypass
```bash
ffuf -u "https://target/admin" -H "FUZZ: 127.0.0.1" -w ~/wordlists/headers.txt -mc 200,302 -fc 403,404 -ac
```

## REFERENCES
ffuf docs, OneListForAll, assetnote wordlists
