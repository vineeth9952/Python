class Mother:
    def __init__(self):
        print("This is Mother's Init")

    def Gold(self):
        print("This is Mother's Gold")

class Father:
    def __init__(self):
        print("This is Father's Init")

    def Car(self):
        print("This is Father's Car")

class Son(Father,Mother):
    def __init__(self):
        print("This is Son's Init")

    def Bike(self):
        print("This is Son's Bike")

m = Mother()
f = Father()
s = Son()
m.Gold()
f.Car()
s.Gold()
s.Car()
s.Bike()