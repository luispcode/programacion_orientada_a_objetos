""" Herencia: copy paste
Polimorfismo: edit copy paste """

class Persona: #declaramos la clase

    def __init__(self, nombre): #Estructura inicial de una clase.
        self.nombre = nombre

    def avanza(self): #metodo avanzar.
        print('Ando caminando')


class Ciclista(Persona): #clase heredada de ciclista. la clase ciclista extends persona

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')


def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    main()