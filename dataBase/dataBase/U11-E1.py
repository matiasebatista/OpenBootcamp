import sqlite3

dataBase = sqlite3.connect('Alumnos.db')
prueba = dataBase.cursor()

prueba.execute('''CREATE TABLE IF NOT EXISTS tabla1(ID int, NOMBRE text, APELLIDO text)''')



prueba.execute("INSERT INTO tabla1 VALUES(1,'jose','ramos')")
prueba.execute("INSERT INTO tabla1 VALUES(2,'jose','ramos')")
prueba.execute("INSERT INTO tabla1 VALUES(3,'alba','perez')")
prueba.execute("INSERT INTO tabla1 VALUES(4,'gabriel','lopez')")
prueba.execute("INSERT INTO tabla1 VALUES(5,'laura','ramirez')")
prueba.execute("INSERT INTO tabla1 VALUES(6,'lucas','ramirez')")
prueba.execute("INSERT INTO tabla1 VALUES(7,'camila','lopez')")
prueba.execute("INSERT INTO tabla1 VALUES(8,'matias','ceballos')")
dataBase.commit()
prueba.execute("SELECT * FROM tabla1")
primeralumno= prueba.fetchone()
print(primeralumno)
traervarios = prueba.fetchmany(3)
print(traervarios)
print(prueba.fetchall())

dataBase.close()

