import random


class Pessoa:

    def __init__(self, nome, nascimento, idade, filhos, redes_sociais):
        self._nome = nome.title()
        self.nascimento = nascimento
        self.idade = idade
        self.filhos = filhos
        self.redes_sociais = redes_sociais
        self.__seguidores = 0

    @property
    def seguidores (self):
        return (self.__seguidores + 3) * (self.__seguidores + random.random())


    @property

    def nome(self):
        return self._nome

    @nome.setter

    def nome(self, value):
          self.__nome = value


nome_2 = Pessoa('francis', '09-03-1995', 27, 3, 'instagram e face')
print(f' nome: {nome_2.nome}, nascimento: {nome_2.nascimento}, idade:{nome_2.idade}, redes_sociais: {nome_2.redes_sociais}, {nome_2.seguidores}' )



