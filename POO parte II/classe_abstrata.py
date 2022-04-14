"""
Clases abstratas fornecem um modelo para classes concretas

- A classe abstrata não pode ser instanciada;
- As subclasses derivadas da classe abstrata devem possuir os métodos herdados
"""
#Criando uma classe abstrata:
from abc import ABCMeta, abstractmethod
import pandas as pd

class AbstractClassCSV (metaclass= ABCMeta):
    """Dentro da classe abstrata forçamos as subclasses a utilizar as propriedades abaixo"""

    def __init__(self, path, file_name):
        self._path = path
        self._file_name = file_name
        pass

    @property
    @abstractmethod
    def path(self):
        pass

    @path.setter
    @abstractmethod
    def path(self, value):
        pass

    @property
    @abstractmethod
    def file_name (self):
        pass

    @file_name.setter
    @abstractmethod
    def file_name (self):
        pass

"""Criando uma subclasse concreta derivada de uma classe abstrata"""

class GetCSVinfo(AbstractClassCSV): #herdando a minha classe abstrata

    @property
    def path(self):
        print("Getting value of path")
        return self._path

    @path.setter
    def path(self, value):
        if '/' in value:
            self._path = value
            print("Setting value of path to {}".format(value))
        else:
            print("the value {} is incorrect".format(value))

    @property
    def file_name(self):
        print("Getting value of file...")
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if '.' in value:
            self._file_name = value
            print("Your file name is {}".format(value))
        else:
            print("The value of your file name {} is incorrect".format(value))

    def display_summary(self):
        data = pd.read_csv(self._path + self._file_name)
        print(self._file_name)
        print(data.info())

if __name__ == '__main__':
#Colocando as informações do meu local user
    csv = GetCSVinfo("C:/Users/localuser/jupyter/", "car_evaluation.csv")
    csv.display_summary()
