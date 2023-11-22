def saisir_entier_positif():
    while True:
        try:
            N = int(input("Veuillez saisir un entier supérieur à zéro (N) : "))
            if N > 0:
                return N
            else:
                print("Veuillez saisir un entier supérieur à zéro.")
        except ValueError:
            print("Veuillez saisir un entier valide.")

def afficher_tables_multiplication(N):
    print(f"Tables de multiplication de 1 à {N}:\n")
    
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i}:")
        for j in range(1, 11):
            produit = i * j
            print(f"{i} x {j} = {produit}")

if __name__ == "__main__":
    N = saisir_entier_positif()
    afficher_tables_multiplication(N)