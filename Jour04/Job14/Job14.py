def est_separateur(c):
    # Vérifie si le caractère est un séparateur (espace, virgule, point, etc.)
    return c == ' ' or c == ',' or c == '.' or c == ';' or c == ':' or c == '?' or c == '!' or c == '(' or c == ')'

def my_long_word(longueur_min, texte):
    mot_actuel = ""
    mots_plus_longs = ""

    for caractere in texte:
        if not est_separateur(caractere):
            # Ajouter le caractère au mot actuel
            mot_actuel += caractere
        elif len(mot_actuel) > longueur_min:
            # Ajouter le mot actuel aux mots plus longs
            mots_plus_longs += mot_actuel + " "
            mot_actuel = ""
        else:
            # Réinitialiser le mot actuel
            mot_actuel = ""

    # Ajouter le dernier mot s'il est plus long que la longueur minimale
    if len(mot_actuel) > longueur_min:
        mots_plus_longs += mot_actuel

    return mots_plus_longs

# Exemple d'utilisation
longueur_minimale = 3
texte_exemple = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(longueur_minimale, texte_exemple)
print("Output :", resultat)
