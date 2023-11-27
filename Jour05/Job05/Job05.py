def decale_cesar(message, decalage):
    message_decale = ""
    for lettre in message:
        if lettre.isalpha():
            # Gestion du dépassement pour les lettres minuscules
            if lettre.islower():
                nouvelle_lettre = chr((ord(lettre) - ord('a') + decalage) % 26 + ord('a'))
            # Gestion du dépassement pour les lettres majuscules
            else:
                nouvelle_lettre = chr((ord(lettre) - ord('A') + decalage) % 26 + ord('A'))
            message_decale += nouvelle_lettre
        else:
            # Si ce n'est pas une lettre, ajoutez directement au message décalé
            message_decale += lettre
    return message_decale

# Exemple d'utilisation
message_original = "Hello, World!"
decalage = 3
message_decale = decale_cesar(message_original, decalage)
print(f"Message original : {message_original}")
print(f"Message décalé de {decalage} : {message_decale}")
