from flask import Flask, redirect, render_template, url_for, request, session
from pymongo import MongoClient

client = MongoClient()
db = client["DE"]
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

<<<<<<< HEAD
@app.route('/login/', methods=["GET","POST"])
def login():
    if request.method=="POST":
        users = db["users"]
        user=request.form["enrl"]
        u=users.find_one({"enrl":user})
        if u is None:
            print("User not found!")
            return render_template("index.html", error="User not found. Please sign up first")
        else:
            password=request.form["password"]
            print(user, password)
            print(u["password"])
            if u["password"]!=password:
                print("here1")
                return render_template("index.html", error="Wrong password")
            print("acc")
            return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("index"))

@app.route('/signup/', methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        data={}
        users = db["users"]
        enrl=request.form["enrl"]
        u=users.find_one({"enrl":enrl})
        if u is not None:
            return render_template("index.html", error="User already exists")
        for i in request.form:
            data[i]=request.form[i]
        users.insert_one(data)
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("index"))




if __name__ == '__main__':

    app.run()
=======
@app.route('/header')
def header():
    return render_template("header.html")

@app.route('/footer')
def footer():
    return render_template("footer.html")

@app.route('/submissions')
def submissions():
    return render_template("submissions.html")

@app.route('/updates')
def updates():
    return render_template("updates.html")

if __name__ == '__main__':
    app.run()
>>>>>>> ec39e333a02654884dd6aee52c9e43b7294336ac
