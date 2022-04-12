class Pessoa:

    def __init__(self, nome, nascimento, idade, filhos, redes_sociais):
        self._nome = nome.title()
        self.nascimento = nascimento
        self.idade = idade
        self.filhos = filhos
        self.redes_sociais = redes_sociais
        self._seguidores = 0

    @property
    def seguidores (self):
        return self._seguidores

    def follow(self):
        self._seguidores += 2

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
          self._nome = value


class C(Pessoa):
    def __init__(self, nome, rua, numero):
        super().__init__(nome)
        self.rua = rua
        self.numero = numero

    def __str__(self):
        return (f'nome: {self.nome} - rua:{self.rua} - numero: {self.numero}')



person = Pessoa('francisco', '09-03-1995', 27, 3, 'instagram e face')
person.follow()
person.follow()

c = C('Francisco', 'rua comendador haroldo', 301321)




