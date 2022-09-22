from app import app
from flask import render_template, request, redirect
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        kayttajatunnus = request.form["kayttajatunnus"]
        salasana = request.form["salasana"]

        if not users.login(kayttajatunnus, salasana):
            return render_template("error.html", message="Väärä tunnus tai salasana")
        return redirect("/")

@app.route("/register", methods =["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        tunnus = request.form["kayttajatunnus"]
        if len(tunnus) < 1 or len(tunnus) > 20:
            return render_template("error.html", message="Tunnuksen tulee olla 1-20 merkkiä pitkä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if password1 == "":
            return render_template("error.html", message="Salasana on tyhjä")

        if not users.register(tunnus, password1):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

        return redirect("/")