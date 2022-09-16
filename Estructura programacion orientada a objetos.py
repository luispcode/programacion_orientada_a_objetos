class Hotel: #definir una clase.
    pass
#Generar una instancia llamando al constructor de la clase.

hotel = Hotel()


#Atributos de la instancia.
# Todas las clases crean objetos y todos los objetos tienen atributos. 
# Utilizamos el método especial __init__ para definir el estado inicial 
# de nuestra instancia. Recibe como primer parámetro obligatorio 
# self (que es simplemente una referencia a la instancia).

class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0


hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
print(hotel.lugares_de_estacionamiento) # 20

# Métodos de instancia

# Mientras que los atributos de la instancia describen lo que representa el objeto, 
# los métodos de instancia nos indican qué podemos hacer con las instancias de dicha 
# clase y normalmente operan en los mencionados atributos. Los métodos son equivalentes 
# a funciones dentro de la definición de la clase, pero todos reciben self como primer argumento.

class Hotel:

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes


hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() # 2