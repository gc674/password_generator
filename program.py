import time
import database
import generator


def generare_parola(lungime=9, majuscule=1, cifre=1, schar=2):
    """se va genera o parola cu o lungime standard de 9 caractere,
    1 majusculă, 1 cifră și 2 caractere speciale
    """
    print('Se generează parola...')
    time.sleep(0.5)
    return generator.generare(lungime, majuscule, cifre, schar)


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
        database.istoric()
    else:
        print('Alegeți opțiunea corectă!')


while True:
    meniu()
