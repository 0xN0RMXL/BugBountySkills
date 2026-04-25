# SKILL: JavaScript / Node.js Source Code Review
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
