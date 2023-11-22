chaine_base = "abcdefghijklmnopqrstuvwxyz" * 10

longueur_pyramide = 10  # Vous pouvez ajuster cette valeur selon vos besoins

for i in range(1, longueur_pyramide + 1):
    sous_chaine = chaine_base[:i]
    print(sous_chaine.center(longueur_pyramide * 2 - 1))