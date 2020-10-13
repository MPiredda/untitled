import sys


class Test1():
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value=0):
        self._x = value


test = Test1()
test.x = 2


print(test.x)
