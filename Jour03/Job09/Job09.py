def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

moyenne_etudiant = moyenne(note1, note2, note3)

print("La moyenne de l'étudiant est :", moyenne_etudiant)

if 15 <= moyenne_etudiant <= 20:
    print("T'es pas si spécial mais bien joué'.")
elif 11 <= moyenne_etudiant <= 14:
    print("Bien joué tu as dépassé 23% de la population.")
elif 8 <= moyenne_etudiant <= 10:
    print("Bof, tu n'as rien de spécial.")
elif 0 <= moyenne_etudiant <= 7:
    print("T'es un merde Timy.")
else:
    print("Moyenne invalide.")