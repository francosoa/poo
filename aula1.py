#Primeira aula de Programação Orientada a Objeto

#Abaixo temos um exemplo de função normal, que não é orientada a objeto

def criar_conta (numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo":saldo, "limite":limite}
    return conta

def deposita (conta, valor):
    conta["saldo"] += valor

def saca (conta, valor):
    conta["saldo"] -= valor

def extrato (conta):
    print("Seu saldo é {}".format(conta["saldo"]))



