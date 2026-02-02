#!/usr/bin/env python3
"""
News Digest Bot - 每日新闻摘要
使用 GitHub API 获取真实科技趋势，无需 API Key
"""

import os
import json
import requests
from datetime import datetime
from typing import Dict, List


class NewsDigestBot:
    """新闻摘要机器人"""
    
    def __init__(self, config_file: str = "config.json"):
        self.config = self.load_config(config_file)
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json"
        })
    
    def load_config(self, config_file: str) -> Dict:
        default_config = {
            "schedule": "09:00",
            "sources": ["github_trending", "github_ai"],
            "count": 5,
        }
        
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
                default_config.update(config)
        
        return default_config
    
    def get_github_trending(self) -> List[Dict]:
        """获取 GitHub 热门项目"""
        try:
            url = "https://api.github.com/search/repositories"
            params = {
                "q": "stars:>10000",
                "sort": "stars",
                "per_page": 10
            }
            resp = self.session.get(url, params=params, timeout=10)
            
            if resp.status_code == 200:
                data = resp.json()
                news = []
                for item in data.get('items', [])[:10]:
                    news.append({
                        "title": item.get('name', 'No name'),
                        "url": item.get('html_url', '#'),
                        "source": "GitHub Trending",
                        "stars": item.get('stargazers_count', 0),
                        "description": item.get('description', '')[:100]
                    })
                return news
        except Exception as e:
            print(f"GitHub Error: {e}")
        return []
    
    def get_github_ai(self) -> List[Dict]:
        """获取 AI 相关热门项目"""
        try:
            url = "https://api.github.com/search/repositories"
            params = {
                "q": "topic:AI language:Python stars:>5000",
                "sort": "stars",
                "per_page": 10
            }
            resp = self.session.get(url, params=params, timeout=10)
            
            if resp.status_code == 200:
                data = resp.json()
                news = []
                for item in data.get('items', [])[:10]:
                    news.append({
                        "title": item.get('name', 'No name'),
                        "url": item.get('html_url', '#'),
                        "source": "GitHub AI",
                        "stars": item.get('stargazers_count', 0),
                        "description": item.get('description', '')[:100]
                    })
                return news
        except Exception as e:
            print(f"GitHub AI Error: {e}")
        return []
    
    def get_github_new(self) -> List[Dict]:
        """获取最新热门项目"""
        try:
            url = "https://api.github.com/search/repositories"
            params = {
                "q": "created:>2025-01-01 stars:>1000",
                "sort": "stars",
                "per_page": 10
            }
            resp = self.session.get(url, params=params, timeout=10)
            
            if resp.status_code == 200:
                data = resp.json()
                news = []
                for item in data.get('items', [])[:10]:
                    news.append({
                        "title": item.get('name', 'No name'),
                        "url": item.get('html_url', '#'),
                        "source": "GitHub New",
                        "stars": item.get('stargazers_count', 0),
                        "description": item.get('description', '')[:100]
                    })
                return news
        except Exception as e:
            print(f"GitHub New Error: {e}")
        return []
    
    def get_news(self, source: str = "github_trending") -> List[Dict]:
        """获取新闻"""
        source_map = {
            "github_trending": self.get_github_trending,
            "github_ai": self.get_github_ai,
            "github_new": self.get_github_new
        }
        
        func = source_map.get(source, self.get_github_trending)
        return func()
    
    def format_news_message(self, news: List[Dict]) -> str:
        """格式化新闻消息"""
        if not news:
            return "📰 暂无新闻"
        
        lines = [f"📰 GitHub 热门项目 - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"]
        
        for i, item in enumerate(news[:10], 1):
            title = item.get('title', '无标题')
            source = item.get('source', 'Unknown')
            stars = item.get('stars', 0)
            desc = item.get('description', '')[:50]
            lines.append(f"{i}. ⭐ {title}")
            lines.append(f"   {desc}...")
            lines.append(f"   📰 {source} | ★ {stars:,}")
        
        lines.append("\n#GitHub #热门项目 #科技")
        return '\n'.join(lines)
    
    def run(self) -> str:
        """主程序"""
        all_news = []
        
        for source in self.config.get("sources", ["github_trending"]):
            news = self.get_news(source)
            count = self.config.get("count", 5)
            all_news.extend(news[:count])
        
        message = self.format_news_message(all_news)
        print(message)
        return message


if __name__ == "__main__":
    bot = NewsDigestBot()
    bot.run()
