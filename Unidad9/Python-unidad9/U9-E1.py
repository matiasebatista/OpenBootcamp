listado = []
pais = ""
while pais != "No":
    pais = input("Coloca un país o pon No si quieres devolver los paises agregados")
    if pais == "No":
        break
    listado.append(pais)
    listado.sort()
print(f'Los paises que fueron colocados son:{set(listado)}')
