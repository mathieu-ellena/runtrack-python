def supprimer_doublons(liste):
    liste_unique = []

    for element in liste:
        # Vérifier si l'élément est déjà dans la liste unique
        if element not in liste_unique:
            liste_unique.append(element)

    return liste_unique

# Exemple d'utilisation
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Afficher la liste avant la suppression des doublons
print("Liste avant la suppression des doublons :", ma_liste)

# Appeler la fonction pour supprimer les doublons
liste_sans_doublons = supprimer_doublons(ma_liste)

# Afficher la liste après la suppression des doublons
print("Liste après la suppression des doublons :", liste_sans_doublons)
