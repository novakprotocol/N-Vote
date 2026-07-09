# AGENTS.md

## Read first

1. README.md
2. COMMANDS.md
3. docs/PUBLIC_PRIVATE_BOUNDARY.md
4. docs/VOTING_MODEL.md
5. docs/OWNER_APPROVAL.md
6. docs/OVERLAY_INTEGRATION.md

## Rules

- Keep N-Vote public-safe.
- Do not expose secrets, tokens, private repo internals, private branch names, private receipts, or local personal paths.
- Do not make public votes trigger runner execution.
- Do not create private implementation work without owner approval.
- Keep scripts Python standard library only.
- Keep the web interface static and GitHub Pages-compatible.
- Do not claim production-ready, production-grade, hosted-CI-green, formal-audit, runner-ready, private-work execution, or complete status without evidence.

## Checks

```bash
python scripts/check_public_boundary.py
python scripts/check_data_contract.py
python scripts/quality_gate.py
git diff --check
```
