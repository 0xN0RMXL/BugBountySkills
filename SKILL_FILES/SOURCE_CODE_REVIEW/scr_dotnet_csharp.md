# SKILL: .NET / C# Source Code Review
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
