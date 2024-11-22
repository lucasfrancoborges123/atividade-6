from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nome, idade):
        self.__nome=nome
        self.__idade=idade
        
    def getnome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome=nome
    
    def getidade(self):
        return self.__idade
    def setIdade(self, idade):
        self.__idade=idade
        
    @abstractmethod
    def mostar(self):
        pass 
