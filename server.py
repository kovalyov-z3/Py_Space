from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("login.html", username = "")

    if request.method == "POST":

        login = request.form.get("login")
        pasword = request.form.get("password")
        return render_template("login.html", username = "Привет " + login)

@app.route("/snake_to_space", methods= ["GET", "POST"])
def snake():
    return {"status":"launched!", "description":"from timeweb apps"}

app.run(host="0.0.0.0")
