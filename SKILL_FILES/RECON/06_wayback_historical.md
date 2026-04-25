# SKILL: Wayback / Historical URL Mining
## Version: 1.0 | Domain: recon | Trigger: after passive recon; before content discovery

---

## IDENTITY IN THIS SKILL
Archive.org, CommonCrawl, AlienVault OTX, URLScan.io, and CertSpotter store snapshots of URLs that may no longer be in the live app — but the parameters, paths, and behaviors often still work, sometimes more vulnerable than current code.

---

## TOOLS
- `gau (gauplus) — pulls from waybackmachine + AlienVault + CommonCrawl + URLScan.io`
- `waybackurls — archive.org only`
- `urlhunter — date-bounded archive search`
- `github-endpoints — pull URL strings from leaked code`
- `katana (PD) — has -jsl flag to also pull from JS`
- `uro — dedup URLs by template`

## COMMANDS & WORKFLOWS
### Pull all historical URLs
```bash
echo example.com | gau --subs --threads 10 > wayback_gau.txt
echo example.com | waybackurls > wayback_wbu.txt
echo example.com | urlhunter -d 30d > wayback_uh.txt
cat wayback_*.txt | sort -u > all_historical.txt
wc -l all_historical.txt
```

### Dedup by URL template (reduce N×same param to 1)
```bash
uro < all_historical.txt > all_historical_uniq.txt
```

### Filter to interesting extensions / signs of leak
```bash
cat all_historical_uniq.txt | grep -E '\.(php|asp|aspx|jsp|do|action|cgi|json|xml|env|bak|old|orig|backup|swp|tmp|sql|tar|tar\.gz|zip|7z|rar|log|conf|config|cnf|ini|yml|yaml|pem|key|crt|p12|pfx|properties|rb|py|pl|sh|wsdl|wadl|swagger|openapi)(\?|$)' > sus_extensions.txt
```

### Extract parameters
```bash
cat all_historical_uniq.txt | unfurl --unique keys > param_names.txt
cat all_historical_uniq.txt | qsreplace FUZZ > urls_for_fuzzing.txt
```

### Diff: historical vs current (find resurrected endpoints / removed-but-still-live)
```bash
comm -23 <(sort all_historical_uniq.txt) <(sort current_crawl.txt) > only_in_historical.txt
# Test if any of these still respond
httpx -l only_in_historical.txt -mc 200,401,403 -threads 100 -silent > resurrected.txt
```

### Pull historical JS specifically (often dropped in newer builds, still hosted)
```bash
cat all_historical_uniq.txt | grep -E '\.js(\?|$)' > historical_js.txt
wget -i historical_js.txt -P historical_js/  # download for secret scan
trufflehog filesystem historical_js/ > historical_js_secrets.txt
```

### Pull historical robots.txt + sitemap.xml diffs (often disclose admin paths)
```bash
for snap in $(curl -s "http://web.archive.org/cdx/search/cdx?url=example.com/robots.txt&output=text&fl=timestamp,original&from=20150101" | awk '{print $1}'); do
  echo "=== $snap ==="; curl -s "https://web.archive.org/web/$snap/https://example.com/robots.txt"
done > robots_history.txt
```




## EDGE CASES
- **Soft 404 in archives** — archive page may render but be archived during a maintenance redirect. Spot-check before fuzzing.
- **Private archive pages** — some are not crawled because of `robots.txt`; URLScan.io often has them.
- **API contract leakage** — old `/swagger.json`, `/openapi.json`, `/api-docs` paths often hosted historically; fetch via wayback timetravel.
- **JS files with secrets** — old JS bundles may still have `apiKey: '...'` that was rotated, but sometimes wasn't (rotation is hard). Always test live.
- **Internal staging URLs** — `staging.example.com` might be archived even if no longer DNS-live; pivot for new subdomains.

## OUTPUT FORMAT
```
WAYBACK___HISTORICAL_URL_MINING({target}):
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
