# Public / Private Boundary

N-Vote is a public request and voting board candidate for N-Stack/N-Suite.

## Public surface

Public data may include:

- public GitHub issue numbers, titles, labels, states, dates, and URLs from this repository;
- public reaction counts;
- public area slugs and display names;
- public request kind metadata for application requests;
- public status markers such as `status:submitted`, `status:triage`, `status:needs-owner-approval`, `status:approved-public`, and `approved-now`.

## Application-request public fields

Application-request issues may include:

- request kind: app, web app, game, overlay, docs, or other;
- target family: N-Suite, N-Idea, N-G, N-A candidate, N-Vote, docs, or other;
- requested launch surface: CLI, GUI, web, GitHub Pages, or unknown;
- public summary, user value, and public-safe notes.

## Private boundary

N-Vote public issues and votes are never implementation input by themselves.

A request can become private implementation work only after owner approval and a separate private handoff.

N-Vote must not expose private repo internals, secrets, local personal paths, private receipts, private branch names, customer or private data, or private implementation plans.

## Not a control surface

N-Vote is not a private implementation queue, not a runner trigger, not a private repo browser, not a secret store, and not a production-control surface.
