# Public / Private Boundary

N-Vote is a public request and voting board candidate for N-Stack/N-Suite.

## Public surface

Public data may include:

- public GitHub issue numbers, titles, labels, states, dates, and URLs from this repository;
- public reaction counts;
- public area slugs and display names;
- public status markers such as `status:submitted`, `status:triage`, `status:needs-owner-approval`, `status:approved-public`, and `approved-now`.

## Private boundary

N-Vote public issues and votes are never implementation input by themselves.

A request can become private implementation work only after owner approval and a separate private handoff. Public N-Vote output can be copied into a private recon packet by an owner-approved action only.

Runner may only read private approved packets from:

- N-Idea recon records with a build decision;
- N-Suite private approved queue;
- an approved execution receipt or plan.

N-Vote must not expose private repo internals, secrets, local paths, private receipts, or private implementation plans.

## Not a control surface

N-Vote is not a private implementation queue, not a runner trigger, not a private repo browser, not a secret store, and not a production-control surface.
