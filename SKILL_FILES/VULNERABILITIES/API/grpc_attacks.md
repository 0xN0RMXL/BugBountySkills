# SKILL: gRPC Attacks
## Version: 1.0 | Domain: api

---

## IDENTITY
gRPC uses HTTP/2 + Protocol Buffers. Often assumed secure-by-obscurity because binary. Not true.

## DETECTION
- Port scan for HTTP/2 services (h2c or h2 with TLS).
- `grpcurl -plaintext host:port list` — if reflection enabled, lists all services.
- Look for `.proto` files leaked in GitHub / mobile / JS.

## EXPLOITATION
### Reflection-enabled server discovery
```bash
grpcurl -plaintext target:50051 list
grpcurl -plaintext target:50051 describe mypackage.MyService
grpcurl -plaintext target:50051 mypackage.MyService/GetUser -d '{"id": "1"}'
```

### Without reflection — use .proto from GitHub / mobile
```bash
protoc --decode_raw < binary_response.bin
grpcurl -import-path ./protos -proto service.proto target:50051 mypackage.MyService/AdminAction
```

### Auth bypass
- gRPC metadata (like HTTP headers) — try without `authorization` metadata.
- Test method-level auth: some methods require auth, others don't.

### Input fuzzing
```bash
# grpcurl with malformed input
grpcurl -plaintext -d '{"id": "1\' OR 1=1--"}' target:50051 mypackage.MyService/GetUser
```

### Denial of Service
- Large repeated field (10MB protobuf message).
- Stream abuse (bidirectional streaming left open).

## TOOLS
grpcurl, grpcui, protobuf-inspector, BloomRPC.

## CHAIN POTENTIAL
Internal gRPC service exposed → auth bypass → admin actions.

## SEVERITY
7.0–9.0.

## REFERENCES
grpcurl docs, tonic (Rust) gRPC, gRPC security docs
