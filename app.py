from flask import Flask, render_template, request
import json
from model_pred import ModelPred

# creates a Flask application, named app
app = Flask(__name__)
model = ModelPred()

# a route where we will display a welcome message via an HTML template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/generator")
def generator():
    #Return template and data
    return render_template("generator.html")

@app.route("/directory")
def data():
    #Return template and data
    return render_template("table.html")

@app.route("/get_recommended", methods=["POST"])
def get_recommended():
    user_input = request.json['data']

    if user_input['game'] != "":
        game = user_input['game']
        recommender  = model.get_recommended(game)
        return recommender
    else:
        platform = user_input['platform']
        score = float(user_input['score'])
        recommender  = model.get_recommended2(platform, score)
        return recommender


    # return recommender

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

# run the application
if __name__ == "__main__":
    app.run(debug=True)