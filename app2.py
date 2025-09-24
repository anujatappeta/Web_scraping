import feedparser
from datetime import datetime

# List of trusted RSS feeds
news_feeds = {
    "BBC World": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "The Hindu (National)": "https://www.thehindu.com/news/national/feeder/default.rss",
    "Times of India (Top Stories)": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
}

print("\n================= 📰 TODAY'S NEWS DIGEST =================\n")
print("Date:", datetime.now().strftime("%A, %d %B %Y"))
print("----------------------------------------------------------\n")

# Fetch and display headlines from each source
for source, url in news_feeds.items():
    print(f"🔹 {source}:\n")
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]:  # only top 5 headlines per source
        print(f"👉 {entry.title}")
        print(f"   {entry.link}\n")  # link to full story
    print("----------------------------------------------------------\n")

print("✅ End of today's news digest.\n")
