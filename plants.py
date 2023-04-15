# LIBRARIES
# BeautifulSoup4

# DATA FORMAT
# Input: Zip Code
# URL: f"http://floranorthamerica.org/Special:Ask/format%3Djson/sort%3D/order%3Dasc/offset%3D{OFFSET}/limit%3D500/-5B-5BDistribution::{location}-5D-5D/mainlabel%3D/prettyprint%3Dtrue/unescape%3Dtrue/searchlabel%3DJSON"

# POTENTIAL IDEAS
# NLP
# Whisper
# FLASK BACKEND

from flask import Flask

app = Flask(__name__)

@app.route("/county/<county>")
def local_area(county):
    return f"<p>You entered: {county}</p>"

@app.route("/")
def home():
    return "<p>Balls</p>"
