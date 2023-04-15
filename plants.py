# LIBRARIES
# BeautifulSoup4

# DATA FORMAT
# Input: Zip Code
# Default URL: http://floranorthamerica.org/Special:Ask/sort%3D/order%3Dasc/offset%3D0/limit%3D500/-5B-5BDistribution::Kans.-5D-5D/mainlabel%3D/
# Modified URL: f"http://floranorthamerica.org/Special:Ask/format%3Djson/sort%3D/order%3Dasc/offset%3D{OFFSET}/limit%3D500/-5B-5BDistribution::{location}-5D-5D/mainlabel%3D/prettyprint%3Dtrue/unescape%3Dtrue/searchlabel%3DJSON"

# POTENTIAL IDEAS
# NLP
# Whisper
# FLASK BACKEND

from flask import Flask

from lab import scrapeFNA

app = Flask(__name__)

plants = scrapeFNA()

@app.route("/state/<state>")
def local_area(state):
    return f"<p>You entered: {state}</p>"

@app.route("/")
def home():
    return "<p>Balls</p>"
