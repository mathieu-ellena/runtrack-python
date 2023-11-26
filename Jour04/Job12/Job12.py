def tri_insertion(liste):
    n = len(liste)

    # Parcourir tous les éléments de la liste
    for i in range(1, n):
        cle = liste[i]
        j = i - 1

        # Déplacer les éléments de la liste [0..i-1] qui sont plus grands que 'cle' vers une position avant leur position actuelle
        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1

        liste[j + 1] = cle

# Exemple d'utilisation
ma_liste = [7, 11, 42, 39, 2]

# Afficher la liste avant le tri
print("Liste avant le tri :", ma_liste)

# Appeler la fonction de tri par insertion
tri_insertion(ma_liste)

# Afficher la liste après le tri
print("Liste après le tri :", ma_liste)
