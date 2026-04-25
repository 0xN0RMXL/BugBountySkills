# SKILL: Dangerous Functions Reference (All Languages)
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
