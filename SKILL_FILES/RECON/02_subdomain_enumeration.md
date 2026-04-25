# SKILL: Subdomain Enumeration (Active + Permutation)

## Version: 1.0 | Domain: recon | Trigger: `RECON MODE` after passive

---

## IDENTITY IN THIS SKILL

Passive recon gave us a seed list. Now we expand it via DNS bruteforcing + permutation + alteration. We resolve everything, dedup, and prep the alive set for HTTP probing.

---

## DECISION TREE

```
seed list → permutation → mass DNS resolution → wildcard filter → alive set
        ↘ pure brute force (only if seed list is thin) ↗
```

- Seed list ≥ 200? → **Skip brute-force**, go straight to permutation. Pure brute is dead in 2024+ unless the org has weird subs.
- Seed list < 50? → Pure brute force first with `puredns` + commonspeak2 + n0kovo big list.

---

## COMMANDS & WORKFLOWS

### A. Seed Aggregation

```bash
# Combine all passive sources into seed
cat ct_subs.txt subfinder.txt amass.txt assetfinder.txt chaos.txt gh_subs.txt \
  | sed 's/^\*\.//; s/\.$//' \
  | grep -E "^[a-zA-Z0-9._-]+\.example\.com$" \
  | tr '[:upper:]' '[:lower:]' \
  | sort -u > seed.txt
```

### B. Permutation Generation

```bash
# alterx — modern, regex-based
alterx -l seed.txt -enrich -o permutations.txt
# OR gotator — older but solid
gotator -sub seed.txt -perm permutations.txt -depth 1 -numbers 5 -mindup -adv -md > altered.txt

# ripgen — very fast
ripgen -d seed.txt > rip.txt

# Combine permutations
cat permutations.txt altered.txt rip.txt | sort -u > all_perm.txt
wc -l all_perm.txt   # often 200K-2M
```

Permutation patterns to also manually feed into a wordlist:
```
{env}-{name}.example.com    where env ∈ {dev,staging,stg,test,qa,uat,preprod,prod,prd,beta,sandbox,demo,internal,intra,intranet,corp,backend,api,admin}
{name}-{env}.example.com
{name}{n}.example.com       n ∈ 1..20
{name}-{n}.example.com
{region}-{name}.example.com region ∈ {us,eu,ap,uw1,ue1,euw1,euc1,apn1,aps1,jp,uk,fr,de,nl,sg,au}
```

### C. Mass DNS Resolution

```bash
# Get fresh public resolver list
wget -q https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt -O resolvers.txt

# Validate resolvers (cull bad ones — critical for accuracy)
dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 200 -o validated_resolvers.txt
# (or use trickest's pre-validated list above)

# puredns — best mass DNS resolver, has wildcard handling
puredns resolve all_perm.txt \
  --resolvers validated_resolvers.txt \
  --rate-limit 5000 \
  --wildcard-tests 30 \
  --wildcard-batch 1500000 \
  --write resolved.txt \
  --write-massdns massdns_raw.txt

# shuffledns alternative (PD)
shuffledns -d example.com -list all_perm.txt -r validated_resolvers.txt -o resolved_sd.txt
```

### D. Wildcard Detection (CRITICAL)

```bash
# Manually verify — query 5 random non-existent names
for i in 1 2 3 4 5; do
  rand=$(openssl rand -hex 8)
  dig +short "$rand.example.com" @1.1.1.1
done
# If they all resolve to the same IP → wildcard. puredns handles this with --wildcard-batch but verify.

# Hunt wildcard *exceptions* — subs that DO resolve differently
# These are the real subs hiding in a wildcard DNS zone
puredns resolve all_perm.txt -r validated_resolvers.txt --wildcard-batch 1500000 -w resolved.txt
```

### E. Pure Brute Force (when seed is thin)

```bash
# Combine all the heavyweights
cat \
  /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt \
  /usr/share/seclists/Discovery/DNS/n0kovo_subdomains_huge.txt \
  /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt \
  | sort -u > brute.txt
wc -l brute.txt   # ~3M

puredns bruteforce brute.txt example.com \
  --resolvers validated_resolvers.txt \
  --rate-limit 5000 \
  --wildcard-batch 1500000 \
  --write brute_resolved.txt
```

### F. Final Combine + Live Probe (handoff to skill 03)

```bash
cat seed.txt resolved.txt brute_resolved.txt | sort -u > live_candidates.txt
wc -l live_candidates.txt

# Probe HTTP/S — basic alive check
httpx -l live_candidates.txt -ports 80,443,8080,8443,8000,8888,8008,8081,8181,9000,9090,3000,5000,7000,7443,8443 \
  -threads 100 -timeout 5 -retries 1 -silent -o alive.txt
```

---

## EDGE CASES

- **DNS over HTTPS only / split-horizon** — public resolvers won't see internal subs. `dnsx -ptr` reverse-PTR scan against the company netblock catches some.
- **Anycast wildcard with rotating IPs** — looks like noise. Filter by HTTP response body hash via `httpx -hash mmh3` and dedup.
- **CNAME chaining** — sub → 3rd party hosting (S3 / Heroku / Github Pages / Vercel / Netlify / Azure CDN / Cloudfront / Akamai). Run `dnsx -cname -resp-only` and look for dangling targets — feeds into `subdomain_takeover.md`.
- **Internationalized domain names (IDN)** — `xn--` prefix. Don't filter them out.

---

## CHECKLIST

- [ ] Seed aggregated from all passive sources
- [ ] Wildcard detected and handled
- [ ] alterx + gotator + ripgen permutations generated
- [ ] Resolvers validated (dnsvalidator or trickest list)
- [ ] puredns mass resolution complete
- [ ] Pure brute (n0kovo + jhaddix + top-110k) merged in
- [ ] Final unique resolved list → handoff to `03_dns_analysis` and `08_fingerprinting_tech_stack`

---

## OUTPUT FORMAT

```
SUBDOMAIN_ENUM(example.com):
  seed: 1247
  permutations_generated: 1.4M
  resolved: 1893 unique
  wildcard_filtered: yes (wildcard resolves to 1.2.3.4)
  CNAME_to_3rd_party: 17 (S3:5, Heroku:3, Cloudfront:4, Vercel:2, Netlify:3) → check takeover
  ALIVE (HTTP/S): 1456 hosts × 1.6 ports avg = 2310 endpoints
```

---

## SOURCES

- `Bug Hunters Methodology Live Day One Recon.pdf` (jhaddix recon stack)
- ProjectDiscovery docs — puredns, shuffledns, dnsx
- d3mondev/puredns README
- Trickest resolver list
- alterx README (PD)
