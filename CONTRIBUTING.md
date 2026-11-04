# Contributing

Thanks for your interest in improving Python Animation Video Lab.

## Ways to contribute

- Fix bugs in rendering scripts
- Improve animation quality or performance
- Add new reusable effects
- Improve docs and examples
- Add tests for helper logic

## Local setup

1. Fork and clone the repository
2. Create a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run scripts and validate outputs in output/

## Branch and commit style

- Create focused branches per task
- Keep commits small and descriptive
- Commit message style:

```text
<type>: <specific detail>
```

Examples:

- update: improve wave scene colour blending
- fix: handle ffmpeg missing path more clearly
- refactor: split scene rendering helpers

## Pull request checklist

- Explain the problem and solution clearly
- Include before/after behaviour notes
- Keep README/docs updated if behaviour changes
- Avoid committing generated media in output/

## Code style notes

- Keep functions focused and readable
- Prefer explicit variable names for timeline math
- Add comments only when logic is non-obvious
- Preserve existing script behaviour unless PR scope requires changes

## Suggested contribution ideas

- Add scene transition helpers
- Add text animation presets
- Add platform output presets (9:16, 1:1, 16:9)
- Add CLI arguments for duration/resolution/fps

## Using AI

AI tools are welcome within my [AI policy](https://github.com/zaccesss/ai-policy), also [on my site](https://isaacadjei.me/ai-policy). **Every pull request must say how AI was used, even when the answer is None.** Write your own issue and pull request titles and descriptions, understand everything you submit and test it before you open it.
