def somme_valeurs_paires(liste):
    # Utiliser une compréhension de liste pour filtrer les valeurs paires
    valeurs_paires = [nombre for nombre in liste if nombre % 2 == 0]

    # Afficher la liste des valeurs paires
    print("Valeurs paires dans la liste :", valeurs_paires)

    # Calculer la somme des valeurs paires
    somme_paires = sum(valeurs_paires)
    print("Somme des valeurs paires :", somme_paires)

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Appel de la fonction pour calculer la somme des valeurs paires dans la liste
somme_valeurs_paires(L)