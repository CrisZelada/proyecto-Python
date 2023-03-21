import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#las tre comillas son para hacer en varias lineas
# PRIMARY KEY es para crear el codigo del articulo, es de tipo texto=varchar y su longitud=4 caracter
miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[

   ("AR01", "pelota", 20, "Juguetería"),
   ("AR02", "pantalón", 15, "Confección"),
   ("AR03", "destornillador", 25, "Ferretería"),
   ("AR04", "jarrón", 45, "Cerámica")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)", productos)



miConexion.commit()

miConexion.close()

