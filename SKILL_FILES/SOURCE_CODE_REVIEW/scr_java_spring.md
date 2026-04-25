# SKILL: Java / Spring Source Code Review
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
