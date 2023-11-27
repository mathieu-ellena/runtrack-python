def display_diagonal_line(n):
    for i in range(n+1):
        for j in range(n-1):
            if i == j:
                print(" ", end="")
            else:
                print("#", end="")
        print()


length = int(input("Enter the length: "))
display_diagonal_line(length)