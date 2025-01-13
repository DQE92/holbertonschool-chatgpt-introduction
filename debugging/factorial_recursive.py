#!/usr/bin/python3
# Importation de la bibliothèque sys pour gérer les arguments de ligne de commande
import sys

# Définition de la fonction récursive factorial
def factorial(n):
    # Cas de base : si n est égal à 0, la factorielle est définie comme 1
    if n == 0:
        return 1
    else:
        # Appel récursif : multiplier n par la factorielle de (n-1)
        return n * factorial(n - 1)

# Lecture du premier argument de la ligne de commande, converti en entier
# sys.argv[1] est le premier argument passé (le nom du script est sys.argv[0])
f = factorial(int(sys.argv[1]))

# Affichage de la valeur de la factorielle calculée
print(f)