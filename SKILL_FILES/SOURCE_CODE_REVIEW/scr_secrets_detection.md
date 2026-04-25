# SKILL: Secrets Detection in Source Code
## Version: 1.0 | Domain: scr

---

## TOOLS
- **trufflehog** — best for verified secret detection
- **gitleaks** — fast pattern matching
- **detect-secrets** (Yelp) — for pre-commit hooks
- **noseyparker** — Rust, fast historical scan
- **scoutsuite, nodejsscan** — multi-purpose

## COMMANDS
```bash
# Whole repo + history
trufflehog filesystem --json . > truffle.json
trufflehog git file://. --only-verified

# Org-wide
trufflehog github --org=examplecorp --only-verified --json > org.json

# Gitleaks
gitleaks detect --source=. --report-format=json --report-path=leaks.json

# Including dangling commits
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(rest)' | awk '$1=="blob" {print $2}' > all_blobs.txt
for blob in $(cat all_blobs.txt); do
  git cat-file -p $blob | grep -E 'AKIA|ghp_|gho_|ghs_|sk_live|xoxb-' && echo "BLOB: $blob"
done
```

## CUSTOM REGEX (high-value)
```
AKIA[0-9A-Z]{16}                            # AWS access key
ghp_[a-zA-Z0-9]{36}                          # GitHub PAT
ghs_[a-zA-Z0-9]{36}                          # GitHub server token
gho_[a-zA-Z0-9]{36}                          # GitHub OAuth
xox[baprs]-[a-zA-Z0-9-]+                     # Slack
sk_live_[0-9a-zA-Z]{24,}                     # Stripe live
sk_test_[0-9a-zA-Z]{24,}                     # Stripe test
SG\.[a-zA-Z0-9_-]{22}\.[a-zA-Z0-9_-]{43}     # SendGrid
AIza[0-9A-Za-z_-]{35}                         # Google API
[a-zA-Z0-9+/=]{300,}                          # large base64 → keys/certs
-----BEGIN [A-Z ]+ PRIVATE KEY-----            # any private key
```

## VERIFICATION (don't report unverified)
- AWS: `aws sts get-caller-identity`
- GitHub: `curl -H "Authorization: token X" https://api.github.com/user`
- Slack: `curl -X POST https://slack.com/api/auth.test -H "Authorization: Bearer X"`
- Stripe: `curl https://api.stripe.com/v1/balance -u X:`

## REFERENCES
trufflehog, gitleaks docs
