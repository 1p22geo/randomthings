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

    def power(self, exponent):
        p = Complex(self.a, self.b)
        for n in range(exponent-1):
            p = p.mul(self)
        return p


    def __str__(self):
        if self.b >=0:
            return "{} + {}i".format(self.a,self.b)
        else:
            return "{} - {}i".format(self.a,-self.b)

if __name__ =="__main__":
    x = Complex(2,3)
    y = Complex(3,8)
    a = x.mul(y)
    print(x.power(3))
    print(a.add(Complex(1,1)))
    print(Complex(-1.34, -1.34))