from abc import ABC,abstractmethod

class Game(ABC):
    def start(self):
        print(f"{self.__class__.__name__} is started")

    @abstractmethod
    def move(self):
        pass
    
    def stop(self):
         print(f"{self.__class__.__name__} is stopped")

'''concrete class'''
class Bike(Game):
    def move(self):
        print("Bike can move forward direction only...")

game = Bike
game.start()
game.move()
game.stop()



    
