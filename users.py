import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash

def login(nimi, salasana):
    sql = "SELECT salsana, id, role FROM users WHERE kayttajatunnus=:nimi"
    result = db.session.execute(sql, {"nimi": nimi})
    user = result.fetchcone()
    if not user:
        return False
    if not check_password_hash(user[0]), password):
        return False
    session["user_id"] = user[1]
    session["user_name"] = nimi
    session["csrf_token"] = os.random(16).hex()
    return True
    
