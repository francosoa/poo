#As funções dentro do mundo de objetos são chamadas de método
#Metodo = O que a função sabe fazer

#
#
#


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo ... {}".format(self))
        self.numero = numero #Quando eu coloco o self aqui, quero mostrar o caminho do meu objeto, e criar uma receita
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self): #esse é um metodo
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita (self, valor):
        self.saldo += valor

    def saca (self, valor):
        self.saldo -= valor


