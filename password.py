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



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()