
#####
#  Antes de termos um objeto, devemos definir as suas características..
###

# Uma classe é uma especificação de um tipo, definindo valores e comportamentos.
#Para criar uma instância, é obrigatório preencher os valores de todos os atributos.
#Uma boa analogia é considerar a classe como a receita para a criação de algum prato;
# por exemplo, um delicioso bolo de cenoura ;-)


#as variáveis criadas para armanezar os objetos são chamadas de referências

# Função construtora é quando no def tem dois __
#O self dentro do __init__(Self) é a referência que sabe onde está o nosso objeto

#As caracteristicas de uma classe são chamadas de atributos.

#Definir uma receita:

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo ... {}".format(self))
        self.numero = numero #Quando eu coloco o self aqui, quero mostrar o caminho do meu objeto, e criar uma receita
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

#Nessa parte atribuimos a classe a uma referência
conta = Conta

#Nessa parte eu coloco um atributo dentro do objeto
conta = Conta(123, "João", 100 , 15000)

#Acesso o atributo
print(conta.titular)

