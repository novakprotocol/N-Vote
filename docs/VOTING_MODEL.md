# Voting Model

N-Vote v1 uses GitHub issue reactions as the public voting signal.

## Reaction weights

- `+1` = 1
- `heart` = 2
- `rocket` = 3
- `eyes` = 0.5
- `-1` = -1

Comments are not counted as votes in v1.

## Friday score

```text
score = (+1 * 1) + (heart * 2) + (rocket * 3) + (eyes * 0.5) - (-1 * 1)
```

## Tie-breakers

1. `approved-now` label
2. rocket count
3. `+1` count
4. older request first

The score is a public prioritization signal only. It does not start implementation work.
