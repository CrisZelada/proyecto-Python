#en este ejemplo vamos a automatizar la cracion del código del articulo

import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#"ID" junto con "AUTOINCREMENT" es para q automaticamente agregue codigo a los articulos ingresados incrementandose de manera automatica
miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[

   ("pelota", 20, "Juguetería"),
   ("pantalón", 15, "Confección"),
   ("destornillador", 25, "Ferretería"),
   ("jarrón", 45, "Cerámica"),
   ("pantalones", 35, "Confección")

]

#la palabra reservada NULL va a reemplazar al signo para crear el espacio donde va el código del articulo
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)



miConexion.commit()

miConexion.close()

#el metodo UNIQUE es para q no se pueda repetir este campo y se puede utilizar donde necesite