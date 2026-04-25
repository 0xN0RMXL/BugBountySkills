# SKILL: Port Scanning & Service Discovery
## Version: 1.0 | Domain: recon | Trigger: you have a netblock or IP list; need full TCP/UDP service map

---

## IDENTITY IN THIS SKILL
Beyond top-1000 web ports — find management interfaces, admin panels, queue brokers, DBs, internal services that drift onto the public IP space.

---

## TOOLS
- `naabu (PD) — fast SYN-style discovery`
- `masscan — full /16 in minutes if rate is high`
- `rustscan — fast wrapper that hands off to nmap`
- `nmap — version + script + OS detection (gold standard)`
- `smap — shodan-backed nmap-compatible (returns Shodan's already-scanned data; fully passive)`

## COMMANDS & WORKFLOWS
### Full TCP scan, exclude CDN ranges (avoid noise)
```bash
naabu -list netblocks.txt -p - -rate 10000 -exclude-cdn -o ports_full.txt
```

### masscan alternative
```bash
sudo masscan -p1-65535 --rate 25000 -iL netblocks.txt -oG masscan.gnmap
```

### Nmap version + script scan against discovered open ports
```bash
# Build target spec from naabu output
awk -F: '{print $1":"$2}' ports_full.txt > host_port.txt
# Run nmap with vuln scripts
nmap -sV -sC -O -Pn --script=vulners,vuln,banner,http-enum,smb-enum-shares,ftp-anon,smb-vuln-* \
  -iL <(awk -F: '{print $1}' ports_full.txt | sort -u) -p $(awk -F: '{print $2}' ports_full.txt | sort -u | tr '\n' ',') \
  -oA nmap_full
```

### Targeted hunt for HIGH-VALUE management ports
```bash
# 9200,9300 (Elasticsearch), 27017 (MongoDB), 6379 (Redis), 5432 (PG), 3306 (MySQL),
# 11211 (Memcached), 5984 (CouchDB), 1521 (Oracle), 1433 (MSSQL),
# 8500 (Consul), 4040 (Spark), 6066 (Spark master), 7077 (Spark master),
# 8086 (InfluxDB), 5601 (Kibana), 15672 (RabbitMQ mgmt), 8161 (ActiveMQ),
# 9000 (SonarQube/Portainer), 3000 (Grafana), 8081 (Jenkins UNCONF), 8080 (Jenkins/Tomcat),
# 7474 (neo4j), 9090 (Prometheus), 8888 (Jupyter), 9870/50070 (Hadoop),
# 2375/2376 (Docker daemon), 6443/10250 (k8s), 4243 (Docker), 28017 (MongoDB http),
# 8443/8888 (admin web), 50000 (DB2/SAP), 5985/5986 (WinRM), 5900-5902 (VNC)
naabu -list netblocks.txt -p 9200,9300,27017,6379,5432,3306,11211,5984,1521,1433,8500,8086,5601,15672,8161,9000,3000,8081,8080,7474,9090,8888,9870,50070,2375,2376,6443,10250,4243,28017,8443,50000,5985,5986,5900,5901,5902 -rate 5000 -o highvalue_ports.txt
```

### Passive port scan via Shodan (no packets to target)
```bash
smap -iL netblocks.txt -oG smap.gnmap   # uses Shodan API
```

### UDP top-100 (slow but catches DNS, SNMP, NTP, IPMI, MikroTik)
```bash
sudo nmap -sU --top-ports 100 -sV -iL netblocks.txt -oA nmap_udp
```




## EDGE CASES
- **WAF / IPS triggers** — masscan at >50k pps will get IP blacklisted. Throttle. Use VPS rotation.
- **Filtered ports** — `filtered` ≠ closed. Sometimes service is alive but firewalled. Re-test from VPS in different region.
- **Cloud LB ranges** — AWS/Azure/GCP LB ranges scan-noisy and meaningless. Filter via `cdncheck`.
- **Honeypots** — if every port responds and banners are generic, suspect honeypot. Confirm via `nmap --script=http-honeypot` or `shodan honeyscore IP`.
- **Wildcard SNI** — same IP serves many vhosts; need to swap `Host:` header to find the live one.

## OUTPUT FORMAT
```
PORT_SCANNING_&_SERVICE_DISCOVERY({target}):
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
