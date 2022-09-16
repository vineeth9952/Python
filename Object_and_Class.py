
class Computer:
    def __init__(self,cpu,ram,memory):
        self.cpu = cpu
        self.ram = ram
        self.memory = memory

    def config(self):
        print("Configuaration is ",self.cpu,self.ram,self.memory)


com1 = Computer('I7',16,'1Tb')
com2 = Computer('I5',8,'500MB')

com1.config()
com2.config()






















