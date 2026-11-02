# LinkedIn Human Writer Claude Skill

A Claude Code skill for writing LinkedIn posts that sound like a real person. It focuses on first-hand work experiences and informed reactions to industry news, using plain English and a distinctive personal voice.

## What's included

- **[`linkedin-post-writer/SKILL.md`](linkedin-post-writer/SKILL.md)** — the `linkedin-post-writer` skill instructions.
- **[`linkedin-post-writer/scripts/check_post.py`](linkedin-post-writer/scripts/check_post.py)** — a lightweight Python checker for common AI-writing patterns, repetitive structures, formatting issues and LinkedIn post constraints.
- **[`linkedin-post-writer/voice-samples.md`](linkedin-post-writer/voice-samples.md)** — a template for adding real writing samples so Claude can follow the writer's natural habits.

## Install with Claude Code

Copy the `linkedin-post-writer` folder into your project's `.claude/skills/` directory:

```text
your-project/
└── .claude/
    └── skills/
        └── linkedin-post-writer/
            ├── SKILL.md
            ├── voice-samples.md
            └── scripts/
                └── check_post.py
```

The skill can then be used when drafting, rewriting, fixing or checking a LinkedIn post. It covers experience-led posts and reactions to industry news. It is not intended for cold emails or LinkedIn direct messages.

## Run the post checker

From the skill directory:

```bash
python3 scripts/check_post.py post.txt
```

Check several drafts together to compare openings and endings:

```bash
python3 scripts/check_post.py monday.txt wednesday.txt friday.txt
```

On macOS, check the clipboard:

```bash
pbpaste | python3 scripts/check_post.py -
```

The checker reports hard-rule failures and softer warnings. Passing the checker does not guarantee a good post; read the draft aloud and verify that every fact is accurate.

## Personalize the voice

Add 3–5 real writing samples to `linkedin-post-writer/voice-samples.md`. The skill uses them to learn writing habits, not to reuse sentences.

## License

No license file is included yet. All rights remain with the repository owner unless a license is added.
