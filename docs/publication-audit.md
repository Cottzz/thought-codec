# Publication Audit / 发布审计

This file records the release-readiness checks for ThoughtCodec before creating a public GitHub release.

本文记录 ThoughtCodec 在创建公开 GitHub Release 前的发布准备审计结果。

## Scope / 范围

- Repository: `Cottzz/thought-codec`
- Branch: `main`
- Target release: `v0.1.0`
- Audit date: 2026-07-07

## Checks Completed / 已完成检查

### Repository Baseline / 仓库基线

- The repository structure includes README files, license, conduct, contribution guide, security policy, catalog, docs, examples, visual assets, skills, and CI workflow.
- `main` is configured to run `Structure Check` on push and pull request.
- Local validation command: `bash scripts/validate_structure.sh`

- 仓库结构已包含 README、许可证、行为准则、贡献指南、安全说明、目录索引、文档、示例、视觉资产、Skill 和 CI 工作流。
- `main` 已配置在 push 和 pull request 时运行 `Structure Check`。
- 本地校验命令：`bash scripts/validate_structure.sh`

### Skill Content / Skill 内容

- Five preview-status skills are present.
- Every published skill includes `SKILL.md`, `SKILL.zh-CN.md`, and `examples/basic-usage.md`.
- Skill examples are generic and do not rely on private company, client, account, or contact details.
- Skill boundaries include privacy and review reminders where relevant.

- 当前包含 5 个 preview 状态的 Skill。
- 每个公开 Skill 都包含 `SKILL.md`、`SKILL.zh-CN.md` 和 `examples/basic-usage.md`。
- Skill 示例均为通用场景，不依赖私人公司、客户、账号或联系方式。
- Skill 边界中已经在相关位置包含隐私和审核提醒。

### Privacy And Secrets / 隐私与密钥

- Automated checks scan Markdown, JSON, YAML, text, SVG, Python, and shell files for common private or secret-like patterns.
- Checked patterns include emails, Google API keys, OpenAI-style keys, GitHub personal access tokens, Slack tokens, AWS access keys, and private key blocks.
- AI conversation references are summarized as reusable process notes instead of copied private transcript dumps.

- 自动检查会扫描 Markdown、JSON、YAML、文本、SVG、Python 和 shell 文件中的常见隐私或密钥模式。
- 检查模式包括邮箱、Google API key、OpenAI 风格 key、GitHub personal access token、Slack token、AWS access key 和私钥块。
- AI 对话相关内容已整理为可复用流程说明，而不是复制私人原始对话。

### Visual Assets / 视觉资产

- Final repository logo, monochrome logo, banner, diagrams, and social preview assets are stored as project assets.
- Generated brand exploration images are retained only as references and are documented as non-final assets.
- The final logo route is represented by clean SVG assets rather than generated raster text/logo output.

- 最终仓库 logo、单色 logo、banner、图表和社交预览图已作为项目资产入库。
- 生成式品牌探索图片仅作为参考保留，并已说明不是最终资产。
- 最终 logo 路线使用干净 SVG 表达，而不是直接使用带文字或渲染瑕疵的生成式位图。

### Link And Path Integrity / 链接与路径完整性

- Validation now checks local Markdown image and link targets across all Markdown files, not only root README files.
- Catalog entries are checked against actual skill folders and bilingual skill paths.
- Required GitHub templates and release notes are checked as required files.

- 校验现在会检查所有 Markdown 文件中的本地图片和链接目标，不再只检查根 README。
- 目录索引会与真实 Skill 文件夹和双语 Skill 路径互相校验。
- 必需的 GitHub 模板和发布说明也被纳入必需文件检查。

## Remaining GitHub UI Tasks / 剩余 GitHub 页面任务

These tasks live in GitHub repository settings and cannot be fully represented by committed files.

这些任务属于 GitHub 仓库页面设置，无法完全通过仓库文件表达。

- Add repository topics from `docs/en/naming-and-positioning.md`.
- Upload `assets/social-preview.png` as the GitHub social preview image.
- Create the `v0.1.0` GitHub Release after the final release-prep commit is pushed.
- Optionally pin the repository on the GitHub profile.

## Release Gate / 发布门槛

Before publishing `v0.1.0`, confirm:

- `bash scripts/validate_structure.sh` passes.
- GitHub Actions passes on the final pushed commit.
- GitHub About, topics, and social preview are reviewed.
- Release notes in `docs/release-notes/v0.1.0.md` match the final commit.

发布 `v0.1.0` 前确认：

- `bash scripts/validate_structure.sh` 通过。
- 最终推送提交上的 GitHub Actions 通过。
- GitHub About、topics 和 social preview 已复核。
- `docs/release-notes/v0.1.0.md` 与最终提交内容一致。
