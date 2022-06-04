from flask import Flask, render_template
from feedparser import parse

RSS_SOURCE = 'https://ilmajaam.postimees.ee/rss'
app = Flask(__name__)


@app.route('/')
def get_index():
    entries = get_news(RSS_SOURCE)
    return render_template('index.html', entries=entries)


def get_news(rss_link):
    feed = parse(rss_link)
    entries = feed['entries']
    return entries


if __name__ == '__main__':
    app.run()
