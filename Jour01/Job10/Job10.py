Montant_actuelle = 1000
Rendement_en_pourcentage = 2


Montant_actuelle = 1000
Rendement_en_pourcentage = 2

#Versement de 5000€
Montant_actuelle += 5000
Rendement_en_pourcentage += 2

#Augmentation des gain.
#ont divise le Rendement_en_pourcentage par 100 et ont le multiplie au montent initiale afin de calculer les gain.
Apres_augmentation = Montant_actuelle * (Rendement_en_pourcentage / 100)

#resultat.
print(f"Gain après augmentation : {Apres_augmentation:.2f} euros")

#L'investisseur retire 10% de sont compte.
Montant_actuelle -= 0.10 * Montant_actuelle
#L'investisseur perd 1%
Rendement_en_pourcentage -= 1

#Calcul du montant.
montant_final = Montant_actuelle * (1 - 0.01 + Rendement_en_pourcentage / 100)

print(f"Montant après retrait : {montant_final:.2f} euros")