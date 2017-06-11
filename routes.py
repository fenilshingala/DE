from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

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