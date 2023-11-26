def afficher_deuxieme_element():
    fruits = ["pomme", "cerise", "orange"]
    
    # Assurez-vous que la liste a au moins deux éléments
    if len(fruits) >= 2:
        deuxieme_element = fruits[1]
        print("Le deuxième élément de la liste est :", deuxieme_element)
    else:
        print("La liste ne contient pas assez d'éléments pour afficher le deuxième.")

# Appel de la fonction
afficher_deuxieme_element()