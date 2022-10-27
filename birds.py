import os
from flask import abort, request, session
from db import db

def is_empty():
    sql = """SELECT * FROM birds"""
    return len(db.session.execute(sql).fetchall()) == 0

def get_all():
    sql = """SELECT * FROM birds"""
    return db.session.execute(sql).fetchall()

def get_families():
    sql = """SELECT * FROM family """
    return db.session.execute(sql).fetchall() 

def add_birds_to_db():
    family = None
    with open("birds.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            if parts[0] == "Heimo":
                family = parts[1]
                to_family = """INSERT INTO family (name) VALUES (:name)"""
                db.session.execute(to_family, {"name":family})
                db.session.commit()
            else:
                name = parts[0]
                latin_name = line.split(")")
                latin_name = latin_name[0].split("(")
                latin_name = latin_name[1]

                try:
                    to_birds = """INSERT INTO birds (latin_name, name, family) VALUES (:latin_name, :name, :family)"""
                    db.session.execute(to_birds, {"latin_name":latin_name, "name":name, "family":family})
                    db.session.commit()

                except:
                    return False
