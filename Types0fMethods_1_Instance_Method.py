class Food:
    def __init__(self,starter,maincourse,dessert):
        self.starter = starter
        self.maincourse = maincourse
        self.dessert = dessert

    def show(self):#instance method
        print(self.starter, self.maincourse, self.dessert)

    def get_maincourse(self):#getter method or Accessor
        return self.maincourse

    def set_maincourse(self,newmaincourse):
        self.maincourse = newmaincourse


meal1 = Food("chi   cken_tikka","Biryani","gualb_jamun")
meal2 = Food("Manchuriyan","Mutton_biryani","Icecream")

print(meal1.get_maincourse())
meal1.set_maincourse("Fish_man")
print(meal1.get_maincourse())

'''
===> It contains keyword "self" as Default first Implicit Argument
===> An Instance method is bound to the object of the class.
===> An instance method is created to be used by the class members 
    or the objects
===> An Instance method can be invoked(called) using the object of the
    particular class.
'''