"""

Write a python class Calculation. The class would have 3 methods.
sum(a,b) calculate sum of a and b.
mul(a,b) calculate multiplication for a, b
sub(a,b) calculate subtraction value of a and b, validation to check if a > b, if a < b return error,
 A should be greater than b.
In the same class there should be a constructor function that will take values of a,b .
 If a,b is not passed in constructor method params will be used. See Classes Tutorial

"""


class calculation:
    def __init__(self,a=0,b=0):


        self.x=a
        self.y=b
    def sum(self,a=0,b=0):
        if self.x==0:
            self.x=a
        if self.y==0:
            self.y=b

        return self.x+self.y



c=calculation(4,4)
print(c.sum(2,4))

c1=calculation()
print(c1.sum(2,4))

c2=calculation(4,4)
print(c2.sum())














