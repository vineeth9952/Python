

class CSE:
    Trainer = "vineeth"
    def __init__(self,a,b):
        self.a = a
        self.b = b


obj = CSE("Prashanth",403)

print(getattr(CSE,'Trainer'))
print(getattr(obj,'b'))#gets the attribute

print(hasattr(obj,'b'))#gives True if attribute is present else False

setattr(obj,'b','20H55A0403')#set the attribute with new value

print(getattr(obj,'b'))

delattr(obj,'b')#deletes the attribute

print(hasattr(obj,'b'))
print(getattr(obj,'b'))#AttributeError: 'CSE' object has no attribute 'b'