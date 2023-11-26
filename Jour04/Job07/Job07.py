def compter_multiples_de_trois(liste):
    # Utiliser une compréhension de liste pour filtrer les multiples de 3
    multiples_de_trois = [nombre for nombre in liste if nombre % 3 == 0]

    # Afficher la liste des multiples de 3
    print("Multiples de 3 dans la liste :", multiples_de_trois)

    # Afficher le nombre de multiples de 3
    nombre_de_multiples = len(multiples_de_trois)
    print("Nombre de multiples de 3 :", nombre_de_multiples)

# Liste donnée
L = [8, 24, 48, 2, 16]

# Appel de la fonction pour compter les multiples de 3 dans la liste
compter_multiples_de_trois(L)
