# Owner Approval Model

Public votes do not directly trigger implementation work.

A request needs owner approval before it can become private implementation work. The public marker for that state is `status:needs-owner-approval` or `approved-now`, depending on the decision.

Approved public markers do not expose private packet contents. They only show that an owner may create or has created a separate private handoff outside the public N-Vote repository.
