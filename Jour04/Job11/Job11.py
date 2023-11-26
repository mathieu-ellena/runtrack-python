def augmenter_elements_liste(liste):
    # Afficher la liste d'origine
    print("Liste d'origine :", liste)

    # Augmenter de 1 la valeur de chaque élément de la liste
    for i in range(len(liste)):
        liste[i] += 1

    # Afficher la liste modifiée
    print("Liste après augmentation de 1 :", liste)

# Créer la liste d'entiers
L = [7, 11, 42, 39, 2]

# Appel de la fonction pour augmenter de 1 la valeur de chaque élément
augmenter_elements_liste(L)
