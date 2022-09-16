class A():
    def show(self):
        print("i am in show of A")

class B(A):
    def Display(self):
        print("I am in Display of B")


a = A()
a = B()
a.show()
a.Display()