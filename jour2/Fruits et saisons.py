def fruitlegume(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange,mandarine et kiwi")
    elif  type == "fruits" and saison == "ete" :
        print("Poire,fraise,cassis")
    elif  type == "legume" and saison == "hiver" :
        print("carotte,topinambour,endive")
    elif type =="legume" and saison == "ete" :
        print("artichaud,aubergine,navet")

fruitlegume("fruits","hiver")
fruitlegume("fruits","ete")
fruitlegume("legume","hiver")
fruitlegume("legume","ete")