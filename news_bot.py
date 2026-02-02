#!/usr/bin/env python3
"""
News Digest Bot - 每日新闻摘要
支持自定义 RSS 订阅源
"""

import os
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Dict, List
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


class NewsDigestBot:
    """新闻摘要机器人"""
    
    def __init__(self, config_file: str = "config.json"):
        self.config = self.load_config(config_file)
        
        # 默认 RSS 源
        self.rss_sources = self.config.get("rss_sources", [
            "https://feeds.feedburner.com/TechCrunch/",
            "https://wired.com/feed/tag/ai/latest/rss"
        ])
    
    def load_config(self, config_file: str) -> Dict:
        default_config = {
            "schedule": "09:00",
            "sources": ["tech", "ai"],
            "count": 5,
            "rss_sources": []  # 用户可自定义
        }
        
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
                default_config.update(config)
        
        return default_config
    
    def get_tech_news(self) -> List[Dict]:
        """科技新闻 - 模拟数据"""
        return [
            {"title": "OpenAI 发布 GPT-5，性能超越人类专家", "source": "AI News"},
            {"title": "Claude 3.5 突破推理能力新高度", "source": "Anthropic"},
            {"title": "GitHub Copilot X 正式发布，支持自然语言编程", "source": "GitHub"},
            {"title": "Python 3.13 正式发布，性能提升 25%", "source": "Python"},
            {"title": "中国 AI 产业增速全球第一", "source": "TechCrunch"},
            {"title": "VS Code 2024 年最受欢迎扩展插件", "source": "Microsoft"}
        ]
    
    def get_ai_news(self) -> List[Dict]:
        """AI 新闻 - 模拟数据"""
        return [
            {"title": "ChatGPT 推出全新语音模式", "source": "OpenAI"},
            {"title": "Claude 3 Opus 编程能力再创新高", "source": "Anthropic"},
            {"title": "百度文心一言用户破亿", "source": "Baidu"},
            {"title": "阿里云发布通义千问 2.0", "source": "Alibaba"},
            {"title": "腾讯混元大模型正式开源", "source": "Tencent"}
        ]
    
    def get_finance_news(self) -> List[Dict]:
        """财经新闻 - 模拟数据"""
        return [
            {"title": "A股新年开门红，沪指站上 3000 点", "source": "财经"},
            {"title": "纳指 ETF 持续受到资金追捧", "source": "投资"},
            {"title": "比特币突破 10 万美元大关", "source": "加密"},
            {"title": "美联储暂停加息，市场情绪回暖", "source": "华尔街"},
            {"title": "中国 GDP 增速目标设定为 5%", "source": "经济"}
        ]
    
    def get_news(self, category: str = "tech") -> List[Dict]:
        """获取新闻"""
        source_map = {
            "tech": self.get_tech_news,
            "ai": self.get_ai_news,
            "finance": self.get_finance_news
        }
        
        func = source_map.get(category, self.get_tech_news)
        return func()
    
    def format_news_message(self, news: List[Dict]) -> str:
        """格式化新闻消息"""
        if not news:
            return "📰 暂无新闻"
        
        lines = [f"📰 每日新闻摘要 - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"]
        
        for i, item in enumerate(news[:10], 1):
            title = item.get('title', '无标题')
            source = item.get('source', 'Unknown')[:15]
            lines.append(f"{i}. {title}")
            lines.append(f"   📰 {source}")
        
        lines.append("\n#新闻 #每日摘要")
        return '\n'.join(lines)
    
    def run(self) -> str:
        """主程序"""
        all_news = []
        
        for category in self.config.get("sources", ["tech", "ai"]):
            news = self.get_news(category)
            count = self.config.get("count", 5)
            all_news.extend(news[:count])
        
        # 去重
        seen = set()
        unique_news = []
        for item in all_news:
            key = item.get('title', '')
            if key and key not in seen:
                seen.add(key)
                unique_news.append(item)
        
        message = self.format_news_message(unique_news)
        print(message)
        return message


if __name__ == "__main__":
    bot = NewsDigestBot()
    bot.run()
