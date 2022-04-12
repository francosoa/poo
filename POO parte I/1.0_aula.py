""""

Aula 1: O que é POO?

Na programação procedural, o código é colocado em funções ou procedimentos totalmente distintos, 
já no paradigma OO os atributos e comportamentos estão contidos dentro de um único objeto, 
ao passo que no projeto procedural ou estruturado, os atributos e comportamentos estão normalmente separados.

O código abaixo conta com uma programação procedual:
""""



def criar_conta (numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo":saldo, "limite":limite}
    return conta

def deposita (conta, valor):
    conta["saldo"] += valor

def saca (conta, valor):
    conta["saldo"] -= valor

def extrato (conta):
    print("Seu saldo é {}".format(conta["saldo"]))



