class Food:
    Restuarent = "CMR Canteen"
    def __init__(self,starter,maincourse,dessert):
        self.starter = starter
        self.maincourse = maincourse
        self.dessert = dessert

    def show(self):
        print(self.starter, self.maincourse, self.dessert)

    @staticmethod #decorator
    def Display():
        print(" We are inside the Restuarent. ")

    @staticmethod
    def change():
        Food.Restuarent = "Bounce"

meal1 = Food("chicken_tikka","Biryani","gualb_jamun")
meal2 = Food("Manchuriyan","Mutton_biryani","Icecream")

print("Restuarent Name :- ",Food.Restuarent)
Food.change()
print("Restuarent Name :- ",Food.Restuarent)
Food.Display()

'''
===> a static method doesnt have implicit first argument
===> it has a decorator @staticmethod above it.
===> it is bound to class not the object of class   
===> it cant modify the state of class 

'''