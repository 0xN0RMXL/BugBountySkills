# SKILL: JS / Node.js Hunting Scripts
## Version: 1.0 | Domain: scripting

---

## ENDPOINT EXTRACTION (PUPPETEER)
```javascript
const puppeteer = require('puppeteer');
(async () => {
  const b = await puppeteer.launch({headless:'new', args:['--no-sandbox','--ignore-certificate-errors']});
  const p = await b.newPage();
  const urls = new Set();
  p.on('request', r => urls.add(r.url()));
  await p.goto(process.argv[2], {waitUntil:'networkidle2', timeout:30000});
  for (const u of urls) console.log(u);
  await b.close();
})();
```

## DOM XSS HELPER
```javascript
// Browser console
[...document.querySelectorAll('a')]
  .filter(a => /javascript:|data:/i.test(a.href))
  .forEach(a => console.log(a.outerHTML));
// Sinks scan
['innerHTML','outerHTML','document.write','eval'].forEach(s => {
  console.log(s, document.body.outerHTML.match(new RegExp(s,'g'))?.length || 0);
});
```

## POST MESSAGE LISTENER (BROWSER CONSOLE)
```javascript
window.addEventListener('message', e => {
  console.log('FROM:', e.origin, 'DATA:', e.data, 'SOURCE:', e.source);
});
// Send a probe
top.postMessage({pwn:1}, '*');
```

## NODE FAST FUZZER
```javascript
const fetch = require('node-fetch'); const fs = require('fs');
const wl = fs.readFileSync(process.argv[3]).toString().split('\\n');
const tpl = process.argv[2];
const conc = 50;
let i = 0;
async function worker(){
  while (i < wl.length){
    const w = wl[i++];
    const u = tpl.replace('FUZZ', encodeURIComponent(w));
    try { const r = await fetch(u, {redirect:'manual'}); if (r.status === 200) console.log(r.status, u); } catch{}
  }
}
Promise.all(Array(conc).fill().map(worker));
// node fuzz.js 'https://target/FUZZ' wl.txt
```

## REFERENCES
puppeteer/playwright, axios/node-fetch
