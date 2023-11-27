def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            # Si la note est inférieure à 40, l'étudiant échoue et la note n'est pas arrondie
            notes_arrondies.append(note)
        else:
            # Si la note est supérieure ou égale à 40, vérifier les critères d'arrondissement
            difference_multiple_5 = note % 5
            if difference_multiple_5 >= 3:
                # Si la différence entre la note et le prochain multiple de 5 est de 3 ou plus, arrondir à ce multiple
                note_arrondie = note + (5 - difference_multiple_5)
            else:
                # Sinon, la note reste la même
                note_arrondie = note

            notes_arrondies.append(note_arrondie)

    return notes_arrondies

# Exemple d'utilisation
liste_notes = [78, 42, 55, 93, 37]
notes_arrondies = arrondir_notes(liste_notes)

# Affichage du résultat
print(f"Notes originales : {liste_notes}")
print(f"Notes arrondies   : {notes_arrondies}")
