class A:
    def __init__(self):
        print("init of A")

    def feature1(self):
        print("Feature 1")

class B(A):
    def __init__(self):
        super().__init__()
        print("init of B")

class C(B):
    def __init__(self):
        super().__init__()
        print("init of C")

c = C()