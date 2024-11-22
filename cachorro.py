from animal import Animal
class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte=porte
        
    def setporte(self, porte):
        self.__porte=porte
    def getporte(self):
        return self.__porte
    def mostar(self):
        return (f"O animal se chama: {self.getnome()}, idade {self.getidade()}, Porte: {self.getporte()}")
    
