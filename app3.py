from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index3a.html")

@app.route("/")
def more():
    return render_template("index3b.html")
