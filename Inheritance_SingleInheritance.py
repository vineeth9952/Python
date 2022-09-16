
class Father:
    def Car(self):
        print("This is Father's Car")

class Son(Father):
    def Bike(self):
        print("This is Son's Bike")

f = Father()
s = Son()
f.Car()
s.Car()
s.Bike()