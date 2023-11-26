def main():
    # Création de la liste d'au moins 5 entiers
    L = [1, 2, 3, 4, 5]

    # Afficher la deuxième valeur de la liste
    print("Deuxième valeur de la liste :", L[1])

    # Appeler la fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
    remplacer_par_somme_voisins(L)

    # Afficher le tableau après la modification
    print("Tableau après modification :", L)

    # Afficher la dernière valeur de la liste
    print("Dernière valeur de la liste :", L[-1])

def remplacer_par_somme_voisins(liste):
    # Assurer que la liste a au moins 5 éléments
    if len(liste) >= 5:
        # Remplacer L[3] par la somme des cases voisines L[2] & L[4]
        liste[3] = liste[2] + liste[4]

# Appel de la fonction principale
main()
