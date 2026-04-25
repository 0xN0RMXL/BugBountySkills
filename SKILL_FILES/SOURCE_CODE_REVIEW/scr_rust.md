# SKILL: Rust Source Code Review
## Version: 1.0 | Domain: scr

---

## PATTERNS
- `unsafe { ... }` — review every block; common UB sources.
- `std::mem::transmute` — type pun; UB if invalid.
- `Box::from_raw` / `Box::into_raw` — manual lifetime.
- `unwrap()` / `expect()` in HTTP handlers — DoS via panic.
- Integer overflow in `usize` arithmetic (silent in release; panic in debug). Use `checked_add` / `saturating_add`.
- `format!` / `println!` with user-controlled format string — use `"{}", input` not `input` as format.
- `process::Command::new("sh").arg("-c").arg(user)` — shell injection (rare in Rust idiomatic code).
- `serde_json` from untrusted source — type confusion via tagged enums.
- `cargo audit` for known dep CVEs.

## WEB FRAMEWORKS
- **Actix-Web** — `web::Json<T>` deserialization; check size limits.
- **Axum** — same.
- **Rocket** — `Form<T>` similar.
- SQLx — uses parameterized queries; raw query via `query!` is compile-time checked.
- Diesel — generally safe; raw `sql_query` is dangerous.

## TOOLS
```bash
cargo clippy -- -D warnings
cargo audit
cargo geiger    # find unsafe usage
semgrep --config=p/rust src/
```

## REFERENCES
RustSec advisory DB
