# SKILL: Docker Hunting Environment
## Version: 1.0 | Domain: automation

---

## ALL-IN-ONE DOCKERFILE
```dockerfile
FROM ubuntu:22.04
RUN apt update && apt install -y \
    git curl wget jq python3 python3-pip golang nodejs npm unzip ripgrep nmap masscan
ENV GOPATH=/root/go PATH=/root/go/bin:$PATH
RUN go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && \
    go install github.com/projectdiscovery/httpx/cmd/httpx@latest && \
    go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest && \
    go install github.com/projectdiscovery/katana/cmd/katana@latest && \
    go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest && \
    go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest && \
    go install github.com/lc/gau/v2/cmd/gau@latest && \
    go install github.com/hahwul/dalfox/v2@latest && \
    go install github.com/ffuf/ffuf/v2@latest
RUN pip3 install sqlmap arjun trufflehog3 apkleaks dirsearch
RUN mkdir -p /root/wordlists && \
    git clone --depth 1 https://github.com/danielmiessler/SecLists /root/wordlists/SecLists
ENTRYPOINT ["/bin/bash"]
```

```bash
docker build -t hunter .
docker run -it --rm -v $PWD:/work -w /work hunter
```

## DOCKER-COMPOSE
```yaml
services:
  hunter:
    build: .
    volumes:
      - .:/work
      - ~/wordlists:/root/wordlists
    networks: [bbnet]
  burp:
    image: portswigger/burp-pro
    networks: [bbnet]
networks:
  bbnet:
```

## REFERENCES
projectdiscovery/pdtm
