# Commands

## Validate public boundary

```bash
python scripts/check_public_boundary.py
```

## Validate public data contract

```bash
python scripts/check_data_contract.py
```

## Quality gate

```bash
python scripts/quality_gate.py
git diff --check
```

## Build public data locally

```bash
python scripts/build_public_data.py
python scripts/tally_votes.py
```

Local runs without `GITHUB_TOKEN` use public skeleton data only. GitHub Actions may use the built-in `GITHUB_TOKEN` to read public issues and write public JSON.
