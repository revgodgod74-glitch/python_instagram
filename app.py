from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/feed")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return redirect("/")
    return render_template("signup.html")

@app.route("/feed")
def feed():
    return render_template("feed.html")

if __name__ == "__main__":
    app.run(debug=True)
