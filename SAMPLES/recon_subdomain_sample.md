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

