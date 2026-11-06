class Rational:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def reduce (self, a ,b):
        if a > b:
            a -=b
        for i in range (b,0,-1):
            if a % i == 0 and b % i == 0:
                a //= i
                b //= i
                break
        return Rational(a,b)
    def __str__(self):
        return  f"{self.a}/{self.b}"
    def __add__(self, other):
        return self.reduce(self.a*other.b + self.b*other.a , self.b*other.b)
    def __sub__(self, other):
        return self.reduce(self.a*other.b- self.b*other.a , self.b*other.b)
    def __mul__(self, other):
        return self.reduce(self.a*other.a , self.b*other.b)
    def __truediv__(self,other):
        return self.reduce(self.a*other.b ,self.b*other.a)
f1 = Rational(5,10)
f2 = Rational(3,4)
print(f1+f2)
