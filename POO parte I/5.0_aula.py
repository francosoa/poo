''''''''''
Usando Propriedades

Getters são os metodos que retornam o resultado de um metodo:
EX - Gostaria de saber o sa ldo da conta X, em vez de fazer um 
conta.extrato(), eu posso construir um metodo para isso.

def get_saldo(self):
    return self.__saldo
 
Setters: O set altera, coloca um novo valor. 
Ex: Gostaria de aumentar o valor do limite do cliente da conta

def set__limite(self, limite):
    self.__limite = limite  
'''''''''''

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

    def saca (self, valor):
        self.__saldo -= valor

    def transfere (self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def set_limite(self, limite):
        self.__limite = limite


