# describe-image — Claude Code + DeepSeek V4 图片描述分析 skill

调用阿里云百炼 qwen-vl-max 视觉模型分析图片内容，返回中文描述。

## 前置条件

- [Claude Code](https://claude.ai/code) 已安装
- Python 3（仅用标准库，无需 pip 安装依赖）
- 阿里云百炼 API Key（[开通 DashScope 服务](https://dashscope.console.aliyun.com/)）

## 安装

```bash
git clone https://github.com/Potatotalen/describe-image.git ~/.claude/skills/describe-image
```

> Claude Code 的 skill 系统从 `~/.claude/skills/` 自动发现技能，必须 clone 到此路径。

## 配置 API Key

1. Win+R → 输入 `sysdm.cpl` → 确定
2. 高级 → 环境变量
3. 新建用户变量，变量名 `DASHSCOPE_API_KEY`，值填你的阿里云百炼 API Key
4. 确定后**重启 VSCode** 生效

## 使用

在 Claude Code 中直接说：

- "分析这张图"
- "帮我看看 screenshot.png"
- "这张图片里是什么内容"
- "图片里的文字是什么"

Claude Code 会自动调用本 skill 并返回图片的中文描述。

## 手动测试

```bash
python ~/.claude/skills/describe-image/scripts/img_describe.py /path/to/image.jpg
# 自定义提问
python ~/.claude/skills/describe-image/scripts/img_describe.py /path/to/image.jpg "图片里有什么文字？"
```

## 支持格式

jpg, jpeg, jfif, png, gif, bmp, webp, tiff

## 文件结构

```
describe-image/
├── SKILL.md                  # Claude Code 技能清单
├── scripts/
│   └── img_describe.py       # 调用百炼 Vision API 的脚本
├── README.md
├── LICENSE
└── .gitignore
```
