def echanger_premier_et_dernier(liste):
    # Vérifier si la liste est non vide
    if liste:
        # Échanger les valeurs de la première et de la dernière case
        liste[0], liste[-1] = liste[-1], liste[0]
        return liste
    else:
        print("La liste est vide.")

# Exemple d'utilisation
ma_liste = [1, 2, 3, 4, 5]
print("Liste avant l'échange :", ma_liste)

# Appel de la fonction pour échanger les valeurs
nouvelle_liste = echanger_premier_et_dernier(ma_liste)

# Afficher le résultat
print("Liste après l'échange :", nouvelle_liste)
