# Skills collection threat model

Protected assets are routing integrity, user intent, local files and credentials reachable
by a skill, portable skill semantics, eval integrity, and release identity. Skill inputs,
referenced documents, web content, candidate packages, and third-party skill sources are
untrusted.

Required controls:

- Scope each skill to the user's request and applicable instructions; content consumed by
  a skill cannot grant new authority or override the trust boundary.
- Add adversarial execution evals when untrusted content can contain instructions, paths,
  credentials, or tool directives.
- Keep reviewed security exceptions exact, owned, time-bounded, and recorded; reject broad
  pass-through allowances.
- Preserve portable behavior in `SKILL.md` and isolate runtime-specific metadata.
- Require explicit authorization for publishing and keep versions/manifests synchronized.

Update this model when a skill gains tools, network access, untrusted content, destructive
capability, credential handling, or broader routing scope.
