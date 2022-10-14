class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, x):
        return Complex(self.a + x.a, self.b + x.b)

    def sub(self, x):
        return Complex(self.a - x.a, self.b - x.b)

    def mul(self,x):
        return Complex((self.a*x.a)-(self.b*x.b),(self.a*x.b)+(self.b*x.a))