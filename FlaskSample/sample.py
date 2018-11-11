from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')


@app.route("/scraping")
def scraping():
    req = requests.get("https://japanese.engadget.com/rss.xml")
    soup = BeautifulSoup(req.content, "html.parser")

    items = []
    for item in soup.select("item"):
        cursor_item = {}
        for title in item.select('title'):
            cursor_item["title"] = title.getText()
        for link in item.select('guid'):
            cursor_item["link"] = link.getText()
        items.append(cursor_item)

    return render_template('scraping.html', items=items)

if __name__ == "__main__":
    app.run()
