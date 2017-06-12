from flask import Flask, redirect, render_template, url_for, request, session
from pymongo import MongoClient
from datetime import timedelta
client = MongoClient()
db = client["DE"]
app = Flask(__name__)


def loggedin():
    return 'enrl' in session


@app.route('/')
def index():
    if loggedin():
        return redirect(url_for("dashboard"))
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    if not loggedin():
        return redirect(url_for("index"))
    print(session["enrl"])
    return render_template("dashboard.html",session=session)


@app.route('/login', methods=["GET", "POST"])
def login():
    if loggedin():
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        users = db["users"]
        enrl = request.form["enrl"]
        u = users.find_one({"enrl": enrl})
        if u is None:
            return render_template("index.html", error="User not found. Please sign up first")
        else:
            password = request.form["password"]
            if u["password"] != password:
                return render_template("index.html", error="Wrong password")
            session['enrl'] = enrl
            return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("index"))


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if loggedin():
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        data = {}
        users = db["users"]
        enrl = request.form["enrl"]
        u = users.find_one({"enrl": enrl})
        if u is not None:
            return render_template("index.html", error="User already exists")
        for i in request.form:
            data[i] = request.form[i]
        users.insert_one(data)
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("index"))


@app.route('/signout/')
def signout():
    session.pop('enrl', None)
    return redirect(url_for("index"))


@app.route('/submissions/')
def submissions():
    if not loggedin():
        return redirect(url_for("index"))
    return render_template("submissions.html")


@app.route('/updates/')
def updates():
    if not loggedin():
        return redirect(url_for("index"))
    return render_template("updates.html")

@app.errorhandler(404)
def pagenotfound(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.secret_key = 'secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.permanent_session_lifetime = timedelta(days=30)
    app.run(debug=True)
