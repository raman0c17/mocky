# Claude skill

Mocky ships a [Claude skill](https://github.com/raman0c17/mocky/blob/master/skills/mocky/SKILL.md)
so Claude can scaffold, refine, and render decks for you. It's a community
give-back: anyone using Claude can drop the skill in and get Mocky's idea→deck
flow.

## What the skill does

- Recognizes requests like “make a presentation about X” or “turn this Markdown into PowerPoint.”
- Chooses a workflow: scaffold from an **idea**, or convert existing **Markdown**.
- Renders a real `.pptx` with the cross-platform engine.

## Where it lives

```
skills/
└── mocky/
    └── SKILL.md
```

## Using it

Point your Claude environment at the `skills/mocky/SKILL.md` file (or copy it into
your skills directory). The skill's front matter describes when Claude should
trigger it; the body documents the slide model and both workflows.

!!! info "Other coding agents"
    The repository also ships an `AGENTS.md` at its root so tools like Codex and
    Cursor can navigate the codebase.
