# Checklist: Deserialization
- [ ] Identify deserialization sink (Java ObjectInputStream, .NET BinaryFormatter, Python pickle, PHP unserialize, Node serialize, Ruby Marshal/YAML)
- [ ] Find serialized data in: cookies, hidden inputs, body, headers
- [ ] Probe with URLDNS chain (Java) or OOB DNS payload (others) — silent confirmation
- [ ] Use ysoserial / ysoserial.net / pickle for chain generation
- [ ] Test with multiple chains (CommonsCollections1-7, Spring, ROME for Java)
- [ ] If RCE — drop reverse shell, read /etc/passwd, etc.
- [ ] Check for type-confusion gadgets (Json.Net TypeNameHandling=All, FastJson)
- [ ] Test error-based detection if blind (cause exception, leak class names)
