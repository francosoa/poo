"""Classe Bola: Crie uma classe chamada bola, e crie
um método de circuferência """

class Ball:

    def __init__(self, color, raio, mater):
        self.__color = color
        self.__raio = raio
        self.mater = mater

    @property
    def mostra_cor (self):
        return print(f'A cor da bola é {self.__color.title()}')

    @property
    def circuferência (self):
        circ = (2 * 3.14) * self.__raio
        return print(f'A circuferência da sua bola é {circ}')

    @property
    def colour(self):
        return self.__color

    @colour.setter
    def colour(self, value):
         self.__color = value.title()



ball = Ball("Azul", 18, "Plástico")
print('=' * 30)
print(f'{ball.mostra_cor}, {ball.circuferência} and the material is {ball.mater}')
print('=' * 30)
