# N-Vote

N-Vote is a public request and voting board candidate for N-Stack/N-Suite.

It uses GitHub Issues as the public request intake surface, GitHub issue reactions as the voting signal, public JSON data files as the read model, and a static GitHub Pages site as the public web interface.

## Public boundary

N-Vote is public. Do not paste private repo internals, secrets, tokens, local personal paths, private receipts, private branch names, or implementation plans into issues.

Public N-Vote requests and votes are never runner input. Owner approval is required before any request becomes private implementation work.

## Intake and voting

- Submit requests through GitHub issue forms.
- Vote with issue reactions.
- Reaction scores: `+1 = 1`, `heart = 2`, `rocket = 3`, `eyes = 0.5`, `-1 = -1`.
- Comments are not counted as votes in v1.

## Web site

Static site source lives under `site/`. Public data lives under `data/`.

GitHub Pages is intended to deploy through GitHub Actions. Pages settings still require repo-level GitHub Pages Source: GitHub Actions when this repository has not yet been configured.

## Validation

```bash
python scripts/check_public_boundary.py
python scripts/check_data_contract.py
python scripts/quality_gate.py
git diff --check
```

## Claim boundary

Allowed claim: N-Vote is a public request and voting board candidate for N-Stack/N-Suite.

Not claimed: production-ready, production-grade, hosted-CI-green, formal-audit, runner-ready, fully automated implementation, private work execution, or complete.
