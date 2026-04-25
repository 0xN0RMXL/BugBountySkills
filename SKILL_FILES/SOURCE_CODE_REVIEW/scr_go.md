# SKILL: Go Source Code Review
## Version: 1.0 | Domain: scr

---

## PATTERNS TO FLAG
```go
exec.Command("sh", "-c", userInput)         // shell injection
fmt.Sprintf("SELECT * FROM x WHERE id=%s", id)  // SQLi (use prepared)
template.HTML(userInput)                      // bypass auto-escape → XSS
template.URL(userInput)                       // bypass URL escape
text/template instead of html/template        // no auto-escape (XSS in HTML output)
http.Get(userURL)                             // SSRF
http.Redirect(w, r, userInput, 302)           // open redirect
filepath.Join(base, userInput)                // can still go above base via ".."; check filepath.Clean
os.OpenFile(userPath, ...)                    // path traversal
ioutil.ReadFile(userPath)
yaml.Unmarshal — generally safe but check custom types
gob.Decode                                    // type confusion
encoding/asn1 with custom types
reflect-based deserialization
```

## SAFE BY DEFAULT
- `database/sql.DB.Query("...?...", arg)` — parameterized.
- `html/template` — auto-escapes for HTML, JS, URL contexts.
- `crypto/rand` for tokens (not `math/rand`).

## RACE
```go
// goroutine without sync
go func() { sharedMap[k] = v }()             // race
// Use sync.Mutex / sync.RWMutex / sync.Map

// time-of-check vs time-of-use
if !exists(file) { create(file) }            // TOCTOU
```

## TOOLS
```bash
gosec ./...
staticcheck ./...
nilaway ./...
semgrep --config=p/go ./...
```

## REFERENCES
gosec, OWASP Go Security
