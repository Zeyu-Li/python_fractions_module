""" a custom fractions class """

class Fraction:
    """ a class for defining fractions """
    def __init__(self, top, bottom):
        """ top is numerator and bottom is denominator """
        self.top = top
        if bottom == 0:
            raise ZeroDivisionError
        self.bottom = bottom

    # overloads
    def __str__(self):
        """ prints fraction """
        self.simplify()
        if self.bottom == 1:
            return f"{int(self.top)}"
        return f"{int(self.top)}/{int(self.bottom)}"

    def __add__(self, rhs):
        """ overloads + """
        if isinstance(rhs, int):
            rhs = Fraction(rhs, 1)
        elif isinstance(rhs, float):
            return self.to_float() + rhs

        lcm = int(self.lcm(self.bottom, rhs.bottom))
        self.lcm_apply(lcm, self, rhs)

        return Fraction(self.top + rhs.top, self.bottom)

    def __radd__(self, lhs):
        """ overloads + but backwards b/c of commutativity """
        return self.__add__(lhs)

    def __sub__(self, rhs):
        """ overloads - """
        if isinstance(rhs, int):
            rhs = Fraction(rhs, 1)
        elif isinstance(rhs, float):
            return self.to_float() - rhs
        lcm = self.lcm( self.bottom, rhs.bottom)
        self.lcm_apply(lcm, self, rhs)

        return Fraction(self.top - rhs.top, self.bottom)

    def __rsub__(self, lhs):
        """ overloads - but opposite """
        if isinstance(lhs, int):
            lhs = Fraction(lhs, 1)
        elif isinstance(lhs, float):
            return lhs - self.to_float()
        lcm = self.lcm( self.bottom, lhs.bottom)
        self.lcm_apply(lcm, self, lhs)

        return Fraction(lhs.top - self.top, self.bottom)

    def __mul__(self, rhs):
        """ overloads * """
        if isinstance(rhs, int):
            rhs = Fraction(rhs, 1)
        elif isinstance(rhs, float):
            return self.to_float() * rhs

        return Fraction(self.top * rhs.top, self.bottom * rhs.bottom)

    def __rmul__(self, lhs):
        """ overloads * but backwards """
        return self.__mul__(lhs)

    def __truediv__(self, rhs):
        """ overloads / """
        if isinstance(rhs, int):
            rhs = Fraction(rhs, 1)
        elif isinstance(rhs, float):
            return self.to_float() / rhs

        return Fraction(self.top * rhs.bottom, self.bottom * rhs.top)

    def __rtruediv__(self, lhs):
        """ overloads / but backwards """
        if isinstance(lhs, int):
            lhs = Fraction(lhs, 1)
        elif isinstance(lhs, float):
            return lhs / self.to_float()

        return Fraction(self.bottom * lhs.top, self.top * lhs.bottom)

    def __pow__(self, rhs):
        """ overloads ** """
        return self.to_float() ** rhs

    def __rpow__(self, lhs):
        """ overloads ** but backwards """
        return self.__pow__(lhs)

    # comparisons
    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.to_float() < other.to_float()
        return self.to_float() < other

    def __rlt__(self, lhs):
        if isinstance(lhs, Fraction):
            return self.to_float() > lhs.to_float()
        return self.to_float() > lhs

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.to_float() <= other.to_float()
        return self.to_float() <= other

    def __rle__(self, lhs):
        if isinstance(lhs, Fraction):
            return self.to_float() >= lhs.to_float()
        return self.to_float() >= lhs

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.to_float() > other.to_float()
        return self.to_float() > other

    def __rgt__(self, lhs):
        if isinstance(lhs, Fraction):
            return self.to_float() < lhs.to_float()
        return self.to_float() < lhs

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.to_float() >= other.to_float()
        return self.to_float() >= other

    def __rge__(self, lhs):
        if isinstance(lhs, Fraction):
            return self.to_float() <= lhs.to_float()
        return self.to_float() <= lhs

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.to_float() == other.to_float()
        return self.to_float() == other

    def __req__(self, lhs):
        return self.__eq__(lhs)

    def __ne__(self, other):
        if isinstance(other, Fraction):
            return self.to_float() != other.to_float()
        return self.to_float() != other

    def __rne__(self, lhs):
        return self.__ne__(lhs)

    # end of overloads
    def simplify(self):
        """ simplifies the fraction """
        gcd = self.gcd(self.top, self.bottom)
        if not gcd == max(abs(self.top), abs(self.bottom)):
            self.top = int(self.top/gcd)
            self.bottom = int(self.bottom/gcd)

    def lcm(self, a, b):
        """ calculates lcm """
        return (a*b)/self.gcd(a,b)

    def gcd(self, first, second):
        """ gets gcd from first and second number """
        if second == 0:
            return first
        return self.gcd(second, first % second)

    def lcm_apply(self, lcm, *argv):
        """ applies the lcm """
        for fraction in argv:
            if lcm == fraction.bottom:
                continue
            fraction.top *= int(lcm/fraction.bottom)
            fraction.bottom = lcm

    def to_float(self):
        """ converts fraction to decimal """
        return self.top/self.bottom


def strip_mult(*args):
    """ converts a variable amount of args to be striped of whitespace """
    temp = []
    for element in args:
        temp.append(element.strip())

    return temp


def parse(*args):
    """ parses through a set of strings and returns the right type """

    message = 0
    inputs = []

    for index, input_ in enumerate(args):

        if input_.isdigit():
            inputs.append(int(input_))
            message = 1
        else:
            try:
                inputs.append(float(input_))
                message = 1
            except ValueError:
                fraction = []
                input_ = input_.split("/")
                if input_[1] == 0:
                    return "zero d", 0, 0
                for number in input_:
                    fraction.append(int(number.strip()))
                inputs.append(Fraction(fraction[0], fraction[1]))
                message = 1
            else:
                message = str(index)

    return message, inputs[0], inputs[1]
