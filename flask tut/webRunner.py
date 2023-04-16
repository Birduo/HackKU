from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route("/state")
def local_area():
    return render_template('first.html')


@app.route('/plants', methods=["GET", "POST"])
def plants():
    '''
    if request.method == "POST":
        plants = request.form.get("State")

        return "The best plants for you are: "+plants
    '''
    return render_template("plant.html")
