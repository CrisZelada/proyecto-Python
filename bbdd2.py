
import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#-----------------para leer info de la base de datos---------------

miCursor.execute("SELECT * FROM PRODUCTOS")#con la instruccion "select *" lo usamos para que nos devuelva todos los registros

variosProductos=miCursor.fetchall()#el método "fetchall" nos devuelve los registro de la instruccion "select * from"

for PRODUCTOS in variosProductos:
	#print(PRODUCTOS) o pdemos hacer de la siguiente manera
	print("El artículo: ", PRODUCTOS[0], "pertenece a la sección: ", PRODUCTOS[2])

miConexion.commit()

miConexion.close()

















