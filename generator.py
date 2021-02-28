import string
import secrets
import random
import database


def generare(lungime, majuscule, cifre, schar):
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
    database.add_to_db(parola)
