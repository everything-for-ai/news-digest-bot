# News Digest Bot / 新闻摘要机器人

<div class="tabs">
<details open>
<summary><span>🇨🇳 中文 (默认)</span></summary>

## 📰 GitHub 热门项目摘要

每日推送 GitHub 热门开源项目

### 功能特点
- ⭐ **真实数据** - 直接调用 GitHub API
- 🔥 **每日更新** - 自动获取最新热门项目
- 🤖 **AI 项目** - 专门收录 AI/机器学习项目
- 📱 **多平台** - 飞书、企业微信、Telegram

### 新闻源

| 分类 | 说明 | 示例 |
|------|------|------|
| github_trending | 全站热门 | freeCodeCamp, awesome |
| github_ai | AI 热门项目 | AutoGPT, stable-diffusion |
| github_new | 新趋势项目 | 最新高星项目 |

### 自定义配置

编辑 `config.json`：

```json
{
    "schedule": "09:00",
    "sources": ["github_trending", "github_ai"],
    "count": 5
}
```

### 快速开始
```bash
cd news-digest-bot
pip install -r requirements.txt
python news_bot.py
```

</details>
<details>
<summary><span>🇺🇸 English</span></summary>

## 📰 GitHub Trending Digest

Daily GitHub trending open-source projects

### Features
- ⭐ **Real Data** - Direct GitHub API
- 🔥 **Daily Update** - Auto fetch trending projects
- 🤖 **AI Projects** - AI/ML projects focus
- 📱 **Multi-platform** - Feishu, WeCom, Telegram

### Sources

| Category | Description | Example |
|----------|-------------|---------|
| github_trending | All-time popular | freeCodeCamp, awesome |
| github_ai | AI trending projects | AutoGPT, langchain |
| github_new | New trending | Recent high-star projects |

### Quick Start
```bash
cd news-digest-bot
pip install -r requirements.txt
python news_bot.py
```

</details>
</div>

---

## 项目结构

```
news-digest-bot/
├── news_bot.py       # 主程序
├── config.json       # 配置文件
└── requirements.txt  # 依赖
```

## 依赖

```
requests
```

## 数据来源

- GitHub REST API (https://api.github.com)
- 免费，无需 API Key

## License

MIT
