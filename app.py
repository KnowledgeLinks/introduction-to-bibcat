__author__ = "Jeremy Nelson"

import os
import rdflib

from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config["FLATPAGES_EXTENSION"] = ".md"

pages = FlatPages(app)

SCHEMA = rdflib.Namespace("http://schema.org/")
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
INTRO_BIBCAT_GRAPH = rdflib.Graph()
INTRO_BIBCAT_GRAPH.parse(
    os.path.join(SITE_ROOT, 
                 'static/data/project.ttl'),
    format='turtle')

@app.template_filter('get_name')
def entity_name(url):
    name_obj = INTRO_BIBCAT_GRAPH.value(
        subject=rdflib.URIRef(url),
        predicate=SCHEMA.name)
    if not name_obj:
        return ''
    return str(name_obj)
    
@app.template_filter('build_nav')
def build_contents(contents_str):
    internal_link, label = contents_str.split(":")
    return """<a href="#{0}">{1}</a>""".format(
        internal_link.strip(),
        label.strip())

@app.route("/topic/")
@app.route("/topic/<name>.html")
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
