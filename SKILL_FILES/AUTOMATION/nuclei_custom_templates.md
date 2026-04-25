# SKILL: Nuclei Custom Templates
## Version: 1.0 | Domain: automation

---

## STRUCTURE
```yaml
id: my-custom-check
info:
  name: Detect Specific Endpoint Misconfig
  author: hunter
  severity: high
  tags: misconfig,custom
http:
  - method: GET
    path:
      - "{{BaseURL}}/admin/debug"
    matchers-condition: and
    matchers:
      - type: word
        words:
          - "DEBUG"
          - "stack trace"
        condition: or
      - type: status
        status:
          - 200
```

## RUN
```bash
nuclei -t custom-templates/ -l targets.txt -o findings.txt -severity medium,high,critical
```

## DSL FUNCTIONS
- `to_lower`, `to_upper`, `base64`, `base64_decode`, `md5`, `sha256`, `len`, `contains`
- `dsl: ['contains(body,"foo") && status_code == 200']`

## DYNAMIC EXTRACTORS
```yaml
extractors:
  - type: regex
    regex:
      - 'token=([a-zA-Z0-9]+)'
    group: 1
```

## CHAINING (multi-step)
```yaml
http:
  - raw:
      - |
        POST /login HTTP/1.1
        Host: {{Hostname}}
        ...
    extractors:
      - type: regex
        name: token
        regex: ['token=([a-zA-Z0-9]+)']
        internal: true
  - raw:
      - |
        GET /admin HTTP/1.1
        Host: {{Hostname}}
        Cookie: session={{token}}
```

## REFERENCES
nuclei-templates GitHub, ProjectDiscovery docs
