# SKILL: VPS Setup for Bug Hunting
## Version: 1.0 | Domain: automation

---

## RECOMMENDED SPECS
- 2 vCPU, 4-8GB RAM, 60GB SSD (for moderate scope)
- Ubuntu 22.04 LTS
- DigitalOcean / Linode / Hetzner / Vultr ($5-20/month)

## INSTALL SCRIPT
```bash
#!/usr/bin/env bash
set -e
sudo apt update && sudo apt install -y \
  build-essential git curl wget jq python3 python3-pip golang nodejs npm \
  unzip tmux htop ripgrep fzf nmap masscan dnsutils whois \
  libpcap-dev libldns-dev

# Go tools
GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
go install -v github.com/projectdiscovery/katana/cmd/katana@latest
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest
go install -v github.com/projectdiscovery/notify/cmd/notify@latest
go install -v github.com/projectdiscovery/alterx/cmd/alterx@latest
go install -v github.com/lc/gau/v2/cmd/gau@latest
go install -v github.com/tomnomnom/waybackurls@latest
go install -v github.com/tomnomnom/assetfinder@latest
go install -v github.com/tomnomnom/qsreplace@latest
go install -v github.com/tomnomnom/unfurl@latest
go install -v github.com/d3mondev/puredns/v2@latest
go install -v github.com/owasp-amass/amass/v4/...@master
go install -v github.com/hahwul/dalfox/v2@latest
go install -v github.com/ffuf/ffuf/v2@latest
go install -v github.com/OJ/gobuster/v3@latest
go install -v github.com/sensepost/gowitness@latest

# Python tools
pip3 install --user trufflehog3 sqlmap arjun apkleaks dirsearch

# Misc
sudo wget https://github.com/danielmiessler/SecLists/archive/master.tar.gz -O /tmp/seclists.tar.gz
mkdir -p ~/wordlists && tar -xzf /tmp/seclists.tar.gz -C ~/wordlists/

# Nuclei templates
nuclei -ut

# Resolvers
wget https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt -O ~/.config/resolvers.txt
```

## PERSISTENCE
- All output to /home/hunter/results/$DATE/
- Daily backup to S3 / object storage
- Pin tools to specific versions in /opt/tools/

## SECURITY
- SSH key only, disable password auth
- ufw allow OpenSSH; deny all else
- fail2ban
- unattended-upgrades for kernel

## REFERENCES
projectdiscovery.io, Tomnomnom tools
