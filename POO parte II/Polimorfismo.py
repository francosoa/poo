"""
Utilizando a técnica de Polimorfismo - Parte I
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

    def print_for_me (self):
        return f'id: {self.id}, name:{self.name} age:{self.age}, kids:{self.age}'


class Employee_pj(Employee_pf):
    """
    Classe filha - Possui os métodos da mãe, e uma particularidade que é a company

    """

    def __init__(self, id, name, age, kids, company):
        super().__init__(id, name, age, kids)
        self.company = company


    def print_for_me (self):
        """
        :return: Retorna um metódo de polimorfismo
        """
        return f'id: {self.id}, name:{self.name}, ' \
               f'age:{self.age}, kids:{self.age} , company:{self.company}'


pj = Employee_pf (10163623, "Jade Picon", 22, 0)
pf = Employee_pj (10163024, "Arthur Aguiar", 30, 1, "Arthur & CIA")

employee = [pj, pf]

for value in employee:
    print('=' * 30)
    print(value.print_for_me())
    print('=' * 30)


"""
Débito Técnico:

Dessa forma consegui utilizar o polimorfismo, mas ainda não é o melhor método
"""