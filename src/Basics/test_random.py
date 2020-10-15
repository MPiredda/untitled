

class Test1(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    def boicotto(self):
        self._x = self._x*self._x


    def stampa(self):
        print("Stampo a cazzo")



test = Test1()
test.x = 2
print(test.x)
test.boicotto()
print(test.x)
test._x+1
print(test.x)


def decorator(f):
    def new_function():
        print("Extra Functionality")
        f()
    return new_function

@decorator
def initial_function():
    print("Initial Functionality")

initial_function()