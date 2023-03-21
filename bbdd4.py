import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


#aca agregamos un articulo a  nuestra lista 

miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR05', 'tren', 15, 'Jugueteria')")



miConexion.commit()

miConexion.close()

