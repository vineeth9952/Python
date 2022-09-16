'''
a = '5'
b = '6'
print(a+b)#synthetic sugar
print(str.__add__(a,b))#magic method
magic methods
__add__()
__sub__()
__mul__()
'''

class Student:
    def __init__(self,c,java,python):
        self.c = c
        self.java = java
        self.python = python



    def __gt__(self, other):
        a = self.c + self.java + self.python
        b = other.c + other.java + other.python
        if a>b:
            return True
        else:
            return False

Anand =  Student(99,12,80)
Mujahid = Student(100,50,85)

if Anand>Mujahid:
    print("Anand scored more marks")
else:
    print("Mujahid Scored more marks")













class Student:
    def __init__(self,c,java,python):
        self.c = c
        self.java = java
        self.python = python
    '''
    def __str__(self):
        return self.c,self.java,self.python
    '''
    def __str__(self):
        return '{2} {0} {1}'.format(self.c,self.java,self.python)

a = Student('seventy','eighty','ninety')
b = Student('Adarsh','pavan','Hemanth')
print(a.__str__())
print(b)



