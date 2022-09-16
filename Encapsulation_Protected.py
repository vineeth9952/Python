
'''
    Protected members are denoted by using "_" before the name
    They can be accessed either inside the class or inside the subclass
    python allows the protected members to be accessed outside the class but you are not supposed to use like that
'''


class Electronics:
    _battery = "3000A"
    def __init__(self):
        self._Gadget()  # Accessed using class
        print(self._battery)

    def IC(self):
        print("It needs a Processor")

    def _Gadget(self):
        print("Smart Watch")

class Watches(Electronics):
    def __init__(self):
        self._Gadget()  # Accessed using subclass
        print(self._battery)


elec = Electronics()
wat = Watches()
