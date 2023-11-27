n = int(input("height : "))

underscore = "_"
slash = "/"
backslash = "\\"
space = " "

for i in range(1, n):
   print(" "*(n-i*1)+"/"+2*(i-1)*" "+"\\")
print("/"+2*(n-1)*"_"+"\\")
