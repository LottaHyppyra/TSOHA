from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///hylotta"
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute("SELECT laji FROM linnut")
    linnut = result.fetchall()
    return render_template("index.html", count=len(linnut), linnut=linnut) 

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    laji = request.form["laji"]
    sql = "INSERT INTO linnut (laji) VALUES (:laji)"
    db.session.execute(sql, {"laji":laji})
    db.session.commit()
    return redirect("/")

