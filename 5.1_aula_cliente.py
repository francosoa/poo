
'''''''''
Os getters e setters muitas vezes são usados para impedir que 
determinadas variáveis sejam alteradas, ou validar o valor antes de atribuir a variável, 
ou ainda processar um valor a partir de outras variáveis. 
Porém como o Python incentiva o acesso direto as variáveis, 
existe a property, que ao tentar acessar uma variável ou alterar um valor, uma função é chamada.
'''''''''

class Cliente:
    def __init__(self, nome):
        self.nome = nome

    @property
    def saldo(self):
        return self.__saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
