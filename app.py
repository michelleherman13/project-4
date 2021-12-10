from flask import Flask
from flask import render_template
# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/generator")
def generator():
    #Return template and data
    return render_template("generator.html")

# run the application
if __name__ == "__main__":
    app.run(debug=True)