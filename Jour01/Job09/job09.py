Nom_du_prodruit = "yaourt"
Prix_unitaire = 3 
En_stock = 50

#le "f" placer ici est un f-string est sert a formater une chaine de character.
print(f"Produit:{Nom_du_prodruit}.")
print(f"Montant a paye:{Prix_unitaire}€")
print(f"En stock:{En_stock}")
#\n pour sauter une ligne.
vendeur = int(input("\nBonjours Combien d'article desirer vous ?:"))
#-= sert soustraire la valeur dune variable a une autre.
En_stock -= vendeur

#*= sert a multiplier une valeur numerique en locurence de 10% dans ce cas.
Prix_unitaire *= 1.1

print("\nInformation apres l'achat au sujet de l'inflation:")
print(f"Nom du produit : {Nom_du_prodruit}")
print("Iflation de 10%")
print("\n...")
#le .2 dit au terminale dafficher seulment de chifre apres la virgule
#le f apres les : indique  que ces un nombre a virgule flotant
print(f"prix unitaire apres inflation : {Prix_unitaire: .2f}€")
print(f"Quantité en stock : {En_stock} unités")
