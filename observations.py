from db import db

def get_all():
    sql = """SELECT laji, paikka, spotted FROM bongaukset"""
    return db.session.execute(sql).fetchall()

def get_my(user_id):
    sql = """SELECT laji, paikka, spotted FROM bongaukset WHERE kayttaja_id=:user_id"""
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def add(laji, paikka, spotted, kayttaja_id):
    try:
        sql = """INSERT INTO bongaukset (laji, paikka, spotted, kayttaja_id) VALUES (:laji, :paikka, :spotted, :kayttaja_id) """
        db.session.execute(sql, {"laji":laji, "paikka":paikka, "spotted":spotted, "kayttaja_id":kayttaja_id})
        db.session.commit()
    except:
        return False
