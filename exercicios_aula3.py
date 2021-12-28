
"""

Desafio da aula número 3

Lançamos o seguinte desafio: para ajudar na formatação de datas você deve criar uma nova classe auxiliar. Essa classe deve representar uma Data (sem hora) que sabe imprimir uma data formatada. Ela deve funcionar dessa forma:

from exercicios_aula3 import Data
d = Data(21,11,2007)
d.formatada()COPIAR CÓDIGO
Imprime:

21/11/2007

"""

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada (self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))


## Para fazer no console:

from exercicios_aula3 import Data

d = Data(21,11,2020)
d.formatada()

#Resultado:
#O output foi como o esperado

