__author__ = "Jeremy Nelson"
from flask_frozen import Freezer
from app import app

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["FREEZER_RELATIVE_URLS"] = True
app.config['FREEZER_BASE_URL'] = 'http://bibcat.org/'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
