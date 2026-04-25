# SKILL: Python Source Code Review
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
