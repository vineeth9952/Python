class Father:
    def Wallet(self):
        print("This is Father's Wallet")

class Son(Father):
    def gpay(self):
        print("This is son's Gpay")

class Daughters_Husband:
    def phonepay(self):
        print("This is Daughters Husband's Phonepay")

class Daughter(Father,Daughters_Husband):
    def handbag(self):
        print("This is Daughter's Handbag")

s = Son()
s.Wallet()
d = Daughter()
d.Wallet()