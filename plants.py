# LIBRARIES
# BeautifulSoup4

# DATA FORMAT
# Input: Zip Code
# URL: https://www.wildflower.org 

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
