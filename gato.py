from animal import Animal
class Gato (Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca=raca
        
    def setraca(self, raca):
        self.__raca=raca
    def getraca(self):
        return self.__raca
    def mostar(self):
        return (f"O animal se chama: {self.getnome()}, idade {self.getidade()}, Raça: {self.getraca()},")
