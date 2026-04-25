# SKILL: DNS Analysis
## Version: 1.0 | Domain: recon | Trigger: after subdomain resolution; or 'analyze DNS for X'

---

## IDENTITY IN THIS SKILL
Beyond A/CNAME — pull every record type, look for misconfig, takeover candidates, mail spoofing primitives, and zone-transfer leftovers.

---

## TOOLS
- `dnsx -a -aaaa -cname -ns -mx -txt -soa -ptr -axfr -resp`
- `dig +short any example.com @1.1.1.1`
- `dnsrecon -d example.com -t std,brt,srv,axfr,goo,bing,zonewalk`
- `fierce -dns example.com`
- `nsec3walker / ldns-walk for DNSSEC NSEC enum`

## COMMANDS & WORKFLOWS
### Pull ALL record types in parallel
```bash
dnsx -l alive.txt -a -aaaa -cname -ns -mx -txt -soa -ptr -resp -silent -o dns_records.txt
```

### Detect dangling CNAMEs (takeover candidates)
```bash
dnsx -l alive.txt -cname -resp-only | tee cnames.txt
# Flag CNAMEs that point to NXDOMAIN or unclaimed third-party services:
for c in $(cat cnames.txt); do dig +short $c @1.1.1.1 | grep -q '^$' && echo "DANGLING: $c"; done
```

### Test for AXFR (zone transfer) on every NS
```bash
for ns in $(dig +short ns example.com); do
  echo "=== $ns ==="
  dig @"$ns" example.com AXFR +noidnout
done | tee axfr.txt
```

### DNSSEC NSEC zone walk (pulls every record without AXFR)
```bash
ldns-walk -s 1.1.1.1 example.com
# or nsec3walker for NSEC3 (slower but works on most modern setups)
```

### Find SPF/DMARC misconfig (email spoofing primitive)
```bash
dig +short txt example.com | grep -i spf
dig +short txt _dmarc.example.com
# SPF too permissive (+all, ?all, ~all + open relay) → spoofable
# DMARC missing/p=none → no rejection of forged mail
```

### CAA records (cert pinning bypass research)
```bash
dig +short caa example.com
```

### Reverse DNS sweep on netblocks
```bash
prips $(cat netblocks.txt) | dnsx -ptr -resp-only -silent | sort -u > rdns.txt
```




## EDGE CASES
- **Wildcard CNAMEs** — `*.example.com → cdn.thirdparty.com`. The wildcard itself isn't takeover-able; specific named subs that go through the wildcard might be. Test each.
- **Split-horizon DNS** — internal vs external view. You only see external. Pivot via leaked /etc/hosts in S3 or GitHub.
- **DNSSEC NSEC walking** — yields full zone for free if NSEC (not NSEC3). Always try first.
- **Cloudflare/Akamai-fronted MX** — origin server IP often leaked via MX record (mail server).
- **Email security misconfig (high-impact P3-P2):** SPF too permissive + DMARC `p=none` + missing DKIM = phishing primitive. Send forged email from `payments@target.com` to triager.

## OUTPUT FORMAT
```
DNS_ANALYSIS({target}):
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
