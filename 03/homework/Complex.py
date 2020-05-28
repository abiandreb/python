import math


class Complex:

    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag, self.imag*other.real + self.real*other.imag)

    def __div__(self, other):
        s_real, s_imag, o_real, o_imag = self.real, self.imag, other.real, other.imag
        r = float(o_real ** 2 + o_imag ** 2)
        return Complex((s_real*o_real + s_imag * o_imag) / r, (s_imag * o_real - s_real * o_imag) / r)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)


a = Complex(3, 4)
b = Complex(5, 6)
print(a*b)
print(a+b)
print(a-b)
print(-a)
print(a == b)
print(a)
print(b)
