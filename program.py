import os
import time
import string
import secrets
import random
import sqlite3
from cryptography.fernet import Fernet


fisier_db = 'parole.db'
# 50 -> 120
sql_agenda_table = """ CREATE TABLE IF NOT EXISTS parole (
                                                                parola_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                parola TEXT); """


def gen_key(cheia):
    """generează cheia și salvează cheia în directorul curent.
    """
    key = Fernet.generate_key()
    with open(cheia, "wb") as key_file:
        key_file.write(key)


def load_key(cheia="secret"):
    """Încarcă cheia din directorul curent..
    """
    if os.path.exists(cheia):
        # print("Cheia există!")
        return open(cheia, "rb").read()
    else:
        print("Cheia nu există.\nSe generează o cheie nouă!")
        gen_key(cheia)
        return open(cheia, "rb").read()


def criptare(text):
    """
    se criptează mesajul folosind cheia din directorul curent
    """
    text_criptat = text.encode()
    f = Fernet(load_key())
    return f.encrypt(text_criptat)


def decriptare(text):
    """se decriptează mesajul folosind cheia din directorul curent,
    iar dacă nu există se va genera o cheie nouă
    """
    f = Fernet(load_key())
    return (f.decrypt(text)).decode()


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
    data = criptare(data)
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
        parola = decriptare(row[1])
        print(parola)
    my_connection.close()
    time.sleep(0.5)


def _generare_parola(lungime=9, majuscule=1, cifre=1, schar=2):
    """se va genera o parola în funcție de datele primite de la utilizator"""
    parola = []
    for i in range(majuscule):
        data = string.ascii_uppercase
        parola.append(secrets.choice(data))
    for i in range(cifre):
        data = string.digits
        parola.append(secrets.choice(data))
    for i in range(schar):
        data = string.punctuation
        parola.append(secrets.choice(data))
    for i in range(lungime - (majuscule + cifre + schar)):
        data = string.ascii_letters + string.digits + string.punctuation
        parola.append(secrets.choice(data))
    random.shuffle(parola)
    parola = ''.join(parola)
    add_to_db(parola)


def generare_parola(lungime=9, majuscule=1, cifre=1, schar=2):
    """se va genera o parola"""
    print('Se generează parola...')
    time.sleep(0.5)
    return _generare_parola(lungime, majuscule, cifre, schar)


def meniu():
    """meniul agendei"""
    print('''
    ^Generator Parole^

    1. Generează o nouă parolă standard de minim 9 caractere.
    2. Generează o parolă nonstandard.
    3. Afișează isotric parole

    !!!păstrați cheia generată!!!

    Pentru a opri programul folosiți litera e
    ''')

    a = input('selectați opțiunea: ')
    if a == 'e':
        print('Programul se oprește!')
        exit(0)
    elif a == '1':
        generare_parola()
    elif a == '2':
        lungime = int(input('Ce lungime va avea parola?: '))
        majuscule = int(input('Câte majuscule va conține?: '))
        cifre = int(input('Câte cifre va conține?: '))
        schar = int(input('Câte caractere speciale va conține?: '))
        termeni = majuscule + cifre + schar
        if termeni <= lungime:
            if lungime <= 50:
                generare_parola(lungime, majuscule, cifre, schar)
            else:
                print(f'Lungimea parolei nu poate fi mai mare de 50 de caractere!')
                time.sleep(0.5)
        else:
            print(f'Lungimea termenilor nu trebuie să depășească lungimea parolei.\n'
                  f'Totalul termenilor:{termeni} depășește lungimea parolei:{lungime}')
            time.sleep(0.5)
    elif a == '3':
        istoric()
    else:
        print('Alegeți opțiunea corectă!')


while True:
    meniu()
