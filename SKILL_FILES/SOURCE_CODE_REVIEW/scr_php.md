# SKILL: PHP Source Code Review
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
