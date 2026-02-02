#!/usr/bin/env python3
"""
News Digest Bot - Daily news summary
"""

import os
import json
import requests
from datetime import datetime
from typing import Dict, List


class NewsDigestBot:
    def __init__(self, config_file: str = "config.json"):
        self.config = self.load_config(config_file)
    
    def load_config(self, config_file: str) -> Dict:
        default_config = {
            "schedule": "09:00",
            "platforms": ["feishu"],
            "news_api_key": os.environ.get("NEWS_API_KEY", ""),
            "categories": ["technology", "business"],
            "country": "cn"
        }
        
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
                default_config.update(config)
        
        return default_config
    
    def get_news(self, category: str = "technology") -> List[Dict]:
        """Get news from NewsAPI"""
        api_key = self.config.get("news_api_key", "")
        
        if not api_key:
            return self.get_mock_news()
        
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "category": category,
            "country": self.config.get("country", "cn"),
            "apiKey": api_key,
            "pageSize": 5
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            if data.get("status") == "ok":
                return data.get("articles", [])
        except Exception as e:
            print(f"News API error: {e}")
        
        return self.get_mock_news()
    
    def get_mock_news(self) -> List[Dict]:
        """Return mock news for testing"""
        return [
            {"title": "AI 助手助力工作效率提升 300%", "source": "TechNews", "url": "#"},
            {"title": "Python 3.13 发布，性能大幅提升", "source": "DevNews", "url": "#"},
            {"title": "GitHub Copilot X 正式发布", "source": "CodeNews", "url": "#"},
            {"title": "OpenClaw 新版本发布，AI 助手更智能", "source": "AI News", "url": "#"},
            {"title": "程序员最佳编程字体推荐", "source": "Tools", "url": "#"}
        ]
    
    def format_news_message(self, news: List[Dict]) -> str:
        """Format news as a message"""
        articles = []
        for i, item in enumerate(news, 1):
            source = item.get("source", {}).get("name", "Unknown") if isinstance(item.get("source"), dict) else item.get("source", "Unknown")
            articles.append(f"{i}. {item.get('title', '无标题')}\n   📰 {source}")
        
        return f"""
📰 每日新闻摘要 - {datetime.now().strftime('%Y-%m-%d')}

{chr(10).join(articles)}

#新闻 #每日摘要
        """.strip()
    
    def run(self):
        all_news = []
        for category in self.config.get("categories", ["technology"]):
            news = self.get_news(category)
            all_news.extend(news[:3])
        
        message = self.format_news_message(all_news)
        print(message)
        return message


if __name__ == "__main__":
    bot = NewsDigestBot()
    bot.run()
