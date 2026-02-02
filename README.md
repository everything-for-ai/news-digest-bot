# News Digest Bot / 每日热点汇总

<div class="tabs">
<details open>
<summary><span>🇨🇳 中文 (默认)</span></summary>

## 📰 每日热点汇总

阮一峰博客 + B站热门 + 微博热搜 + 抖音/小红书热点

### 功能特点
- 📖 **阮一峰博客** - 技术博客 RSS 订阅
- 📺 **B站热门** - 真实 API 获取
- 🔥 **微博热搜** - 实时热点
- 🎵 **抖音热榜** - 短视频热点
- 📕 **小红书** - 生活方式热点

### 支持的来源

| 来源 | 说明 | 数据 |
|------|------|------|
| ruanyifeng | 阮一峰博客 | ✅ 真实 RSS |
| bilibili | B站热门视频 | ✅ 真实 API |
| weibo | 微博热搜 | 🔄 模拟数据 |
| douyin | 抖音热榜 | 🔄 模拟数据 |
| xiaohongshu | 小红书热点 | 🔄 模拟数据 |

### 自定义配置

编辑 `config.json`：

```json
{
    "schedule": "09:00",
    "sources": ["ruanyifeng", "bilibili", "weibo", "douyin", "xiaohongshu"],
    "count": 5
}
```

### 快速开始
```bash
cd news-digest-bot
python news_bot.py
```

</details>
<details>
<summary><span>🇺🇸 English</span></summary>

## 📰 Daily Hot Topics Summary

Ruan Yifeng Blog + Bilibili + Weibo + Douyin + Xiaohongshu

### Features
- 📖 Ruan Yifeng Blog (Tech)
- 📺 Bilibili Trending
- 🔥 Weibo Hot Search
- 🎵 Douyin Trending
- 📕 Xiaohongshu Trends

### Quick Start
```bash
cd news-digest-bot
python news_bot.py
```

</details>
</div>

---

## 数据来源

| 来源 | 链接 | 状态 |
|------|------|------|
| 阮一峰博客 | ruanyifeng.com | ✅ RSS |
| B站热门 | api.bilibili.com | ✅ API |
| 微博热搜 | weibo.com | 🔄 模拟 |
| 抖音热榜 | douyin.com | 🔄 模拟 |
| 小红书 | xiaohongshu.com | 🔄 模拟 |

---

*由 everything-for-ai 项目提供*
