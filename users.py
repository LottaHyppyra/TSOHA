import os
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def login(kayttajatunnus, salasana):
    sql = "SELECT salasana, id FROM users WHERE kayttajatunnus=:kayttajatunnus"
    result = db.session.execute(sql, {"kayttajatunnus":kayttajatunnus})
    user = result.fetchone()
    if not user:
        return False
    else: 
        hash_value = user.salasana
        if check_password_hash(hash_value, salasana):
            session["user_id"] = user[1]
            session["user_name"] = kayttajatunnus
            return True
    return False

def register(kayttajatunnus, salasana):
    hash_value = generate_password_hash(salasana)
    bongaukset = 0
    try:
        sql = """INSERT INTO users (kayttajatunnus, salasana, bongaukset) VALUES (:kayttajatunnus, :salasana, :bongaukset)"""
        db.session.execute(sql, {"kayttajatunnus":kayttajatunnus, "salasana":hash_value, "bongaukset": bongaukset})
        db.session.commit()
    except:
        return False
    return login(kayttajatunnus, salasana)
