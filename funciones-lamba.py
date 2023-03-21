#FUNCIONES LAMBA tambien las encontramos como (on the go, online, on demand)

'''def area_triangulo(base,altura):

	return(base*altura)/2'''

#La funcion lamba no se usa nunca cuando hay condicionales o bucles para esos casos es la funcion tradicional
#se utilizan para funciones sencillas
#ejemplo 1A
area_triangulo=lambda base,altura: (base*altura)/2
print(area_triangulo(5,7))
print(area_triangulo(9,6))

#ejemplo 1B

tringulo1=area_triangulo(10,7)
tringulo2=area_triangulo(10,6)
print(tringulo1)
print(tringulo2)

#ejemplo 2A
#forma 1
al_cubo1=lambda numero:numero**3
print(al_cubo1(13))
#forma 2
al_cubo=lambda numero: pow(numero, 3)
print(al_cubo(13))

#ejemplo 3

euros=lambda comision:" Cristian tu comisión es: ¡u$s {} !".format(comision)
comisionCris= 15000
print(euros(comisionCris))