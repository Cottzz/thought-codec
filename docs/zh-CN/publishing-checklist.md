# 发布清单

在 GitHub 上公开发布 ThoughtCodec 前，使用本清单检查。

## 项目身份

- [ ] 仓库名为 `thought-codec`，或已经确认其他最终名称。
- [ ] GitHub About 描述使用 `docs/zh-CN/naming-and-positioning.md` 中的一句话介绍。
- [ ] 已添加 Topics。
- [ ] Social preview 使用 `assets/social-preview.png`。

## 双语内容

- [ ] `README.md` 和 `README.zh-CN.md` 都是最新版本。
- [ ] 每个正式 Skill 都有 `SKILL.md` 和 `SKILL.zh-CN.md`。
- [ ] `catalog/skills.json` 中包含英文和中文描述。
- [ ] Issue 和 PR 模板能让中英文贡献者理解。

## 视觉资产

- [ ] Logo 已存在。
- [ ] README Banner 已存在。
- [ ] 系统架构图已存在。
- [ ] 解压/压缩流程图已存在。
- [ ] 智能体闭环图已存在。
- [ ] 所有图片链接都能在 GitHub Markdown 中渲染。

## 安全与隐私

- [ ] 没有私人邮箱、token、密钥或账号细节。
- [ ] Gemini 或其他 AI 对话轨迹已清理为可复用规则，没有作为私人原始对话大段复制。
- [ ] 示例使用虚构或通用数据。
- [ ] 许可证已确认。

## 校验

运行：

```bash
bash scripts/validate_structure.sh
```

提交前检查 Git diff。
