from flask import Flask
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")


import routes
import birds

if birds.is_empty():
    birds.add_birds_to_db()
