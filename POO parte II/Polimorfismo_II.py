"""
Utilizando a técnica de Polimorfismo - Parte II

- Fazendo uma classe para criar métodos com informações de funcionários PJ e PF

"""


class Employee_pf:
    """
    Classe mãe - Possui todos os atributos principais, e que podem ser compartilhados

    """

    def __init__(self, id, name, age, kids):
        self.id = id
        self.name = name
        self.age = age
        self.kids = kids

    def __str__(self):
        """

        :return: Como __str__ eu tenho um método que retorna uma string,
        e o método atende a função de se tornar um polimorfismo

        """
        return f'id: {self.id}, name:{self.name} age:{self.age}, kids:{self.age}'


class Employee_pj(Employee_pf):

    def __init__(self, id, name, age, kids, company):
        super().__init__(id, name, age, kids)
        self.company = company

    def __str__(self):
        return f'id: {self.id}, name:{self.name}, ' \
               f'age:{self.age}, kids:{self.age} , company:{self.company}'


pj = Employee_pf(10163623, "Jade Picon", 22, 0)
pf = Employee_pj(10163024, "Arthur Aguiar", 30, 1, "Arthur & CIA")

employee = [pj, pf]

for value in employee:
    """
    Como utilizei o método __str__ nas funções, eu consigo pegar as informações diretamente da classe 
    """
    print('=' * 30)
    print(value)
    print('=' * 30)
