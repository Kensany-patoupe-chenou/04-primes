"""
Module pour vérifier si un nombre est premier et afficher les nombres premiers jusqu'à 100.
"""
from math import sqrt
#### Fonction secondaire

def isprime(p):
    '''
    Retourne le nombre premier p.

    Args:
        p:nombre entierr positif

    returns:
        bool: True si p est un nombre premier, False sinon.
    '''
    if p<2:
        return False
    for i in range(2,int(sqrt(p)) + 1):
        if p%i==0:
            return False
    return True
#### Fonction principale
def main():
    """
    Fonction principale : teste et affiche les nombres premiers jusqu'à 100.
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
