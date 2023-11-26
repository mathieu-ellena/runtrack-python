def calcule(num1, operator, num2):

		#addition

    if operator == "+":
        return num1 + num2

        #soustraction

    elif operator == "-":
        return num1 - num2

        #multiplication

    elif operator == "*":
        return num1 * num2

        #division

    elif operator == "/":
    	return num1 / num2

    	#exemple de paramètre

addition = calcule(5, "+", 3)
soustraction = calcule(8, "-", 2)
multiplication = calcule(4, "*", 7)
division = calcule(6, "/", 2)


print(f"Résultat de l'addition : {addition}")
print(f"Résultat de la soustraction : {soustraction}")
print(f"Résultat de la multiplication : {multiplication}")
print(f"Résultat de la division : {division}")