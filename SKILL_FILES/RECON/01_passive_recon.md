# SKILL: Passive Reconnaissance

## Version: 1.0 | Domain: recon | Trigger: `RECON MODE` or "passive recon on TARGET"

---

## IDENTITY IN THIS SKILL

I am the operator's silent recon engine. I never touch the target with active probes during this phase. Everything is third-party data sources, OSINT, and historical archives. The target's WAF logs see nothing.

---

## WHY PASSIVE FIRST

Active probing leaves logs, triggers WAFs, gets you IP-blocked, sometimes triggers blue-team incident workflows that can result in bounty disqualification. Passive gives you:

- 80% of the asset inventory before the target knows you exist
- Historical endpoints (deleted code, leaked staging) that no longer exist on live infra
- Tech stack fingerprints (Wappalyzer, BuiltWith, Shodan history) that betray vendor versions
- Leaked secrets in GitHub / GitLab / public S3 / Pastebin / Dockerhub

---

## DECISION TREE

```
TARGET TYPE → DATA SOURCE
====================================
Apex domain (example.com)
  → CT logs (crt.sh, certspotter, Censys certificates)
  → Passive DNS (SecurityTrails, DNSdumpster, VirusTotal, BinaryEdge, Whoisxmlapi)
  → ASN / netblock (Hurricane Electric BGP, bgp.he.net, ipinfo.io)
  → Wayback / archive.org / CommonCrawl (gau, waybackurls, urlhunter)
  → GitHub / GitLab / Bitbucket dorks + leaked secrets
  → Search engine dorks (Google, Bing, DuckDuckGo, Yandex)
  → Shodan, Censys, FOFA, ZoomEye, BinaryEdge, Hunter.how, Quake360
  → Cloud: cloud_enum (AWS S3 / Azure blobs / GCP buckets)

Company name / brand
  → Acquisitions: Crunchbase, Wikipedia, SEC EDGAR (10-K filings list subsidiaries)
  → People: LinkedIn / Hunter.io / RocketReach (build target email patterns)
  → Trademarks / domains: WhoisXML reverse-whois, ViewDNS reverse-IP, RiskIQ PassiveTotal

Mobile app (package name)
  → Google Play / Apple App Store metadata (developer name → reverse-whois back to other apps)
  → APKMirror / APKPure historical APKs (older = more vulns)

Web3 contract address
  → Etherscan / BSCscan code page → linked GitHub
  → Github org of protocol team
```

---

## COMMANDS & WORKFLOWS

### A. Certificate Transparency (deepest passive subdomain source)

```bash
# crt.sh — full text JSON
curl -s "https://crt.sh/?q=%25.example.com&output=json" \
  | jq -r '.[].name_value' \
  | sed 's/\*\.//g' \
  | sort -u > ct_subs.txt

# certspotter (better deduplication, free 100/hr)
curl -s "https://api.certspotter.com/v1/issuances?domain=example.com&include_subdomains=true&expand=dns_names" \
  | jq -r '.[].dns_names[]' | sort -u >> ct_subs.txt

# subfinder ALL passive sources at once (uses your ~/.config/subfinder/provider-config.yaml)
subfinder -d example.com -all -silent -o subfinder.txt

# amass passive (slower but thorough)
amass enum -passive -d example.com -o amass.txt -timeout 5

# assetfinder
assetfinder --subs-only example.com > assetfinder.txt

# chaos-client (PD's recon dataset; needs CHAOS_KEY env)
chaos-client -d example.com -o chaos.txt -silent

# github-subdomains (Gwen001) — pulls subs from leaked code
github-subdomains -d example.com -t $GITHUB_TOKEN -o gh_subs.txt

# cero (subdomains via TLS SNI from related infra)
cero example.com | sed 's/^*\.//' | sort -u >> cero.txt

# Combine + dedup
cat ct_subs.txt subfinder.txt amass.txt assetfinder.txt chaos.txt gh_subs.txt cero.txt \
  | sort -u | grep -i "\.example\.com$" > all_subs_passive.txt
wc -l all_subs_passive.txt
```

### B. Passive DNS

```bash
# SecurityTrails (key in env: $ST_KEY)
curl -s "https://api.securitytrails.com/v1/domain/example.com/subdomains" \
  -H "APIKEY: $ST_KEY" \
  | jq -r '.subdomains[]' | sed 's/$/.example.com/' >> all_subs_passive.txt

# VirusTotal v3
curl -s "https://www.virustotal.com/api/v3/domains/example.com/subdomains?limit=40" \
  -H "x-apikey: $VT_KEY" | jq -r '.data[].id' >> all_subs_passive.txt

# DNSdumpster (no key, scrape with Python — see scripts/dnsdumpster.py)
python3 scripts/dnsdumpster.py example.com >> all_subs_passive.txt

# BinaryEdge
curl -s "https://api.binaryedge.io/v2/query/domains/subdomain/example.com" \
  -H "X-Key: $BE_KEY" | jq -r '.events[]' >> all_subs_passive.txt
```

### C. ASN / Netblocks

```bash
# Find ASN owned by company
curl -s "https://api.bgpview.io/search?query_term=Example+Inc" | jq '.data.asns'

# Pull all CIDRs for an ASN
asn=AS54321
curl -s "https://api.bgpview.io/asn/$asn/prefixes" \
  | jq -r '.data.ipv4_prefixes[].prefix' > netblocks.txt

# Reverse DNS the netblocks (still passive — uses public PTR records)
prips $(cat netblocks.txt) | dnsx -ptr -resp-only -silent > rdns.txt
```

### D. Wayback / Historical URLs

```bash
# All three flavors — combine
echo example.com | gau --threads 10 --subs > wayback_gau.txt
waybackurls example.com > wayback_wbu.txt
echo example.com | urlhunter -d 30days > wayback_uh.txt

# Combine, dedup, filter to interesting extensions
cat wayback_*.txt | sort -u \
  | grep -E "\.(php|asp|aspx|jsp|json|xml|env|bak|old|zip|tar\.gz|sql|js|map|conf|config|yml|yaml)(\?|$)" \
  > historical_interesting.txt

# Pull deleted/changed JS files (gold for stale endpoints + secrets)
cat wayback_*.txt | grep -E "\.js(\?|$)" | sort -u > historical_js.txt
```

### E. GitHub Dorks (passive — searches public code only)

```bash
# gitdorker
gitdorker -tf tokens.txt -q example.com -d dorks/medium_dorks.txt -o gh_dorks_results.txt

# trufflehog — public org scan
trufflehog github --org=example --concurrency=4 --json > gh_secrets.json

# manual Google-style code search
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/search/code?q=example.com+password" \
  | jq -r '.items[].html_url'
```

Useful dorks (place in `dorks/medium_dorks.txt`):
```
"example.com" password
"example.com" api_key
"example.com" secret
"example.com" jwt
"example.com" "BEGIN RSA PRIVATE KEY"
"example.com" filename:.env
"example.com" filename:.npmrc _auth
"example.com" filename:.dockercfg auth
"example.com" filename:wp-config.php
"example.com" extension:json client_secret
"example.com" "AWS_SECRET_ACCESS_KEY"
"example.com" "DATABASE_URL"
"example.com" filename:credentials aws_access_key_id
```

### F. Shodan / Censys / FOFA / ZoomEye

```bash
# Shodan — find their netblocks' exposed services (passive: Shodan already scanned)
shodan domain example.com
shodan search "ssl.cert.subject.cn:example.com"
shodan search "org:\"Example Inc\""
shodan search "hostname:example.com http.title:\"login\""

# Censys
censys search 'services.tls.certificates.leaf_data.subject.common_name: "example.com"'
censys search 'autonomous_system.organization: "Example Inc"'

# FOFA (better for asian / east-european targets)
echo 'cert="example.com"' | base64 -w0   # paste into FOFA query
echo 'icon_hash="-1234567890"' | base64 -w0   # find by favicon hash

# Favicon hash dorking — find related assets via favicon
python3 -c '
import mmh3, requests, codecs
r = requests.get("https://example.com/favicon.ico")
print(mmh3.hash(codecs.encode(r.content, "base64")))
'
```

### G. Cloud Asset Discovery (still passive)

```bash
# cloud_enum — checks public buckets/blobs/containers
cloud_enum -k example -k examplecorp -k example-prod -k example-dev -k example-staging \
  --disable-azure --disable-gcp 2>/dev/null

# s3scanner — only enumerates public buckets
s3scanner -bucket-file potential_buckets.txt -enumerate-bucket-objects

# Gobuster S3
gobuster s3 -w common-bucket-names.txt -t 50 -p "example-,examplecorp-,example_"
```

---

## CHECKLIST

- [ ] CT logs (crt.sh + certspotter + subfinder all-sources)
- [ ] Passive DNS (SecurityTrails, VT, DNSdumpster, BinaryEdge)
- [ ] ASN / netblock enumeration (BGPView)
- [ ] Reverse-IP (RiskIQ, ViewDNS) on each known IP
- [ ] Wayback / archive.org / CommonCrawl (gau + waybackurls)
- [ ] GitHub / GitLab / Bitbucket dorks
- [ ] TruffleHog org scan + git-secrets
- [ ] Shodan / Censys / FOFA / ZoomEye
- [ ] Favicon hash pivot
- [ ] Cloud asset discovery (cloud_enum, s3scanner, GCPBucketBrute)
- [ ] LinkedIn / Hunter.io email pattern + employee list
- [ ] Crunchbase / SEC EDGAR for acquisitions / subsidiaries
- [ ] Mobile app stores (Google Play / Apple App Store) for related apps
- [ ] Pastebin / paste.ee / ghostbin / 0bin scrape
- [ ] Dockerhub public images for the org name
- [ ] NPM / PyPI / RubyGems published packages by org email domain
- [ ] CertStream live (subscribe for new certs containing target domain)

---

## EDGE CASES

- **Wildcard DNS** — every subdomain resolves; you'll get noise. Solve with `puredns resolve --wildcard-batch 1500000` then filter NS records.
- **Cloudflare proxied** — IP behind CF; pivot via SecurityTrails historical A records + `tlsx` for SNI of origin server. Look at MX records too.
- **Acquisitions** — easy to miss. Always check Crunchbase + SEC 10-K + the company's own "press" page for "we acquired X".
- **Internal naming pattern leak** — if you see `dev-internal.example.com` or `jenkins-prod-2.example.com`, brute alterations: `puredns resolve` with `gotator` permutations.
- **Wildcard cert "*.example.com"** — doesn't tell you which subdomains exist. Use it as confirmation only.

---

## OUTPUT FORMAT

```
PASSIVE_RECON(example.com):
  subdomains: 1247 unique
  netblocks: 3 ASNs, 14 CIDRs, 4096 IPs
  historical_urls: 23,891
  github_secrets_hits: 7 (3 high-conf)
  shodan_exposed_services: 87 (incl 2 ES, 1 RDP, 4 SMB)
  cloud_buckets: 14 confirmed public
  acquisitions: AcmeCorp (2022), FooSoft (2021)

NEXT: feed all_subs_passive.txt → 02_subdomain_enumeration (active resolution + permutation)
```

---

## SOURCES

- `zseanos-methodology.pdf` — passive recon flow
- `Bug Hunters Methodology Live Day One Recon.pdf` — jhaddix's 2024 stack
- `Bug Bounty Bootcamp` (Vickie Li) Ch. 5 Recon
- `Elite_BugBounty_Methodology.pdf` — passive layer
- ProjectDiscovery docs — subfinder, chaos-client
- bgp.he.net, crt.sh, securitytrails.com, dnsdumpster.com docs
