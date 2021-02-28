import os
from cryptography.fernet import Fernet


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
        print("Cheia există!")
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