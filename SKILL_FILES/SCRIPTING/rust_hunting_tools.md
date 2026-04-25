# SKILL: Rust Hunting Tools
## Version: 1.0 | Domain: scripting

---

## CONCURRENT HTTP PROBE
```rust
// Cargo.toml: tokio = { version = "1", features = ["full"] }, reqwest = { version = "0.12", features = ["rustls-tls"] }, futures = "0.3"
use std::io::{self, BufRead}; use futures::stream::{StreamExt, FuturesUnordered}; use reqwest::Client;

#[tokio::main]
async fn main() {
    let client = Client::builder().danger_accept_invalid_certs(true).build().unwrap();
    let urls: Vec<String> = io::stdin().lock().lines().filter_map(|l| l.ok()).collect();
    let mut futs = FuturesUnordered::new();
    for u in urls {
        let c = client.clone();
        futs.push(async move {
            match c.get(&u).send().await {
                Ok(r) => println!("{} {}", r.status().as_u16(), u),
                Err(_) => {}
            }
        });
        if futs.len() > 50 { futs.next().await; }
    }
    while futs.next().await.is_some() {}
}
```

## WHEN TO USE RUST
- CPU-bound (regex, parsing, crypto)
- Need single static binary
- Memory-safe long-running daemon
- Speed beats Go on tight loops

## EXAMPLE TOOLS WRITTEN IN RUST
- noseyparker (secrets)
- feroxbuster (content discovery)
- rustscan (port scanner)

## REFERENCES
tokio.rs, reqwest docs
