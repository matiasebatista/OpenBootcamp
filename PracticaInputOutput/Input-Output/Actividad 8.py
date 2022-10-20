file = open('Prueba.txt', 'a', encoding='utf-8')
Palabras = [
    'primero\n',
    'segundo',
    'tercero\n',
    'cuarto',
    'quinto'
]

def escribe(fichero, datos):
    file = open(fichero, 'w')

    for linea in datos:
        if not linea.endswith('\n'):
            linea= linea +'\n'
        file.write(linea)
    file.close()


escribe('Prueba.txt', Palabras)


