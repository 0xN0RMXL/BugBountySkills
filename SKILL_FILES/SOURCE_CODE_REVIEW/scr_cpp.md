# SKILL: C/C++ Source Code Review
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
