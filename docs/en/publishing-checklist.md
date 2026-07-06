# Publishing Checklist

Use this checklist before publishing ThoughtCodec on GitHub.

## Identity

- [ ] Repository name is `thought-codec` or another confirmed final name.
- [ ] GitHub About description uses the one-sentence description from `docs/en/naming-and-positioning.md`.
- [ ] Topics are added.
- [ ] Social preview image uses `assets/social-preview.png`.

## Bilingual Content

- [ ] `README.md` and `README.zh-CN.md` are both current.
- [ ] Every published skill has `SKILL.md` and `SKILL.zh-CN.md`.
- [ ] English and Chinese descriptions exist in `catalog/skills.json`.
- [ ] Issue and pull request templates are understandable for both English and Chinese contributors.

## Visual Assets

- [ ] Logo exists.
- [ ] README banner exists.
- [ ] Architecture diagram exists.
- [ ] Decompression/compression diagram exists.
- [ ] Agentic loop diagram exists.
- [ ] All image links render in GitHub Markdown.

## Safety And Privacy

- [ ] No private email addresses, tokens, secrets, or account details are present.
- [ ] Gemini or other AI conversation traces are cleaned into reusable rules, not copied as private transcript dumps.
- [ ] Examples use fictional or generic data.
- [ ] License is final.

## Validation

Run:

```bash
bash scripts/validate_structure.sh
```

Review the Git diff before committing.
