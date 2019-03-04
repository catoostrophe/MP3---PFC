from random import *

points=0

def jeu():
    global joueur, ordi
    tours=0
    liste=['pierre','feuille','ciseaux']
    while tours<5:
        joueur=str(input("Choisir 'pierre', 'feuille', ou 'ciseaux' :       "))
        ordi=choice(liste)
        print('... a choisi', ordi)
        vainqueur()
        tours=tours+1
    if points>=3:
        print('BRAVO! Vous avez vaincu le méchant dragon qui tue la mort.')
    else:
        print('GAME OVER. Vous avez perdu une vie :( PIXIE VOUS RÉSURRECTE! REJOUEZZZZ :O')

def vainqueur():
    global points
    if ordi==joueur:
        points=points+0.5
        print('Égalité! Vos points sont', points)
    elif ordi=='feuille' and joueur=='pierre' or ordi=='pierre' and joueur=='ciseaux' or ordi=='ciseaux' and joueur=='feuille':
        print('Vous avez perdu! Vos points sont', points)
    elif ordi=='pierre' and joueur=='feuille' or ordi=='ciseaux' and joueur=='pierre' or ordi=='feuille' and joueur=='ciseaux':
        points=points+1
        print('Vous avez gagné! Vos points sont', points)
    else:
        print("Veuillez rentrer soit 'pierre', soit 'feuille', soit 'ciseaux'")
        vainqueur()

jeu()

