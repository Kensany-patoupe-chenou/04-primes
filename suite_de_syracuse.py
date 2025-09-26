'''
Module qui retourne les suites de syracuse des valeur de n
'''
def syracuse(n):
    '''
    Retourne la liste de syracuse.

    Args:
        x: Nombre entier positif
        tv:Le plus petit indice tel que la variable associe est 1
        am:La valeur maximale de la suite
        tva:C'est le plus petit indice telque le nombre obtenue est le plus petit

    
    Returns:
        int: les trois metriques precedente.
    '''
    tv=0
    tva=0
    am=n
    x=n
    while x!=1:
        if x%2==0:
            x=x//2
        else:
            x=(x*3)+1
        am = max(am, x)
        if tva==0 and x<=n:
            tva=tv
        tv+=1
    return tv,tva,am


def main():
    """
    Fonction principale : Affiche les valeur de tv,am,tva et n.
    """
    n = 15
    tv, tva, am = syracuse(n)
    print(n, tv, tva, am)

if __name__ == "__main__":
    main()
