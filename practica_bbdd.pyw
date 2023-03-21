from tkinter import *
from tkinter import messagebox
import sqlite3


#-------------funciones--------------

def crearTabla():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	
	try:
		miCursor.execute('''
			CREATE TABLE DATOSUSUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50), 
	        PASSWORD VARCHAR(50),
	        APELLIDO VARCHAR(10),
	        DIRECCION VARCHAR(50),
	        COMENTARIO VARCHAR(100))
			''')
		messagebox.showinfo("BBDD", "Base de datos creada con éxito")
	except:
		messagebox.showwarning("¡Atención!", "La BBDD ya existe")


def salirAplicacion():

	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
	if valor == "yes":
		raiz.destroy()
		

def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	cuadroComentario.delete(1.0,END)#en el texto lo borramos con "delete" y le decimos q borre desde 
	#lo primero hasta la ultimo (1.0 hasta END)

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	
	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),cuadroComentario.get("1.0", END)
	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))
		

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con éxito")


def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())
	elUsuario=miCursor.fetchall()
	for usuarios in elUsuario:
		miId.set(usuarios[0])
		miNombre.set(usuarios[1])
		miPass.set(usuarios[2])
		miApellido.set(usuarios[3])
		miDireccion.set(usuarios[4])
		cuadroComentario.insert(1.0, usuarios[5])
	miConexion.commit()


def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	
	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),cuadroComentario.get("1.0", END)
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE=?, PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIO=?" +
	 "WHERE ID=" + miId.get(),(datos))  	
  	
	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro actualizado con éxito")


def eliminar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
	miConexion.commit()

	#messagebox.showinfo("BBDD", "Registro borrado con éxito")
	valor=messagebox.askquestion("Borrar", "¿Deseas eliminar el registro?")
	if valor == "yes":
		raiz.destroy()


raiz=Tk()

#----------------barra de menu------------------

barraMenu=Menu(raiz)#barraMenu es la variable que esta en la raiz
raiz.config(menu=barraMenu, width=300, height=300)#tamaño de la raiz

bbdd=Menu(barraMenu, tearoff=0)
bbdd.add_command(label="Conectar", command=crearTabla)
bbdd.add_command(label="Salir", command=salirAplicacion)

borrar=Menu(barraMenu, tearoff=0)
borrar.add_command(label="Borrar campos", command=limpiarCampos)

crud=Menu(barraMenu, tearoff=0)
crud.add_command(label="Crear", command=crear)
crud.add_command(label="Leer", command=leer)
crud.add_command(label="Actualizar", command=actualizar)
crud.add_command(label="Borrar", command=eliminar)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de....")

barraMenu.add_cascade(label="BBDD", menu=bbdd)

barraMenu.add_cascade(label="Borrar", menu=borrar)

barraMenu.add_cascade(label="CRUD", menu=crud)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#-----------cuerpo del programa (creamos el primer frame)-------

miFrame=Frame(raiz)
miFrame.pack()

miId=StringVar()#"StringVar" determina que la variable "miId"es de tipo cadena
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()


cuadroId=Entry(miFrame, textvariable=miId)#con el metodo "Entry" creamos un cuadro donde introducir text. 
# "textvariable" es otro metodo para identificar la variable declarada
cuadroId.grid(row=0, column=1, padx=10, pady=10)#el metodo "grid" divide en cuadricula nuestra interface grafica para poder colocar los widgest correctamente
cuadroId.config(fg="red", justify="center")#con este metodo colocamos el color de la letra y donde escribe 


cuadroNombre=Entry(miFrame, textvariable=miNombre)#con el metodo "Entry" creamos un cuadro donde introducir text. 
# "textvariable" es otro metodo para identificar la variable declarada
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)#el metodo "grid" divide en cuadricula nuestra interface grafica para poder colocar los widgest correctamente
cuadroNombre.config(fg="red", justify="center")#con este metodo colocamos el color de la letra y donde escribe 


cuadroPass=Entry(miFrame, textvariable=miPass)#con este metodo creamos un cuadro donde introducir text
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")


cuadroApellido=Entry(miFrame, textvariable=miApellido)#con este metodo creamos un cuadro donde introducir text
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)


cuadroDireccion=Entry(miFrame, textvariable=miDireccion)#con este metodo creamos un cuadro donde introducir text
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)


cuadroComentario=Text(miFrame, width=16, height=5)#con el metodo "Text" abrimos un widget donde escribir texto
cuadroComentario.grid(row=5, column=1, padx=10, pady=10)

scrollVertical=Scrollbar(miFrame, command=cuadroComentario.yview)# el "scroll" es la barra lateral que me permite subir y bajar, el "scroll" tambien puede ser horizontal
scrollVertical.grid(row=5, column=2, sticky="nsew")# "sticky="nsew" esto para que el scroll tome el tamaño del contenedor
cuadroComentario.config(yscrollcommand=scrollVertical.set)# el metodo "yscrollcommand" es para q el scroll se mueva con el cursor

#------------------aquí comienzan los label-------------------

idLabel=Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

passLabel=Label(miFrame, text="Contraseña: ")
passLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=5, column=0, sticky="w", padx=10, pady=10)

#-----------------botones (creamos un segundo frame para dividirlo en columnas)----------------

miFrame2=Frame(raiz)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=0, column=0, sticky="w", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=0, column=1, sticky="w", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=0, column=2, sticky="w", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar", command=eliminar)
botonBorrar.grid(row=0, column=3, sticky="w", padx=10, pady=10)

raiz.mainloop()










