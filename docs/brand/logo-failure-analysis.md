# Logo Failure Analysis / Logo 失败复盘

This note records why earlier ThoughtCodec logo attempts were not ready for an open-source repository identity. It should be used before accepting any new generated image or SVG route.

本文记录 ThoughtCodec 之前几轮 logo 方案未能达到开源仓库标识要求的原因。后续任何生图或 SVG 路线进入定稿前，都应先通过这里的检查。

## Failure Patterns / 失败模式

### 1. Poster Instead Of Mark / 海报感强于标识

Some references worked as presentation images but not as repository assets. Concrete backgrounds, dramatic lighting, large wordmarks, subtitles, and decorative objects made the result look like a brand poster instead of a reusable software mark.

部分参考图适合作为展示海报，但不适合作为仓库资产。水泥墙背景、戏剧化光影、大字标、说明副标题和装饰元素，会让结果偏向品牌海报，而不是可复用的软件标识。

### 2. Too Much Micro-Structure / 细节结构过密

Dense trees, infinity loops, arrow systems, and internal meshes can look meaningful at large size, but they collapse at 32px and 16px. The final mark must survive favicon usage.

密集树状结构、无限循环、箭头系统和内部网格在大图中可能显得有意义，但缩小到 32px 和 16px 时会坍缩。最终标识必须能承担 favicon 场景。

### 3. Styling Before Identity / 风格先于识别

Gradients, glow, bevels, shadows, and rendered textures can hide weak geometry. The mark must work first as a single-color silhouette, then receive color.

渐变、高光、浮雕、阴影和渲染质感容易掩盖几何本身的问题。标识必须先作为单色剪影成立，再考虑颜色。

### 4. Literal Or Generic AI Symbols / 字面化或通用 AI 符号

Brain maps, gears, chat bubbles, code brackets, sparkle marks, and literal flowcharts make the identity feel generic. ThoughtCodec needs an abstract infrastructure mark, not an illustration of AI or coding.

脑图、齿轮、聊天气泡、代码括号、星光符号和字面流程图会让项目显得通用。ThoughtCodec 需要的是抽象的软件基础设施标识，而不是 AI 或代码插画。

### 5. Name And Message Drift / 名称与信息漂移

The Gemini reference used `METHODOX`, but this repository is currently named `ThoughtCodec`. A generated image that includes the wrong name, tagline, or embedded text cannot become the repository logo.

Gemini 参考图使用了 `METHODOX`，但当前仓库名称是 `ThoughtCodec`。任何包含错误名称、副标题或内嵌文字的生图，都不能直接成为仓库 logo。

### 6. Generated Image Is Not Final Asset / 生图不是最终资产

Web image generation is useful for exploring visual directions, but it often creates fragile details, distorted text, raster artifacts, and inconsistent geometry. The accepted route must be redrawn as clean SVG.

网页端生图适合探索视觉方向，但常会产生脆弱细节、文字畸变、位图瑕疵和不一致几何。被采纳的方向必须重新绘制为干净 SVG。

## Acceptance Gate / 接受门槛

A new logo direction can move forward only if it passes all of these checks:

新的 logo 方向只有通过以下检查，才可以继续推进：

1. It is recognizable as a black-only silhouette.
2. It remains legible at 64px, 32px, and 16px.
3. It can be drawn with simple, maintainable SVG geometry.
4. It avoids gradients, glow, shadows, and rendered textures.
5. It avoids brain, gear, chat bubble, sparkle, and generic code bracket clichés.
6. It suggests compression, decompression, workflow, skill, or transformation without needing a paragraph of explanation.
7. It works without embedded text.
8. It can extend to `assets/logo.svg`, `assets/logo-mono.svg`, `assets/banner.svg`, and `assets/social-preview.svg`.

## Revised Workflow / 修正后的工作流

1. Use the web generation prompt in [web-image-generation-prompt.md](web-image-generation-prompt.md) to produce a route board, not a final logo.
2. Select one or two strongest symbols from the generated board.
3. Redraw the selected route manually as SVG.
4. Test the route in color, monochrome, and small-size contexts.
5. Update the repository assets only after the small-size and silhouette checks pass.
6. Run the structure validators before publication.

1. 使用 [web-image-generation-prompt.md](web-image-generation-prompt.md) 生成方向板，而不是直接生成最终 logo。
2. 从方向板中选择 1 到 2 个最强符号。
3. 将选中的方向手工重绘为 SVG。
4. 测试彩色、单色、小尺寸场景。
5. 小尺寸与剪影检查通过后，再更新仓库资产。
6. 发布前运行结构校验。
