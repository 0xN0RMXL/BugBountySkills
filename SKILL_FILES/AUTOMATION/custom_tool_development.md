# SKILL: Custom Tool Development
## Version: 1.0 | Domain: automation

---

## WHEN TO BUILD CUSTOM
- Existing tool can't handle your specific edge case
- You need finer control over output for downstream pipeline
- Speed matters and existing tool is bottleneck
- Your target has specific quirks (custom protocols, weird auth)

## GO TEMPLATE (concurrent HTTP scanner)
```go
package main
import ( "fmt"; "net/http"; "bufio"; "os"; "sync"; "time"; "crypto/tls" )

func main() {
    sem := make(chan struct{}, 50)
    var wg sync.WaitGroup
    s := bufio.NewScanner(os.Stdin)
    client := &http.Client{Timeout: 7*time.Second, Transport: &http.Transport{TLSClientConfig: &tls.Config{InsecureSkipVerify: true}}}
    for s.Scan() {
        url := s.Text()
        sem <- struct{}{}; wg.Add(1)
        go func(u string) {
            defer wg.Done(); defer func(){<-sem}()
            r, err := client.Get(u)
            if err != nil { return }
            defer r.Body.Close()
            if r.StatusCode == 200 { fmt.Println(u) }
        }(url)
    }
    wg.Wait()
}
```

## PYTHON TEMPLATE (async)
```python
import asyncio, httpx, sys

async def probe(client, url):
    try:
        r = await client.get(url, timeout=7)
        if r.status_code == 200: print(url, flush=True)
    except: pass

async def main():
    sem = asyncio.Semaphore(50)
    async with httpx.AsyncClient(verify=False) as c:
        async def w(u):
            async with sem: await probe(c, u)
        urls = sys.stdin.read().split()
        await asyncio.gather(*(w(u) for u in urls))

asyncio.run(main())
```

## TIPS
- I/O-bound: use async (Go goroutines, Python asyncio, Node)
- CPU-bound: use Rust / Go
- Quick scripts: bash + xargs -P
- Pipe-friendly: stdin/stdout, no auth files
- Unix philosophy: do one thing well

## REFERENCES
Tomnomnom's tools (assetfinder, gf, qsreplace, anew) — exemplar of small composable tools
