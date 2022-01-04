'''''''''

Métodos privados e estásticos:



'''''''''


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo ... {}".format(self))
        self.__numero = numero #Quando eu coloco o self aqui, quero mostrar o caminho do meu objeto, e criar uma receita
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self): #esse é um metodo
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita (self, valor):
        self.__saldo += valor

    def pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))


    def transfere (self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def _saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
# toda vez que definimos um setter, obrigatoriamente temos que ter uma property(getter) antes
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
