class A:
    def falar(self):
        print("Classe A")

class B:
    def falar(self):
        print("Classe B")

class C(A, B):
    pass

c = C()
c.falar()

print(C.__mro__)
