#definir clase.
class Coordenada:

    #este es el primer método de inicializacion.
    #inicializamos la estructura de la clase con el metodo constructor de instancias.
    def __init__(self, x, y): #hasta aquí lo que esta después de self, solo son parametros.
        self.x = x
        self.y = y # Aquí estamos inicializando las variables de instancia

    #Generamos un metodo que calcula la distancia.
    def distancia(self, otra_coordendada):
        x_diff = (self.x - otra_coordendada.x)**2
        y_diff = (self.y - otra_coordendada.y)**2

        return (x_diff + y_diff)**0.5 #en python **0.5 significa raiz cuadrada.

if __name__ == '__main__':

    #generamos instancias de la clase Coordenada.
    #estas dos expresiones son instancias que usan el molde que es el primer método de inicializacion.
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8) 

    #calculamos la distancia usando el metodo distancia de la clase Coordenada.
    print(coord_2.distancia(coord_1))
    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada))

    #"coord_1" hace uso de la primer instancia, mientras que coord_2 al 
    # estar dentro del metodo distancia, ocupa el lugar de otra_coordenada. 