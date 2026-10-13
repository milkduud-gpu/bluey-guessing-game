---
name: commit-push
description: Stage current changes, write a commit message, and push to origin. Use when the user asks to commit and push, save changes to GitHub, or run /commit-push.
disable-model-invocation: true
---

Commit the current changes and push them to `origin`.

1. Run `git status` and `git diff` to see what changed. If there is nothing to commit, say so and stop.
2. Stage the changes with `git add`. Do not stage files that look like secrets (`.env`, tokens, credentials); warn the user instead.
3. Write a short, imperative commit message that describes what changed and why. Match the style of `git log --oneline -5`.
4. Commit, then push the current branch with `git push` (use `-u origin <branch>` if it has no upstream).
5. Report the commit hash and the repository URL.

Never force-push or rewrite history unless the user explicitly asks.
