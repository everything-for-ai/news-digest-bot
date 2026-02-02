# News Digest Bot / 新闻摘要机器人

<div class="tabs">
<details open>
<summary><span>🇨🇳 中文 (默认)</span></summary>

## 📰 新闻摘要机器人

每日自动推送精选新闻摘要

### 功能特点
- 📰 **多分类新闻** - 科技、AI、财经
- ⏰ **定时推送** - 每天 09:00 自动推送
- 🔗 **RSS 支持** - 可自定义订阅源
- 📱 **多平台** - 飞书、企业微信、Telegram

### 支持的分类

| 分类 | 说明 | 默认 |
|------|------|------|
| tech | 科技新闻 | ✅ |
| ai | AI 人工智能 | ✅ |
| finance | 财经新闻 | ❌ |

### 自定义配置

编辑 `config.json`：

```json
{
    "schedule": "09:00",
    "sources": ["tech", "ai", "finance"],
    "count": 5,
    "rss_sources": [
        "https://feeds.feedburner.com/TechCrunch/",
        "https://wired.com/feed/tag/ai/latest/rss"
    ]
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

## 📰 News Digest Bot

Daily automated news digest

### Features
- 📰 **Multi-category** - Tech, AI, Finance
- ⏰ **Scheduled push** - Daily at 09:00
- 🔗 **RSS support** - Customizable feeds
- 📱 **Multi-platform** - Feishu, WeCom, Telegram

### Supported Categories

| Category | Description | Default |
|----------|-------------|---------|
| tech | Technology news | ✅ |
| ai | Artificial Intelligence | ✅ |
| finance | Finance news | ❌ |

### Configuration

Edit `config.json`:

```json
{
    "schedule": "09:00",
    "sources": ["tech", "ai", "finance"],
    "count": 5
}
```

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

## License

MIT
