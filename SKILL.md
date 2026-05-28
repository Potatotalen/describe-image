---
name: describe-image
description: >
  用阿里云百炼 qwen-vl-max 视觉模型分析图片内容。当用户说"分析这张图"、"看看图片里有什么"、
  "描述这个图"、"图片是什么"、"帮我看看xxx.jpg"、"分析下截图"、"这张图片里是什么内容"、
  或者提供了任何图片文件路径并要求理解其内容时，都应使用此 skill。
  Even if the user doesn't explicitly say "describe", any request involving
  understanding or checking an image file (jpg, png, jfif, gif, bmp, webp) should trigger this skill.
---

# Describe Image Skill

用阿里云百炼的 qwen-vl-max 视觉模型分析图片，返回中文描述。

## 执行步骤

当用户提供图片路径并要求分析时：

1. **确认图片存在** — 检查路径，如果不存在则提示用户
2. **运行脚本** — 执行以下命令（超时 90 秒），结果直接输出到终端：
   ```bash
   python "$HOME/.claude/skills/describe-image/scripts/img_describe.py" "<图片绝对路径>"
   ```
3. **呈现给用户** — 将脚本输出的描述展示给用户

## 自定义提问

如果用户对图片有具体问题（如"图片里的文字是什么？"），通过第二个参数传入：
```bash
python "$HOME/.claude/skills/describe-image/scripts/img_describe.py" "<图片路径>" "<具体问题>"
```
