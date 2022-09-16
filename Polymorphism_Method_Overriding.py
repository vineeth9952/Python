class A():
    def show(self):
        print("First show in class A")

class B(A):
    def show(self):
        print("First show in class B")

    def show(self):
        print("second show in class B")


obj = B()
obj.show()