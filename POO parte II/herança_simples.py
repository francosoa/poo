"Trabalhando com Herança para diminuir a redundância do código:"

class Employee_pf:

    """
    Classe mãe - Possui todos os atributos principais, e que podem ser compartilhados

    """
    def __init__(self, id, name, age, kids):
        self.id = id
        self.name = name
        self.age = age
        self.kids = kids

class Employee_pj (Employee_pf):
    """
    Classe filha - Possui os métodos da mãe, e uma particularidade que é a company

    """

    def __init__(self, id, name, age, kids, company):
        super().__init__(id, name, age, kids)
        self.company = company


pj = Employee_pj(12, "João", 12, 1, "Consultoria")
