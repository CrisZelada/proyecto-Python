
import sqlite3

#-------------paso para crear la base de datos--------------
#crear la base de datos y abrirla se hacen en un únoco paso
#el 1 paso creamos una conexion que le llamamos "miConexxion" o como quieras llamarlo
# y lo creamos con el método "connect" de la libreria sqlite3
miConexion=sqlite3.connect("PrimeraBase")

#el 2paso es crear el puntero q lo llamamos "miCursor" es una variable objeto, 
#q puede llaamrse de cualquier forma
#el puntero es un espacio en memoria q almacena datos, para hacer consulta y manejar resultados
miCursor=miConexion.cursor()

#el 3 paso es ejecutar el query= consulta
#"execute" es el metodo para crear la consulta y dentro del parentesis va el parametro
#dentro del parentesis se escribe en el lenguaje de base de datos q debo conocer

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") 
#IMPORTANTE cada vez que creamos la tabla la invalidamos comentando para q al ejecutar no intente crear otra tabla

# el 4 paso es cargar datos a la tabla

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")
#el método "execute" es para ejecutar de a uno
#en esta linea agregamos un articulo a nuetra base de datos 
#ahora lo comentamos para seguir con el trabajo

variosProductos=[#esto es una lista y dentro van las tuplas
              
     ("Camiseta", 10, "Deportes"),#estas son tuplas
     ("Jarrón", 90, "Cerámicas"),
     ("Camión", 50, "Juguetería")


]
#el metodo "executemany" es para ejecutar muchos
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)
#los signos de "?" hay que colocar las mismas cantidad de columnas de nuestra lista en este caso 3: "producto", "precio" y "seccion"



miConexion.commit()#el método "commit" es para confirmar el cambio que hemos hecho


miConexion.close()#de esta manera cerramos la creacion de la base de datos
