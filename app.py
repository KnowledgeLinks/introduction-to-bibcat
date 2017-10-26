__author__ = "Jeremy Nelson"

from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config["FLATPAGES_EXTENSION"] = ".md"
pages = FlatPages(app)

@app.route("/topic/")
@app.route("/topic/<name>")
def topic(name=None):
    if name is None:
        return render_template(
            "intro-to-bibcat/topics.html", 
            topics=pages)
    page = pages.get_or_404(name)
    return render_template(
        "intro-to-bibcat/topic.html", 
        topic=page,
        topics=pages)

@app.route("/")
def home():
    return render_template("intro-to-bibcat/index.html", topics=pages)
