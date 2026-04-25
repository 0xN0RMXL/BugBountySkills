# SKILL: Ruby / Rails Source Code Review
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
