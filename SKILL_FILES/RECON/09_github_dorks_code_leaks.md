# SKILL: GitHub / GitLab / Bitbucket Dorks & Code Leaks
## Version: 1.0 | Domain: recon | Trigger: any target with employees on GitHub; almost always

---

## IDENTITY IN THIS SKILL
Public code search reveals: hardcoded creds, internal hostnames, API keys, JWT signing secrets, OAuth client_secret, AWS keys, DB strings, internal Slack webhooks, PII test fixtures.

---

## TOOLS
- `gitdorker — automated dork runner with multi-token rotation`
- `trufflehog — secret scanner with verifiers`
- `gitleaks — fast regex-based secret scanner`
- `github-search (gwen001) — by-organization scrape`
- `github-subdomains (gwen001) — pulls subs from leaked code`
- `git-hound — recursive scan + verify`
- `goop — diff-based GitHub recon`
- `Pastebin / paste.ee / 0bin / ghostbin — keep an eye via bin scrapers (psbdmp, pastebeen)`

## COMMANDS & WORKFLOWS
### Run dorks via gitdorker (handles rate limiting + token rotation)
```bash
gitdorker -tf ~/.config/gitdorker/tokens.txt -q example.com -d ~/tools/gitdorker/Dorks/medium_dorks.txt -o gitdorker_results/ -ev 0.5
```

### Truffle org scan with verifiers
```bash
trufflehog github --org=examplecorp --json --concurrency=8 --only-verified > truffle_examplecorp.json
# Per-user (employees you found via LinkedIn)
for u in $(cat employees_github_handles.txt); do
  trufflehog github --user="$u" --json --only-verified >> truffle_users.json
done
```

### Manual API code search (granular)
```bash
for q in 'password' 'api_key' 'secret' 'jwt' 'token' 'aws_secret' 'BEGIN RSA PRIVATE KEY' 'authorization: bearer' 'Set-Cookie:' 'admin' 'staging' 'internal'; do
  curl -s -H "Authorization: token $GITHUB_TOKEN" \
    "https://api.github.com/search/code?q=%22example.com%22+$q&per_page=100" \
    | jq -r '.items[] | "[\(.repository.full_name)] \(.html_url)"'
done > gh_code_search.txt
```

### GitLab + Bitbucket equivalents
```bash
# GitLab API (key in $GITLAB_TOKEN)
curl -s --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "https://gitlab.com/api/v4/search?scope=blobs&search=example.com&per_page=100"
# Bitbucket
curl -s -u "$BB_USER:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/repositories/?role=member&q=name~%22example%22"
```

### Find deleted commits (gitleaks --redact -v + reflog)
```bash
git clone --mirror https://github.com/example/repo.git
cd repo.git
gitleaks detect --no-git -v
# To get every blob, including dangling:
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(rest)' | awk '$1=="blob" {print $2}' > all_blobs.txt
```

### Pastebin scrape (live)
```bash
psbdmp search example.com
# OR scrape paste.ee API
curl -s 'https://paste.ee/api/v1/pastes/?key=$PASTEEE_KEY&q=example.com'
```

### Dockerhub leaked images
```bash
# Find images tagged with company name
curl -s 'https://hub.docker.com/v2/search/repositories/?query=example' | jq -r '.results[].repo_name'
# Pull + extract layers + grep for secrets
docker pull example/app:latest
docker save example/app:latest | tar -xv -O '*.tar' | tar -xv | grep -rE 'AKIA|password|secret' /tmp/extracted/
```

### npm / PyPI / RubyGems search by org email
```bash
# npm packages with author email matching @example.com
npm search --json author:example.com | jq '.[] | .name'
# PyPI
curl -s 'https://pypi.org/search/?q=example' | grep -oE '/project/[^/]+/' | sort -u
```



## DORKS
```
# Place these in `dorks/medium_dorks.txt` and rotate via gitdorker

# Auth / Secrets
"example.com" password
"example.com" api_key
"example.com" apikey
"example.com" "secret_key"
"example.com" "client_secret"
"example.com" "auth_token"
"example.com" jwt
"example.com" "Bearer"
"example.com" "aws_secret_access_key"
"example.com" "aws_access_key_id"
"example.com" AKIA
"example.com" SLACK_TOKEN
"example.com" "stripe_api_key"
"example.com" "twilio_auth_token"
"example.com" "github_token"
"example.com" "ghp_"
"example.com" "ghs_"
"example.com" "gho_"
"example.com" "BEGIN RSA PRIVATE KEY"
"example.com" "BEGIN OPENSSH PRIVATE KEY"
"example.com" "BEGIN DSA PRIVATE KEY"
"example.com" "BEGIN EC PRIVATE KEY"
"example.com" "BEGIN PGP PRIVATE KEY"

# Files
"example.com" filename:.env
"example.com" filename:.npmrc _auth
"example.com" filename:.dockercfg auth
"example.com" filename:.git-credentials
"example.com" filename:wp-config.php
"example.com" filename:credentials aws_access_key_id
"example.com" filename:id_rsa
"example.com" filename:id_dsa
"example.com" filename:id_ecdsa
"example.com" filename:id_ed25519
"example.com" filename:.htpasswd
"example.com" extension:pem private
"example.com" extension:ppk private
"example.com" extension:p12
"example.com" extension:pfx
"example.com" extension:sql
"example.com" extension:bak
"example.com" extension:log
"example.com" extension:conf
"example.com" extension:cnf
"example.com" extension:config
"example.com" extension:sh "ssh"

# Internal infra
"example.com" "internal"
"example.com" "staging"
"example.com" "dev"
"example.com" "test.example.com"
"example.com" "vpn"
"example.com" "ldap"
"example.com" "mongodb://"
"example.com" "postgres://"
"example.com" "mysql://"
"example.com" "redis://"
"example.com" "amqp://"
"example.com" "smtp.example.com"
"example.com" "DB_PASSWORD"
"example.com" "DATABASE_URL"

# Cloud-specific
"example.com" s3://
"example.com" "s3.amazonaws.com"
"example.com" "*.s3.amazonaws.com"
"example.com" "ec2-"
"example.com" "blob.core.windows.net"
"example.com" "googleapis.com"
"example.com" "storage.googleapis.com"
```


## EDGE CASES
- **Forks / mirrors / bots** — same secret may live in 10 forks. Dedup by file hash to triage faster.
- **Private repos accidentally public** — check the repo's history; sometimes was private then made public — old commits leak secrets.
- **Verified vs unverified** — trufflehog `--only-verified` is conservative. Run without first, then validate the high-conf ones.
- **Slack token live test** — `curl -s -X POST https://slack.com/api/auth.test -H "Authorization: Bearer $token"`; if `ok:true`, working — instant P1.
- **AWS creds live test** — `aws sts get-caller-identity` with the keys; if account ID matches the target, P1. Don't escalate beyond `sts:GetCallerIdentity` in PoC — triagers love minimum-impact PoCs.
- **Dependency Confusion candidates** — internal package names leaked in `package.json`, `requirements.txt`, `pom.xml`, `Gemfile.lock` → see `dependency_confusion.md`.

## OUTPUT FORMAT
```
GITHUB___GITLAB___BITBUCKET_DORKS_&_CODE_LEAKS({target}):
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
