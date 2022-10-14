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

    def __str__(self):
        if self.b >=0:
            return "{} + {}i".format(self.a,self.b)
        else:
            return "{} - {}i".format(self.a,-self.b)

if __name__ =="__main__":
    x = Complex(2,3)
    y = Complex(3,8)
    print(x.mul(y))
    print(Complex(-1.34, -1.34))