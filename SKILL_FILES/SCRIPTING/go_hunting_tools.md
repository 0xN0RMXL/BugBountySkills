# SKILL: Go Hunting Tools (Build Your Own)
## Version: 1.0 | Domain: scripting

---

## SUBDOMAIN BRUTE
```go
package main
import ("bufio";"fmt";"net";"os";"sync")
func main() {
    sem := make(chan struct{}, 200); var wg sync.WaitGroup
    s := bufio.NewScanner(os.Stdin)
    for s.Scan() {
        host := s.Text()
        sem <- struct{}{}; wg.Add(1)
        go func(h string) {
            defer wg.Done(); defer func(){<-sem}()
            ips, err := net.LookupHost(h)
            if err == nil && len(ips) > 0 { fmt.Println(h) }
        }(host)
    }
    wg.Wait()
}
// build: go build -o resolve resolve.go
// use: cat candidates.txt | ./resolve > resolved.txt
```

## CONCURRENT GET
```go
package main
import ("bufio";"crypto/tls";"fmt";"net/http";"os";"sync";"time")
func main(){
    tr := &http.Transport{TLSClientConfig:&tls.Config{InsecureSkipVerify:true}}
    cl := &http.Client{Timeout:7*time.Second, Transport:tr,
        CheckRedirect: func(req *http.Request, via []*http.Request) error { return http.ErrUseLastResponse }}
    sem := make(chan struct{},100); var wg sync.WaitGroup
    s:=bufio.NewScanner(os.Stdin)
    for s.Scan(){ u:=s.Text(); sem<-struct{}{}; wg.Add(1)
        go func(u string){defer wg.Done(); defer func(){<-sem}()
            r,e:=cl.Get(u); if e!=nil{return}; defer r.Body.Close()
            fmt.Printf("%d %s %s\\n",r.StatusCode,u,r.Header.Get("Server"))
        }(u)}
    wg.Wait()
}
```

## BUILD ENV
```bash
go mod init hunter
go build -ldflags="-s -w" -o tool tool.go   # smaller binary
GOOS=linux GOARCH=amd64 go build           # cross-compile
```

## REFERENCES
ProjectDiscovery tools (open source) → study patterns
