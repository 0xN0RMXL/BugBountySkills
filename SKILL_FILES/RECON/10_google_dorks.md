# SKILL: Google / Bing / DuckDuckGo / Yandex Dorks
## Version: 1.0 | Domain: recon | Trigger: any time; but especially when starting on a new program

---

## IDENTITY IN THIS SKILL
Search-engine dorks surface admin panels, exposed endpoints, leaked docs, public buckets, sub-zone exposures. Free, fast, and the engines have indexed things you'd never find via crawl.

---

## TOOLS
- `Google search operators`
- `Bing operators (slightly different syntax)`
- `DuckDuckGo (less rate-limited; bangs to other engines)`
- `Yandex (best for Russian-speaking targets / less indexed corners)`
- `uDork — automates dork lists`
- `GoogD0rker (script to rotate UAs + proxies)`

## COMMANDS & WORKFLOWS
### uDork — automate a dork list
```bash
udork -t example.com -d ~/tools/uDork/dorks.txt -o results.html
```

### Manual rate-limited rotation (custom Python)
```bash
# scripts/google_dorks.py reads dorks.txt, uses serpapi or googlesearch-python
python3 scripts/google_dorks.py -d example.com -i dorks.txt -o dork_hits.txt
```



## DORK LIBRARY

## Subdomain / Asset Discovery
site:*.example.com -www
site:example.com -site:www.example.com
site:example.com -site:blog.example.com -site:docs.example.com   # find unusual subs
site:example.com inurl:dev
site:example.com inurl:staging
site:example.com inurl:test
site:example.com inurl:internal
site:example.com -inurl:www -inurl:blog -inurl:docs

## Login Pages & Admin Panels
site:example.com inurl:login
site:example.com inurl:admin
site:example.com inurl:wp-admin
site:example.com inurl:dashboard
site:example.com intitle:"admin login"
site:example.com intitle:"sign in"
site:example.com inurl:portal
site:example.com inurl:console
site:example.com inurl:management

## Sensitive Files
site:example.com ext:env
site:example.com ext:log
site:example.com ext:bak | ext:old | ext:sql | ext:zip | ext:tar | ext:tar.gz | ext:rar
site:example.com ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini
site:example.com ext:json
site:example.com ext:xml
site:example.com ext:pdf "confidential"
site:example.com ext:pdf "internal use only"
site:example.com filetype:pdf "password"

## Backup / Sourcecode Disclosure
site:example.com ext:bak
site:example.com ext:swp
site:example.com inurl:.git
site:example.com inurl:.svn
site:example.com inurl:.hg
site:example.com inurl:.DS_Store
site:example.com inurl:.idea
site:example.com inurl:wp-content/backup
site:example.com inurl:dump.sql
site:example.com inurl:db.sql

## API / Swagger / GraphQL
site:example.com inurl:api
site:example.com inurl:swagger
site:example.com inurl:swagger-ui
site:example.com inurl:openapi
site:example.com inurl:redoc
site:example.com inurl:api-docs
site:example.com inurl:graphql
site:example.com inurl:graphiql
site:example.com inurl:playground
site:example.com inurl:apollo
site:example.com inurl:wsdl

## Errors / Stack Traces (vuln signal)
site:example.com "stack trace"
site:example.com "Whitelabel Error Page"
site:example.com "PHP Parse error"
site:example.com "Warning: include"
site:example.com "Fatal error"
site:example.com "ORA-00921"
site:example.com "Microsoft OLE DB Provider"
site:example.com "java.lang.NullPointerException"
site:example.com "Traceback (most recent call last)"
site:example.com intext:"sql syntax near"
site:example.com intext:"Microsoft VBScript runtime error"
site:example.com intext:"Server.MapPath"

## Cloud Buckets via Search
"example" site:s3.amazonaws.com
"example" inurl:storage.googleapis.com
"example" inurl:blob.core.windows.net
inurl:s3.amazonaws.com "example"
inurl:digitaloceanspaces.com "example"
inurl:linodeobjects.com "example"

## Document Disclosure
site:example.com filetype:xls | filetype:xlsx
site:example.com filetype:doc | filetype:docx
site:example.com filetype:csv "password"
site:example.com filetype:txt password

## SSO / OAuth Misconfig
site:example.com inurl:redirect_uri
site:example.com inurl:callback
site:example.com inurl:oauth
site:example.com inurl:saml
site:example.com inurl:sso

## Reflected Param Reflection (for XSS hunting)
site:example.com inurl:redirect=
site:example.com inurl:url=
site:example.com inurl:returnTo=
site:example.com inurl:next=
site:example.com inurl:dest=
site:example.com inurl:return=

## Open Redirect Indicators
site:example.com inurl:redir=
site:example.com inurl:goto=
site:example.com inurl:return_url=
site:example.com inurl:rurl=

## SSRF Indicators
site:example.com inurl:url=
site:example.com inurl:fetch=
site:example.com inurl:img=
site:example.com inurl:image=
site:example.com inurl:proxy=
site:example.com inurl:webhook=

## File Upload Indicators
site:example.com inurl:upload
site:example.com inurl:fileupload
site:example.com inurl:attach
site:example.com intitle:"upload" "file"

## Hidden Subdirs / Index of
site:example.com intitle:"index of /"
site:example.com intitle:"index of" "parent directory"
site:example.com intitle:"index of" backup
site:example.com intitle:"index of" .git

## Vendor-Specific (Jira, Confluence, Jenkins, GitLab, Bamboo, Crowd, Slack)
site:example.com inurl:jira
site:example.com inurl:confluence
site:example.com inurl:jenkins
site:example.com inurl:gitlab
site:example.com inurl:bamboo
site:example.com inurl:crowd
site:example.com inurl:slack

## Pastebin-leaked
site:pastebin.com example.com
site:gist.github.com example.com
site:paste.ee example.com
site:0bin.net example.com


## EDGE CASES
- **Captcha after 20 queries** — rotate user agent + proxy + add 5–15s sleep. SerpApi or Bing API are paid alternatives.
- **Site sometimes blocks robots** — pages exist but don't appear in Google. Use Bing/Yandex/Baidu/Naver — different crawlers.
- **`-www` bias** — operators normalize, so `-site:www.example.com` may not strip all variants. Combine with `-inurl:www`.
- **Cached versions** — even after the site removes a page, Google's cache may still hold it; click `Cached` link or use `cache:` operator (deprecated but archive.org timetravel works similarly).

## OUTPUT FORMAT
```
GOOGLE___BING___DUCKDUCKGO___YANDEX_DORKS({target}):
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
