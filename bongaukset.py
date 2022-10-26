from db import db

def get_all():
    sql = """SELECT laji, paikka FROM bongaukset"""
    return db.session.execute(sql).fetchall()

def get_my(user_id):
    sql = """SELECT laji, paikka FROM bongaukset WHERE kayttaja_id=:user_id"""
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def add(laji, paikka, kayttaja_id):
    try:
        sql = """INSERT INTO bongaukset (laji, paikka, kayttaja_id) VALUES (:laji, :paikka, :kayttaja_id) """
        db.session.execute(sql, {"laji":laji, "paikka":paikka, "kayttaja_id":kayttaja_id})
        db.session.commit()
    except:
        return False
