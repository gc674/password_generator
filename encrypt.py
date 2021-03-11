import os
from cryptography.fernet import Fernet


def gen_key(keyfile):
    """generează cheia și salvează cheia în directorul curent.
    """
    key = Fernet.generate_key()
    with open(keyfile, "wb") as kf:
        kf.write(key)


def read_key(keyfile):
    """citește fișierul cheie
    """
    with open(keyfile, "rb") as kf:
        key = kf.read()
        return key


def load_key(keyfile):
    """Încarcă cheia din directorul curent..
    """
    if os.path.exists(keyfile):
        # print("Cheia există!")
        return read_key(keyfile)
    else:
        print("Cheia nu există.\nSe generează o cheie nouă!")
        gen_key(keyfile)
        return read_key(keyfile)


def criptare(text, keyfile):
    """
    se criptează mesajul folosind cheia din directorul curent
    """
    text_criptat = text.encode()
    f = Fernet(load_key(keyfile))
    return f.encrypt(text_criptat)


def decriptare(text, keyfile):
    """se decriptează mesajul folosind cheia din directorul curent,
    iar dacă nu există se va genera o cheie nouă
    """
    f = Fernet(load_key(keyfile))
    return (f.decrypt(text)).decode()
