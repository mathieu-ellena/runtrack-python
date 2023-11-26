def produit_dans_intervalle(liste, borne_inf, borne_sup):
    # Utiliser une compréhension de liste pour filtrer les valeurs dans l'intervalle
    valeurs_intervalle = [nombre for nombre in liste if borne_inf <= nombre <= borne_sup]

    # Vérifier si la liste résultante n'est pas vide
    if not valeurs_intervalle:
        print(f"Aucune valeur trouvée dans l'intervalle [{borne_inf}, {borne_sup}]")
        return

    # Calculer le produit des valeurs dans l'intervalle
    produit = 1
    for valeur in valeurs_intervalle:
        produit *= valeur

    # Afficher les résultats
    print("Liste dans l'intervalle :", valeurs_intervalle)
    print("Produit des valeurs dans l'intervalle :", produit)

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Bornes de l'intervalle
borne_inf = 25
borne_sup = 90

# Appel de la fonction pour calculer le produit des valeurs dans l'intervalle
produit_dans_intervalle(L, borne_inf, borne_sup)
