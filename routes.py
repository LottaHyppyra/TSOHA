from app import app
from flask import render_template, request, redirect
import users
import observations
import birds

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    if request.method == "GET":
        omat_bongaukset = observations.get_my(users.user_id())
        return render_template("profile.html", list=omat_bongaukset)

@app.route("/all")
def all():
    if request.method == "GET":
        return render_template("all.html", list=observations.get_all())

@app.route("/birds")
def list_birds():
    if request.method == "GET":
        return render_template("birds.html", list=birds.get_all())

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

@app.route("/logout")
def logout():
    users.logout()
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

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":
        laji = request.form["laji"]
        if len(laji) < 1 or len(laji) > 20:
            return render_template("error.html", message="Linnun lajin tulee olla 1-20 merkkiä pitkä.")

        paikka = request.form["paikka"]
        if len(paikka) < 1 or len(paikka) > 20:
            return render_template("error.html", message="Paikan nimen tulee olla 1-20 merkkiä pitkä.")

        spotted = request.form["spotted"]

        observations.add(laji, paikka, spotted, users.user_id())
        return redirect("/profile")