'''
class Coordinate(object):
        def __init__(self, x, y):
                self.x = x
                self.y = y
        def distance(self, other):
                x_diff_sq = (self.x-other.x)**2
                y_diff_sq = (self.y-other.y)**2
                return (x_diff_sq + y_diff_sq)**0.5
        #return a string when printed
        def __str__(self):
                return "({},{})".format(self.x,self.y)

g = Coordinate(5,6)
r = Coordinate(-4,7)

print(g.distance(r))
print(g)'''
'''
__add__(self, other) -> self + other
__sub__(self, other) -> self - other
__eq__(self, other) -> self == other
__lt__(self, other) -> self < other
__len__(self) -> len(self)
__str__(self) -> print self
'''
#fractions
class Fractions:
    def __init__(self,num,denom):
        assert type(num)== int and type(denom)== int, "Numerator and Denominator must be an integer"
        assert int(denom)!=0, "Denominator must not be zero"
        self.num=num
        self.denom = denom
    def __add__(self, other):
        newNum = self.num*other.denom + other.num*self.denom
        newDenom = self.denom*other.denom
        return Fractions(newNum,newDenom)
    def __str__(self):
        return str(self.num)+ "/" + str(self.denom)

a = Fractions(-4, 8)
b = Fractions(5,-12)
print(a+b)
