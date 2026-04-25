# SKILL: Solidity / Smart Contract Review
## Version: 1.0 | Domain: scr (web3)

---

## VULNERABILITY CLASSES
- **Reentrancy** — external call before state update. Mitigation: checks-effects-interactions, ReentrancyGuard.
- **Integer overflow/underflow** — Solidity <0.8 silent wrap. Mitigation: SafeMath or 0.8+.
- **Access control** — missing `onlyOwner` / role check on critical functions.
- **tx.origin auth** — phishing risk; use msg.sender.
- **Unchecked low-level calls** — `(bool ok,) = addr.call(...)` without checking ok.
- **Front-running / MEV** — order-dependent operations on public mempool.
- **Block.timestamp / block.number as randomness** — miner-manipulable.
- **Delegatecall to untrusted contract** — full storage takeover.
- **Self-destruct from arbitrary caller** — drain funds.
- **Price oracle manipulation** — flash loan + Uniswap spot price.
- **Signature replay** — missing nonce or chain-id in EIP-712.
- **Initialization** — `initialize()` callable by anyone in proxy patterns.
- **Storage collision** in upgradeable proxies.
- **Phishing approval** — unlimited ERC20 approve to malicious contract.

## TOOLS
- Slither (Trail of Bits)
- Mythril
- Echidna (fuzzer)
- Manticore (symbolic execution)
- Foundry's `forge test --gas-report`

```bash
slither contracts/
myth analyze contracts/Token.sol
echidna-test contracts/Token.sol --contract Token
```

## REFERENCES
SWC Registry • Trail of Bits Building Secure Contracts • Immunefi reports
