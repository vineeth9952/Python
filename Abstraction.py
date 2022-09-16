#Abstraction = Hiding the functionality(behaviour)
#An Abstract class cannot be instantiated i.e., we cannot create an object for the abstract class
#An Abstract class can contain normal methods and Abstract mehtods.
#Concrete(normal) classes cannot have abstract methods
from abc import ABC,abstractmethod

class Factory(ABC):
    @abstractmethod
    def Goods(self):#abstract method
        pass

    def Trasportation(self):#normal method
        print("Trucks are used for Trasporting")

class ChocolateFactory(Factory):

    def Goods(self):
        print("Chocolate are made in this factory")

class CokeFactory(Factory):
    def Goods(self):
        print("Coke is made in this factory")

choc = ChocolateFactory()
choc.Goods()
ck = CokeFactory()
ck.Goods()
ck.Trasportation()