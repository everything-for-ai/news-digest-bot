#!/usr/bin/env python3
"""
News Digest Bot - 每日热点汇总
阮一峰博客 + B站热门 + 微博热搜 + 抖音热点
"""

import os
import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Dict, List


class NewsDigestBot:
    """热点汇总机器人"""
    
    def __init__(self, config_file: str = "config.json"):
        self.config = self.load_config(config_file)
        
        # 微博热搜 URL
        self.weibo_hot = "https://weibo.com/ajax/statuses/mymblog?uid=107603&feature=0&is_all=1&is_search=0&key_word=all&starttime=1738401600&endtime=1738488000&is_all=1"
        
        # 抖音热榜 URL
        self.douyin_hot = "https://www.douyin.com/aweme/v1/web/hot/search/list/"
    
    def load_config(self, config_file: str) -> Dict:
        default_config = {
            "schedule": "09:00",
            "sources": ["ruanyifeng", "bilibili", "weibo", "douyin"],
            "count": 5,
        }
        
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
                default_config.update(config)
        
        return default_config
    
    def get_ruanyifeng(self) -> List[Dict]:
        """阮一峰博客 - RSS"""
        try:
            url = "https://www.ruanyifeng.com/blog/atom.xml"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            r = urllib.request.urlopen(req, timeout=10)
            data = r.read().decode('utf-8')
            root = ET.fromstring(data)
            
            news = []
            for entry in root.findall('.//entry')[:5]:
                title = entry.find('title')
                link = entry.find('link')
                summary = entry.find('summary')
                news.append({
                    "title": title.text if title is not None else "No title",
                    "url": link.get('href') if link is not None else "#",
                    "source": "阮一峰博客",
                    "summary": summary.text[:100] if summary is not None else ""
                })
            return news
        except Exception as e:
            print(f"阮一峰 Error: {e}")
        return []
    
    def get_bilibili(self) -> List[Dict]:
        """B站热门视频"""
        try:
            url = "https://api.bilibili.com/x/web-interface/popular?ps=10"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            r = urllib.request.urlopen(req, timeout=10)
            data = json.loads(r.read().decode('utf-8'))
            
            news = []
            for item in data.get('data', {}).get('list', [])[:10]:
                news.append({
                    "title": item.get('title', 'No title'),
                    "url": f"https://www.bilibili.com/video/av{item.get('aid', '')}",
                    "source": "B站热门",
                    "views": item.get('stat', {}).get('view', 0),
                    "author": item.get('owner', {}).get('name', '')
                })
            return news
        except Exception as e:
            print(f"B站 Error: {e}")
        return []
    
    def get_weibo(self) -> List[Dict]:
        """微博热搜 - 模拟数据（API 需要登录）"""
        return [
            {"title": "春节档电影票房破纪录", "url": "#", "source": "微博热搜", "reads": "2.3亿"},
            {"title": "AI 生成歌曲走红网络", "url": "#", "source": "微博热搜", "reads": "1.8亿"},
            {"title": "某明星恋情曝光", "url": "#", "source": "微博热搜", "reads": "1.5亿"},
            {"title": "考研成绩陆续公布", "url": "#", "source": "微博热搜", "reads": "9800万"},
            {"title": "各地开学季开启", "url": "#", "source": "微博热搜", "reads": "8600万"}
        ]
    
    def get_douyin(self) -> List[Dict]:
        """抖音热榜 - 模拟数据"""
        return [
            {"title": "#年后开工第一天#", "url": "#", "source": "抖音热榜", "views": "5000万+"},
            {"title": "#2024年你能赚多少#", "url": "#", "source": "抖音热榜", "views": "4200万+"},
            {"title": "AI 写春联教程", "url": "#", "source": "抖音热榜", "views": "3800万+"},
            {"title": "各地雪景刷屏", "url": "#", "source": "抖音热榜", "views": "3200万+"},
            {"title": "返程高峰注意事项", "url": "#", "source": "抖音热榜", "views": "2800万+"}
        ]
    
    def get_xiaohongshu(self) -> List[Dict]:
        """小红书热点 - 模拟数据"""
        return [
            {"title": "年后减脂餐推荐", "url": "#", "source": "小红书", "likes": "10万+"},
            {"title": "AI 头像生成教程", "url": "#", "source": "小红书", "likes": "8万+"},
            {"title": "2024 美甲趋势", "url": "#", "source": "小红书", "likes": "6万+"},
            {"title": "租房攻略合集", "url": "#", "source": "小红书", "likes": "5万+"},
            {"title": "开箱视频合集", "url": "#", "source": "小红书", "likes": "4万+"}
        ]
    
    def get_source(self, name: str):
        """获取新闻源"""
        source_map = {
            "ruanyifeng": self.get_ruanyifeng,
            "bilibili": self.get_bilibili,
            "weibo": self.get_weibo,
            "douyin": self.get_douyin,
            "xiaohongshu": self.get_xiaohongshu
        }
        return source_map.get(name, self.get_ruanyifeng)
    
    def format_message(self, all_news: List[Dict], source_name: str) -> str:
        """格式化输出"""
        if not all_news:
            return ""
        
        source_map = {
            "ruanyifeng": ("📖 阮一峰博客", "📝"),
            "bilibili": ("📺 B站热门", "👀"),
            "weibo": ("🔥 微博热搜", "👀"),
            "douyin": ("🎵 抖音热榜", "▶️"),
            "xiaohongshu": ("📕 小红书热点", "❤️")
        }
        
        title, emoji = source_map.get(source_name, ("📰", "•"))
        lines = [f"\n{title}\n"]
        lines.append("-" * 40)
        
        for i, item in enumerate(all_news[:5], 1):
            title = item.get('title', '无标题')[:40]
            url = item.get('url', '#')
            
            # 不同来源的额外信息
            extra = ""
            if item.get('views'):
                extra = f" {emoji} {item['views']}"
            elif item.get('reads'):
                extra = f" {emoji} {item['reads']}"
            elif item.get('likes'):
                extra = f" ❤️ {item['likes']}"
            elif item.get('author'):
                extra = f" | UP: {item['author']}"
            
            lines.append(f"{i}. {title}{extra}")
            lines.append(f"   🔗 {url}")
        
        return '\n'.join(lines)
    
    def run(self) -> str:
        """主程序"""
        lines = [f"📰 每日热点汇总 - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"]
        lines.append("=" * 40)
        
        for source in self.config.get("sources", []):
            news = self.get_source(source)()
            lines.append(self.format_message(news, source))
        
        lines.append("\n#热点 #每日汇总")
        message = '\n'.join(lines)
        print(message)
        return message


if __name__ == "__main__":
    bot = NewsDigestBot()
    bot.run()
