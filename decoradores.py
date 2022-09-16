
#Entendiendo el concepto de decorador

#Ejemplo decorador

def funcion_mayor():
	print("Esta es una función mayor y su mensaje de salida.")

	def librerias():
		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

	def frameworks():
		print("Algunos frameworks de Python son: Django, Dash y Flask.")

	frameworks()
	librerias()

# explicación:

#>>> funcion_mayor()
#Esta es una función mayor y su mensaje de salida.
#Algunos frameworks de Python son: Django, Dash y Flask.
# #Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.

#Ejemplo 2:

def funcion_decoradora(funcion):
	def wrapper():
        print("Este es el último mensaje...")
        funcion()
        print("Este es el primer mensaje ;)")
	return wrapper

#explicación:
#Lo que sucede es lo siguiente:
#>>> zumbido()
#Este es el último mensaje...
#Buzzzzzz
#Este es el primer mensaje ;)