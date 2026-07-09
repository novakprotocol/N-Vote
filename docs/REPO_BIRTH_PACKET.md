# Repo Birth Packet

## Repo Name

N-Vote

## Owner Decision

Create a public GitHub-native request and voting web app for N-Stack/N-Suite.

## Repo Class

Public web app, GitHub Pages static site, GitHub Issues intake surface, public voting board, public roadmap display, and N-Suite overlay read source.

## N-Stack Route

New public N-* candidate with explicit public/private boundary. This is not a private implementation queue.

## Product Reconnaissance

N-Vote solves public request intake and prioritization for N-Stack/N-Suite without exposing private implementation details or triggering execution.

## Required Files

This repository includes issue forms, data contracts, workflows, scripts, site files, app contracts, and continuity docs.

## Commands To Run

```bash
python scripts/check_public_boundary.py
python scripts/check_data_contract.py
python scripts/quality_gate.py
git diff --check
```

## Claim Boundaries

N-Vote is a public request and voting board candidate for N-Stack/N-Suite. It is not claimed production-ready, production-grade, hosted-CI-green, formal-audit, complete, runner-ready, fully automated implementation, or private work execution.

## Next Safe Action

Review the draft PR and enable GitHub Pages Source: GitHub Actions for this repository only.
