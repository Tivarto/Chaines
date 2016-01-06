# coding: utf-8
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)
    #1 pwd contient tous les caractères de la variable password sous forme d'une liste.
    found = False
    i=len(pwd)-1

    if(password == 'zzzzz'):
        raise ValueError('Pas de mot de passe suivant pour zzzzz')

    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)
           #2 la fonction ord() retourne le code ascii du caractère passé en paramètre.
           #On incrémente ensuite ce code de 1 pour obtenir la lettre suivante.
           found = True
        else:
           i = i-1
           pwd[i+1] = 'a'

    
    return ''.join(pwd)
    #3 On reconstruit une chaine de caractère en utilisant les lettres contenues dans le tableau pwd.

def hasSeries(password):

    pwd = list(password)
    i=0
    for i in range (0,len(pwd)-2):
        if(ord(pwd[i])+1==ord(pwd[i+1])):
            if(ord(pwd[i+1])+1==ord(pwd[i+2])):
                return True
    return False

def hasNoBadChar(password):
    pwd = list(password)
    i=0
    for i in range (0,len(pwd)):
        if(pwd[i] == 'i' or pwd[i] == 'l' or pwd[i] == 'o'):
            return False
    return True

def hasTwoPair(password):
    pwd = list(password)
    i=0
    pairnumber=0
    for i in range (0,len(pwd)-1):
        if(i+2<len(pwd)):
            if(ord(pwd[i])==ord(pwd[i+1]) and ord(pwd[i])!=ord(pwd[i+2])):
                pairnumber+=1
        elif(i+1<len(pwd)):
            if(ord(pwd[i])==ord(pwd[i+1])):
                pairnumber+=1
    if(pairnumber>1):
        return True
    else:
        return False


# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()