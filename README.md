# AI-First Engineering Standards 🏎️🛡️

**Governing the speed of AI with the precision of Engineering.**

In the era of **AI-First development**, speed is no longer the bottleneck—**governance is**. While AI models can generate hundreds of lines of code per minute, without the proper guardrails, technical debt and security risks can accumulate at the same velocity.

> *"In Formula 1, going faster without appropriate guardrails is a recipe for a catastrophic crash. This repository aims to be the steering wheel that guides the AI engine."*


### Core Principles:
* **Governance by Design:** Don't just ask the AI to "be good." Enforce your architectural patterns.
* **Tool Agnostic:** Define rules once in `src_rules/` and deploy them to **Cursor, GitHub Copilot, or Claude**.
* **Scale:** Ensure your AI assistants follow modern standards automatically.
---

## 🏗️ Repository Structure

* **`src_rules/`**: Contains pure Markdown files with specific engineering standards.
* **`templates/`**: Configuration templates for different AI tools (`.mdc` for Cursor, `.txt` for Claude, etc.).
* **`generate_rules.py`**: This Python script merges your rules with templates to generate ready-to-use config files.
* **`output/`**: The final artifacts, organized by tool, ready to be copied into your project.

---

## Current Guardrails included:

**Git Discipline** — Verification steps & Conventional Commits.

**Angular Modern Excellence** — Signals, Resource API, Standalone.

**React & Next.js** — Hydration safety (no browser APIs during render), stable hook references with `useCallback`, monorepo `tsconfig` isolation.

**AWS Serverless (Lambda, DynamoDB, SAM)** — CORS headers on every response path, DynamoDB TTL as Unix epoch Number, correct SAM template structure for TTL.

**Security** — Never include credentials, secrets, or sensitive data in code, configuration files, or commit history. AI tools operate on what you give them — review every diff before committing, especially when working under time pressure.


---


## 🚀 How to Use & Collaborate

### 1. Fork & Customize
Every project and team is unique. I encourage you to **fork this repository**. 
* Add your own project-specific rules to `src_rules/`.
* Customize the templates to fit your team's stack.
* Maintain your own fork as your team's internal governance center.

### 2. Standardize
Run the generator to stay up-to-date.

**Generate all rules:**
```bash
python3 generate_rules.py
```

**Generate a specific rule only:**
```bash
python3 generate_rules.py react-next
```

> **Note:** Use `python3` on Linux/macOS. On Windows, use `python` or `py` depending on your installation.

The generator produces ready-to-use artifacts for three AI tools:

| Tool | Output path | How to use |
| --- | --- | --- |
| Cursor | `output/.cursor/rules/*.mdc` | Copy `.cursor/` to your project root |
| Claude Code | `output/CLAUDE.md` | Copy `CLAUDE.md` to your project root |
| GitHub Copilot | `output/.github/copilot-instructions.md` | Copy `.github/` to your project root |

### 3. Collaborate

PRs with rules that proved useful in your projects are welcome 🫶
