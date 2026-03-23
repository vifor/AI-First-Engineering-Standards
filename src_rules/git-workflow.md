
# Workflow & Git Discipline

You must follow these operational rules to ensure a clean project history:

## 1. No Automatic Commits
- **STRICTLY PROHIBITED:** Never execute `git commit` or `git push` automatically after generating code.
- Always wait for the user to manually test and verify the changes in the browser/terminal.

## 2. Verification Step
- After applying changes, ask the user: "Would you like to review these changes or run tests before committing?"
- Suggest specific manual tests if the changes are complex.

## 3. Security Check Before Commit Review

- **MANDATORY:** Before presenting a diff or asking the user to review changes, scan the modified files for sensitive information:
  - API keys, tokens, passwords, secrets
  - Hardcoded credentials or connection strings
  - Private keys or certificates
- **If sensitive data is detected:** Do not proceed. Alert the user immediately and suggest the correct approach:
  - Use `.env` files for local secrets (ensure `.env` is in `.gitignore`)
  - Use environment variables injected at runtime for deployed environments
  - Use a secrets manager (AWS Secrets Manager, HashiCorp Vault, etc.) for production credentials
- **Why:** AI tools operate on what the engineer provides. A distracted review is all it takes to commit credentials to a public repository — an incident that requires secret rotation and history rewriting to resolve.

## 4. Commit Standards
- If the user explicitly asks you to commit, use the **Conventional Commits** format:
  - `feat:` for new features (e.g., `feat: add sorting to plants table`)
  - `fix:` for bug fixes
  - `docs:`, `style:`, `refactor:`, `test:`, `chore:` as appropriate.