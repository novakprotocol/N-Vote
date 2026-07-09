# Request Intake

GitHub Issues are the public request intake surface for N-Vote.

Use the provided issue forms:

- Feature request
- Application request
- Bug report
- Vote nomination

## Application requests

Application requests are public-safe requests for new apps or app-like work. Supported public request kinds are:

- `app`
- `web app`
- `game`
- `overlay`
- `docs`
- `other`

Application requests collect only public context: request kind, target family, requested launch surface, summary, user value, and public-safe constraints or notes.

Allowed target family values are:

- `N-Suite`
- `N-Idea`
- `N-G`
- `N-A candidate`
- `N-Vote`
- `docs`
- `other`

Allowed launch surface values are:

- `CLI`
- `GUI`
- `web`
- `GitHub Pages`
- `unknown`

## Routing

Application requests appear in public request data and Friday top-5 ranking like other requests. The `approved-now` marker remains public context only and still requires owner approval before any private implementation work.

Do not include private repo internals, secrets, tokens, local personal paths, private receipts, private branch names, customer or private data, or implementation instructions in public issues.
