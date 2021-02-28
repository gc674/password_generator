import os
import sqlite3
import encrypt
import time


fisier_db = 'parole.db'
# 50 -> 120
sql_agenda_table = """ CREATE TABLE IF NOT EXISTS parole (
                                                                parola_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                parola TEXT); """


def create_db(db_name, sql_table):
    """se crează baza de date dacă nu există"""
    my_connection = sqlite3.connect(db_name)
    my_connection.execute(sql_table)
    my_connection.commit()
    my_connection.close()


def write_to_db(db_name, data):
    """se adaugă date în baza de date criptate folosind criptare()
    """
    print('Se scrie în baza de date:')
    time.sleep(0.5)
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    data = encrypt.criptare(data)
    cursor.execute("INSERT INTO parole (parola) VALUES (?);", [data])
    time.sleep(0.5)
    connection.commit()
    connection.close()


def _add_to_db(data, sql_table, db_name=fisier_db):
    """se adaugă în baza de date
    """
    print(db_name)
    if os.path.exists(db_name):
        print('Baza de date există!')
        time.sleep(0.5)
        write_to_db(db_name, data)
    else:
        print('Se crează baza de date!')
        time.sleep(0.5)
        create_db(db_name, sql_table)
        write_to_db(db_name, data)


def add_to_db(parola):
    """se generează meniul pentru introducerea datelor persoanei de contact"""
    _add_to_db(parola, sql_table=sql_agenda_table)


def istoric(db_name=fisier_db):
    """se va afișa un istoric cu parolelel generate decriptate"""
    print('Istoric parole:')
    time.sleep(0.5)
    my_connection = sqlite3.connect(db_name)
    my_cursor = my_connection.cursor()
    my_cursor.execute(f'''SELECT * FROM parole;''')
    rows = my_cursor.fetchall()
    for row in rows:
        parola = encrypt.decriptare(row[1])
        print(parola)
    my_connection.close()
    time.sleep(0.5)
