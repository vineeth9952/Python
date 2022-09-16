class Pycharm:
    def Execute(self):
        print("compiling")
        print("running")

class Editor:
    def Execute(self):
        print("spell check")
        print("Convention checking")
        print("compiling")
        print("running")

class Laptop:
    def Code(self,ide):
        ide.Execute()#obj1.Execute()

obj = Pycharm()
obj1 = Editor()
lap = Laptop()
lap.Code(obj1)