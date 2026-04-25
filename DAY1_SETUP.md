# DAY 1 SETUP — BugBounty-AI-System

How to deploy and start using this system.

## 1. EXTRACT THE TARBALL
```bash
tar -xzf BugBounty-AI-System.tar.gz
cd BugBounty-AI-System
```

## 2. PUSH TO YOUR REPO (OPTIONAL)
```bash
git init
git add .
git commit -m "Initial BugBounty-AI-System import"
git remote add origin git@github.com:youruser/bbai.git
git push -u origin main
```

## 3. OPTIONAL: MIRROR TO OBSIDIAN
- Open Obsidian → Open folder as vault → point at `BugBounty-AI-System/`
- All `.md` files become navigable notes with backlinks via INDEX.md.

## 4. LOAD MASTER SYSTEM PROMPT INTO YOUR LLM

### Claude (recommended)
- Open Claude → Projects → New Project → "BugBounty Hunter Oracle"
- System prompt: paste contents of `MASTER_SYSTEM_PROMPTS/claude_master_system_prompt.md`
- Project knowledge: upload all `.md` files in this repo (or just SKILL_FILES + PAYLOADS + KNOWLEDGE_BASE).
- Use Claude Sonnet/Opus 4.x.

### ChatGPT
- Settings → Custom Instructions → paste `chatgpt_master_system_prompt.md`
- For Custom GPT: upload SKILL_FILES + KNOWLEDGE_BASE as files.

### GitHub Copilot
- In your repo: create `.github/copilot-instructions.md` with contents from `github_copilot_instructions.md`.

### Local Model (Ollama / LM Studio)
- Use `local_model_system_prompt.md` as system message for Llama 3.x / Qwen / etc.
- For RAG: index `KNOWLEDGE_BASE/` + `SKILL_FILES/PAYLOADS/` with sentence-transformers + Chroma.

## 5. INSTALL THE TOOL STACK
See `SKILL_FILES/AUTOMATION/vps_setup_hunting.md` for the full install script.

Quick start:
```bash
# Install Go tools
GO111MODULE=on
for t in projectdiscovery/subfinder/v2/cmd/subfinder \\
         projectdiscovery/httpx/cmd/httpx \\
         projectdiscovery/nuclei/v3/cmd/nuclei \\
         projectdiscovery/katana/cmd/katana \\
         projectdiscovery/dnsx/cmd/dnsx \\
         projectdiscovery/naabu/v2/cmd/naabu \\
         projectdiscovery/chaos-client/cmd/chaos \\
         projectdiscovery/notify/cmd/notify \\
         lc/gau/v2/cmd/gau \\
         tomnomnom/waybackurls \\
         tomnomnom/anew \\
         tomnomnom/qsreplace \\
         hahwul/dalfox/v2 \\
         ffuf/ffuf/v2; do
  go install -v github.com/$t@latest
done

# Update Nuclei templates
nuclei -update-templates

# Wordlists
git clone https://github.com/danielmiessler/SecLists ~/wordlists/SecLists
```

## 6. CREATE TARGET WORKSPACE
```bash
mkdir -p ~/targets/<target>
cd ~/targets/<target>
# Copy CHECKLISTS/recon_passive.md and recon_active.md as your TODO
```

## 7. SET UP NOTIFICATIONS
See `SKILL_FILES/AUTOMATION/notification_telegram_discord.md`.

```bash
export TG_BOT_TOKEN=...
export TG_CHAT_ID=...
export DISCORD_WH=...
```

## 8. SCHEDULE PIPELINES
See `SKILL_FILES/AUTOMATION/recon_pipeline_automation.md` and `monitoring_*.md`.

```cron
0 3 * * * /home/hunter/scripts/recon.sh target.tld >> /var/log/recon.log 2>&1
*/30 * * * * /home/hunter/scripts/scope_watch.sh hackerone-target
```

## 9. FIRST HUNT SESSION
1. Pick a target from `MINDSET_STRATEGY/target_selection.md`.
2. Run `passive_recon.md` checklist completely (1h).
3. Run `active_recon.md` checklist (2h).
4. Triage alive set with httpx -tech-detect → manual eyeball top 50.
5. Pick highest-value endpoint per `high_value_target_prioritization.md`.
6. Apply VULNERABILITIES/WEB/* for each candidate.
7. Document findings → REPORTING/* template.

## 10. UPDATE THIS REPO
Treat it as living documentation:
- New technique you learn → add to relevant KNOWLEDGE_BASE entry.
- New tool → add to AUTOMATION or SCRIPTING.
- New chain → add to EXPLOIT_DEVELOPMENT/exploit_chain_building.md.
- Quarterly review SKILL_FILES versions → bump version number, append change log.

## REFERENCES
- All file paths above resolve relative to repo root.
- `INDEX.md` is the master navigation.
- `QUICK_REFERENCE.md` is the one-page cheat sheet.

Happy hunting.
