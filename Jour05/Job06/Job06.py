def distance_toilettes_par_semaine(nombre_marches, hauteur_marche):
    nombre_jours_semaine = 7
    nombre_allers_retours_par_jour = 2  # Un aller et un retour à chaque visite aux toilettes

    distance_marchee_par_jour = nombre_allers_retours_par_jour * hauteur_marche * nombre_marches
    distance_marchee_par_semaine = distance_marchee_par_jour * nombre_jours_semaine / 100  # Convertir en mètres

    return distance_marchee_par_semaine

# Exemple d'utilisation
nombre_marches = 10
hauteur_marche = 20
distance_totale = distance_toilettes_par_semaine(nombre_marches, hauteur_marche)

# Affichage du résultat
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")
