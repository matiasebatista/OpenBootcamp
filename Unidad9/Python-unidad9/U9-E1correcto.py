listado =[]
paisesColocados = input("Coloca tu lista de paises separados por ,: ")
paises = paisesColocados.split(",")
listado= sorted(set(paises))
print(listado)