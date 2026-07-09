# Overlay Integration Plan

N-Suite overlay reads N-Vote public JSON and displays public-safe data only.

## Read sources

- `data/areas.json`
- `data/requests.json`
- `data/votes.json`
- `data/friday-top5.json`
- `data/approved-now.json`
- `data/public-roadmap.json`

## Overlay display

The overlay can display:

- areas;
- public requests;
- public reaction vote counts;
- Friday top 5 overall and per area;
- approved-now public markers.

## Button boundary

Overlay buttons are open, copy, or display only. They must not start implementation work.

Creating a private recon packet requires explicit owner approval. N-Vote panel actions must not trigger runner execution and must not mutate private repositories.
