# working with functions


def changer(x1, y1):
    x1 = x1 + 1
    y1[0] = 'hello!'
    return x1, y1


def my_function(a, b):
    a = a * a
    # see for loops to see a better "shape"
    length = len(b)
    for i in range(length):
        b[i] = b[i] + "a"
    return a, b


x = 0
y = ['bye', 'abx', 'cde']
print(x, y)
x_after, y_after = changer(x, y)
print(x, y, x_after, y_after)

# y, y_after reference the same list in memory
y[0] = 'bye'
print(y, y_after)

x = 4
x_square, y_plussa = my_function(x, y)

print("My_function:\n", x, y)

# ----------------------------------------------------------------------------------------------
# |                                     FUNCTION 2                                             |
# ----------------------------------------------------------------------------------------------

print('Handling optional arguments...')


def funct(a, b, c=10, d=100):
    print(a, b, c, d)


e = 2
f = 1

funct(1, 2)
funct(1, 2, 3, 4)

funct(a=1, b=2)
funct(b=2, a=1)

funct(b=2, a=1, d=2)

# passing my values through variables, the order matters
funct(f, e)
funct(e, f)

# passing parameters as a dictionary
input_params = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(input_params)
funct(**input_params)

# input_params = {'a': 1, 'b': 2, 'c': 3, "e":6} I can't do this
# funct(**input_params)                          I can't do this
