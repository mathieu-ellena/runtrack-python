x = int(input("length: "))
y = int(input("width: "))

dash = "-"
pipe = "|"

for i in range(1, x+1):
    for j in range(1, y+1):
        if i == 1 or i == x:
            print(dash, end="")
        elif j == 1 or j == y:
            print(pipe, end="")
        else:
            print(" ", end="")
    print()
