import os
from flask import abort, request, session
from db import db

def is_empty():
    sql = """SELECT * FROM birds"""
    return len(db.session.execute(sql).fetchall()) == 0

def add_birds_to_db():
    family = None
    with open("birds.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            if parts[0] == "Heimo":
                family = parts[1]
            else:
                name = parts[0]
                latin_name = line.split(")")
                latin_name = latin_name[0].split("(")
                latin_name = latin_name[1]

                try:
                    sql = """INSERT INTO birds (latin_name, name, family) VALUES (:latin_name, :name, :family)"""
                    db.session.execute(sql, {"latin_name":latin_name, "name":name, "family":family})
                    db.session.commit()

                except:
                    return False
