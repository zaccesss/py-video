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

- update: improve wave scene color blending
- fix: handle ffmpeg missing path more clearly
- refacr: split scene rendering helpers

## Pull request checklist

- Explain the problem and solution clearly
- Include before/after behavior notes
- Keep README/docs updated if behavior changes
- Avoid committing generated media in output/

## Code style notes

- Keep functions focused and readable
- Prefer explicit variable names for timeline math
- Add comments only when logic is non-obvious
- Preserve existing script behavior unless PR scope requires changes

## Suggested contribution ideas

- Add scene transition helpers
- Add text animation presets
- Add platform output presets (9:16, 1:1, 16:9)
- Add CLI arguments for duration/resolution/fps
