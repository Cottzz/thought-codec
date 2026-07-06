# Skills / Skill 目录

This folder contains the ThoughtCodec skill library.

本目录存放 ThoughtCodec 的 Skill 库。

## Published Skills / 已发布 Skill

- [Architecture Scaffolding](architecture-scaffolding/SKILL.md) / [架构级脚手架生成器](architecture-scaffolding/SKILL.zh-CN.md)
- [SOP Instantiation](sop-instantiation/SKILL.md) / [标准作业程序实例化引擎](sop-instantiation/SKILL.zh-CN.md)
- [Rule And Prompt Optimizer](rule-prompt-optimizer/SKILL.md) / [规则与提示词迭代器](rule-prompt-optimizer/SKILL.zh-CN.md)
- [Code Abstraction And Encapsulation](code-abstraction-encapsulation/SKILL.md) / [代码与组件重构器](code-abstraction-encapsulation/SKILL.zh-CN.md)
- [Personal Methodology Engine](personal-methodology-engine/SKILL.md) / [个人方法论引擎](personal-methodology-engine/SKILL.zh-CN.md)

## Folder Pattern / 文件夹模式

```text
skills/<skill-id>/
|-- SKILL.md
|-- SKILL.zh-CN.md
|-- assets/
|-- examples/
`-- references/
```

## Add A Skill / 新增 Skill

Copy the template:

复制模板：

```bash
cp -R skills/_template skills/<skill-id>
```

Then update both language files and add the new skill to `catalog/skills.json`.

然后更新两个语言版本，并将新 Skill 加入 `catalog/skills.json`。
