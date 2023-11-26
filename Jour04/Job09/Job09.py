def recuperer_infos_liste(liste):
    # Vérifier si la liste est vide
    if not liste:
        print("La liste est vide.")
        return

    # Récupérer la valeur, le maximum et le minimum des éléments de la liste
    valeur = liste[0]
    maximum = max(liste)
    minimum = min(liste)

    # Afficher les résultats
    print("Liste :", liste)
    print("Valeur :", valeur)
    print("Maximum :", maximum)
    print("Minimum :", minimum)

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Appel de la fonction pour récupérer les informations de la liste
recuperer_infos_liste(L)
