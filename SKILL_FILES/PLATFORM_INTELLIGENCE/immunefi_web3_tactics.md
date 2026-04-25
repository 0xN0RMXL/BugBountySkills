# SKILL: Immunefi (Web3) Tactics
## Version: 1.0 | Domain: platform-intel

---

## DOMAIN
Smart contracts (Solidity / Vyper / Move / Cairo / Rust on Solana), bridges, DEXes, lending protocols, NFT contracts.

## CRITICAL CATEGORIES (highest payouts)
- Direct theft of any user funds (locked or in-flight) — usually $1M-$10M
- Permanent freezing of funds
- Insolvency
- Governance hijack

## METHODOLOGY
1. Read the protocol whitepaper + docs to understand intended flow.
2. Read on-chain code (Etherscan / contract address).
3. Map all external callable functions, especially payable / state-changing.
4. Trace all flows that move tokens / native asset.
5. Look for: reentrancy, integer over/underflow (pre-0.8 or unchecked blocks), access control gaps, oracle manipulation, signature replay, init reentry, proxy storage clash, flash loan attacks.

## TOOLS
- Slither, Mythril, Echidna, Foundry (forge test, forge fuzz)
- Tenderly for forking + simulating
- Immunefi PoC submission template requires fork-based reproducible test

## REPORT
- Must include: vulnerability description, attack scenario, full PoC (Foundry test or hardhat script forking mainnet), recommendation.
- Severity uses Immunefi-specific scale (Critical / High / Medium / Low).

## CRITICAL TIPS
- Check for `delegatecall` to user-controlled address.
- Check signatures against EIP-712 domain separator chain ID + nonce.
- Check Uniswap V2/V3 spot price as oracle (manipulable by flash loan).
- Check init function callable post-deployment.
- Check storage slot collisions in upgradeable proxy patterns.

## REFERENCES
immunefi.com, SWC Registry, Trail of Bits Building Secure Contracts
