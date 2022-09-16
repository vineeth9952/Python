class Grand_Father:
    def __init__(self):
        print("This is Grand Father's Init")

    def House(self):
        print("This is Grand father's House")

class Father(Grand_Father):
    def __init__(self):
        print("This is Father's Init")

    def Car(self):
        print("This is Father's Car")

class Son(Father):
    def __init__(self):
        print("This is Son's Init")

    def Bike(self):
        print("This is Son's Bike")

g = Grand_Father()
f = Father()
s = Son()
g.House()
f.House()
f.Car()
s.House()
s.Car()
s.Bike()