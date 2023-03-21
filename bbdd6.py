#en este ejemplo vamos a utilizar las operacione de tipo CRUD

import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#----------de esta forma vemos lo que hay en la tabla------------
#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección'")
#productos=miCursor.fetchall()
#print(productos)

#-----------ahora modificamos o actualizar la tabla-----------
#hay que decirle que queremos modificar y que seccion de ese articulo

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

#---------------ahora vemos como se borra algo de la tabla DELETE----------
#con el método DELETE hay q tener mucho cuidado en indicar especificamente que queremos borrar por q podemos
#borrar todo lo que contenga el mismo nombre o precio u otra cosa de la base de datos y no hay como rescatar 

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miConexion.commit()

miConexion.close()

#la clausula "WHERE" es para ver una sección determinada
#hay que tener en cuenta los acentos y si esta en mayúscula o miníscula 
#con el "print" vemos los q contiene la lista en esa sección


