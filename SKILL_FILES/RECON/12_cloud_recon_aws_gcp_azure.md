# SKILL: Cloud Recon (AWS / GCP / Azure)
## Version: 1.0 | Domain: recon | Trigger: any modern target; almost always cloud-hosted

---

## IDENTITY IN THIS SKILL
Discover exposed S3 buckets, public Azure blobs, GCP Cloud Storage, dangling subdomains pointing at decommissioned cloud resources, exposed Lambda function URLs, public Cognito user pools, exposed App Runner / ECS / GKE services.

---

## TOOLS
- `cloud_enum (initstring) — sweep AWS / GCP / Azure for permutations of company names`
- `s3scanner — bucket existence + perms + listing`
- `GCPBucketBrute — GCP equivalent`
- `MicroBurst — Azure-specific (PS module)`
- `scoutsuite — when you have read creds, audits everything`
- `prowler — same`
- `pacu — AWS post-exploit framework (READ-ONLY modules for recon)`
- `trufflehog — over downloaded bucket contents`

## COMMANDS & WORKFLOWS
### cloud_enum — broad sweep
```bash
cloud_enum --keyword example --keyword examplecorp --keyword example-prod --keyword example-dev --keyword example-staging --keyword example-internal --logfile cloud_enum.log
```

### S3 bucket enumeration with naming permutations
```bash
# Build wordlist
for prefix in '' 'dev-' 'prod-' 'staging-' 'qa-' 'test-' 'backup-' 'data-' 'logs-' 'media-' 'static-' 'assets-' 'public-' 'private-' 'internal-' 'cdn-' 'images-' 'uploads-' 'web-' 'api-' 'app-'; do
  for suffix in '' '-dev' '-prod' '-staging' '-qa' '-test' '-backup' '-data' '-logs' '-prd'; do
    echo "${prefix}example${suffix}"; echo "${prefix}examplecorp${suffix}"
  done
done | sort -u > bucket_names.txt
# Test
s3scanner -bucket-file bucket_names.txt -enumerate-bucket-objects -threads 50 -output s3_results.json
```

### Test for AWS Cognito leaks
```bash
# Any unauth identity pool?
aws cognito-identity get-id --identity-pool-id us-east-1:xxxx --no-sign-request   # if returns IdentityId, pool is open
aws cognito-identity get-credentials-for-identity --identity-id $ID --no-sign-request   # creds = AssumeRole into account
```

### Azure storage blob enumeration
```bash
# DNS-based existence test
for n in example examplecorp examplestg exampledev; do
  for variant in storage data backup logs files; do
    h="${n}${variant}.blob.core.windows.net"
    dig +short "$h" @1.1.1.1 | head -1 | grep -q '\.' && echo "EXISTS: $h"
  done
done
# Then test list
for h in $exists; do curl -sI "https://$h/?comp=list"; done
```

### GCP Cloud Storage
```bash
# Bucket existence
for n in example example-prod example-data; do
  curl -sI "https://storage.googleapis.com/$n/" | head -1
done
# GCPBucketBrute
python3 gcpbucketbrute.py -k example -u   # -u = unauth
```

### Lambda function URL discovery
```bash
# Look for *.lambda-url.<region>.on.aws hostnames in: JS files, wayback, sub enum, GitHub
rg -oE '[a-z0-9]+\.lambda-url\.[a-z0-9-]+\.on\.aws' js/ wayback/ -h | sort -u
```

### CloudFront distribution discovery
```bash
# Sub points to *.cloudfront.net but distribution is unclaimed → takeover
for sub in $(cat alive.txt); do
  cname=$(dig +short cname "$sub" @1.1.1.1 | tail -1)
  if echo "$cname" | grep -q 'cloudfront.net'; then
    code=$(curl -sk -o /dev/null -w '%{http_code}' "https://$sub/")
    [ "$code" = "403" ] && curl -sk "https://$sub/" | grep -q 'Bad request' && echo "DANGLING: $sub → $cname"
  fi
done
```

### AWS access key validity test (passive — only sts:GetCallerIdentity)
```bash
AWS_ACCESS_KEY_ID=AKIA... AWS_SECRET_ACCESS_KEY=... aws sts get-caller-identity --no-paginate
```

### Azure AD tenant discovery (no auth needed)
```bash
curl -sI "https://login.microsoftonline.com/example.com/.well-known/openid-configuration"
# Returns tenant ID + endpoints. Pivot to MSGraph for user enum if guest invite is open.
```




## EDGE CASES
- **Bucket exists but ListObjects denied** — try `?max-keys=0` or `Range:` header tricks; sometimes individual GET on guessed key paths works. Generate keys from JS file references.
- **Lambda function URL with `AuthType: NONE`** — instant unauth RCE proxy if function logic eval-uates input.
- **Azure storage `?comp=list`** — anonymous-read containers expose every blob name.
- **GCP IAM scoped only to `roles/viewer`** — still grants `compute.instances.list`, `secretmanager.secrets.list` (sometimes), `storage.objects.list` — material disclosure.
- **CloudFront `Bad request: Unable to forward to host`** — origin host header doesn't match — distribution may still be claimable.
- **S3 takeover via 'NoSuchBucket'** — sub CNAMEs to `bucket.s3.amazonaws.com`, returns NoSuchBucket → register that bucket name → takeover.

## OUTPUT FORMAT
```
CLOUD_RECON_(AWS___GCP___AZURE)({target}):
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
