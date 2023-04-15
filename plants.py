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

app = Flask(__name__)

@app.route("/state/<state>")
def local_area(state):
    return f"""
    <html>
        <body>
            <p>You entered: {state}</p>
            <p>Here's your first plant!\n{list(plants.keys())[0]}</p>
        </body>
    </html>   
    """

@app.route("/")
def home():
    return "<p>Balls</p>"
