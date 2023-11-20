
from math import pi


def my_decorator(func):
    def wrapper():
        print('before decorator')
        func()
        print('after decorator')
    return wrapper
@my_decorator
def hello():
    print('лппдари')

hello()

class Vector:
    'IHV;FNVB;QEV'
    MIN_CORD = 0
    MAX_CORD = 100
    def __init__(self,x,y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y


    def get_cords(self):
        return self.x,self.y

    @staticmethod
    def norm2(x,y):
        return x ** 2 + y ** 2
    @classmethod
    def validate(cls,arg):
        return cls.MIN_CORD < arg <cls.MAX_CORD




v = Vector(1,5)
print(v.get_cords())
print(v.__dict__)
print(Vector.__doc__)


from math import pi

class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return 2 * (circle + side)

    def __init__(self, diam, high):
        self.high = high
        self.diam = diam
        self.area = self.make_area(self.diam, self.high)

    def __str__(self):
        return f'diam = {self.diam}, high = {self.high}, area = {self.area}'

c = Cylinder(2, 4)
print(c)

class MyClass:
    TOTAL_COUNTS = 0

    def __init__(self):
        MyClass.TOTAL_COUNTS = MyClass.TOTAL_COUNTS + 1


    @classmethod
    def total_counts(cls):
        print('total counts = ',cls.TOTAL_COUNTS)


class ChildClass(MyClass):
        TOTAL_COUNTS = 0

        def __init__(self):
            ChildClass.TOTAL_COUNTS += 1

s = MyClass()
m1 = MyClass()
MyClass.total_counts()


class Point:
    MIN_COORDS = 0
    MAX_COORDS = 100

    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __str__(self):
        return f'x = {self.x}, y = {self.y}'

    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError("Cannot set 'z' attribute")
        self.__dict__[key] = value

    def __getattr__(self, item):
        print(f'Attribute "{item}" not found')

    def __del__(self):
        print('no object')

p = Point(1, 6)
p.j = 15
print(p.__dict__)
try:
    p.z = 42
except ValueError as e:
    print(e)
print(p.__dict__)





