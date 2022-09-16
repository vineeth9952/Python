
'''
    Protected members are denoted by using "_" before the name
    They can be accessed either inside the class or inside the subclass
    python allows the protected members to be accessed outside the class but you are not supposed to use like that
'''


class Electronics:
    __battery = "3000A"
    def __init__(self):
        self.__Gadget()  #Accessed inside the same class
        print(self.__battery)
        pass

    def IC(self):
        print("It needs a Processor")

    def __Gadget(self):
        print("Smart Watch")
        return "Gadget"

class Watches(Electronics):
    def __init__(self):
        self.__Gadget()  # cannot be Accessed using subclass
        print(self.__battery)
        pass

elec = Electronics()
wat = Watches()
