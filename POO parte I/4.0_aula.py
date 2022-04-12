"""""
Encapsulamento - Atributos provados:
 O __ antes do atributo permite que métodos e atributos sejam acessados apenas dentro da classe;
 
 
Falamos nessa aula sobre a coesão que é ligado ao principio de responsabilidade única. 
Aprendemos que uma classe deve ter apenas uma responsabilidade 
(ou deve ter apenas uma razão para existir). 
Em outras palavras, ela não deve assumir responsabilidades que não são delas.

Além desse princípio de responsabilidade única existem outras que foram definidos através do Robert C. Martin no início dos anos 2000 e são conhecidos pelo acrônimo SOLID:

S - Single responsibility principle
O - Open/closed principle
L - Liskov substitution principle
I - Interface segregation principle
D - Dependency inversion principle
"""""

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
