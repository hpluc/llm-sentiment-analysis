import feedparser
import json

# Categories WORLD NATION BUSINESS TECHNOLOGY ENTERTAINMENT SCIENCE SPORTS HEALTH

def read_google_news_ticker():
    """Reads the Google News ticker and returns a list of news articles."""

    # Get the Google News RSS feed URL.
    rss_feed_url = "https://news.google.com/rss/search?q=Ukraine&ceid=US:en&hl=en-US&gl=US"

    # Parse the RSS feed using the feedparser library.
    feed = feedparser.parse(rss_feed_url)

    # Check if the parsing was successful.
    if feed.get("bozo_exception"):
        print("Error parsing the RSS feed:", feed.bozo_exception)
        return

    # Loop through the entries in the feed and print article titles and links.
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        print("Title:", title)
        print("Link:", link)
        print("\n")

if __name__ == "__main__":
    read_google_news_ticker()
