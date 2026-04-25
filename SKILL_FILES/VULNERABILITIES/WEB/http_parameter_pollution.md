# SKILL: HTTP Parameter Pollution (HPP)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (http parameter pollution (hpp)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Two `?param=a&param=b` — different layers parse differently. WAF sees first, app sees last (or concat).

---

## DETECTION
Send duplicate params; observe behavior diff.

## EXPLOITATION
| Layer | First | Last | Concat |
|---|---|---|---|
| PHP/Apache | last | last | n/a |
| ASP.NET | concat (`,`) | concat | concat |
| ASP/IIS | concat (`,`) | concat | concat |
| Node.js (Express) | array | array | array |
| Python Flask/Django | first | first | n/a |
| Java/Tomcat | first | first | n/a |
| Java/Jetty | first | first | n/a |
| Ruby on Rails | last | last | n/a |
| Perl/CGI | last | last | n/a |

## PAYLOADS (real, copy-paste, grouped)
```
?id=1&id=2
POST: id=1&id=2
JSON dup keys: {"id":1,"id":2}    (parser-dependent)
```

## BYPASS TECHNIQUES
WAF sees `id=1` (first); app sees `id=2` (last) → bypass.

## CHAIN POTENTIAL
HPP + auth bypass / WAF bypass / business-logic skew.

## TOOLS
Burp Repeater, Param Miner

## COMMANDS
Manual

## EDGE CASES / NOT-A-BUG TRAPS
Modern frameworks normalize but legacy stacks split. Mixed-stack proxies very common.

## TRIAGE ANGLE (per platform)
Show side-by-side normalization difference.

## SEVERITY & CVSS
5–8 (depends on chain).

## REFERENCES
OWASP HPP • PortSwigger
