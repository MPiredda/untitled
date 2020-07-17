# numpy arrays

import numpy as np

a = np.eye(3)
print("3x3 identity matrix: \n", a)

r = [False, False, True]
print("Extracting rows for which r is True: \n", a[r, :])

y = np.array([-1, 1, -1])
x = y == -1
print("Comparing array with numerical value: ", x)

print("Extracting rows for which y==-1 is True: \n", a[y == -1, :])
print("Extracting rows for which y==1 is True: \n", a[y == 1, :])

# ----------------------------------------------------------------------------
# |                           Numpy youtube                                  |
# ----------------------------------------------------------------------------

a = np.full((3, 4), 22)              # Create an array/matrix of specific elements
print("Print full function: \n", a)

a = np.arange(0, 12, 2) # Create an array from 0 to 12 with a gap of 2
# Arrange(10) Create an array of 1' element  with a gap of 1
print("Print arrange function: \n", a)

a = np.linspace(0, 10, 7)            # Create an array from 1 to 10 of 7 element with equal(more or less) gap
print("Print linspace function: \n ", a)

a = np.random.randint(0, 10, (2, 3))
print("Print matrix: \n", a)
a = a.ravel()                       # Transform the matrix in an array
print("Print array a: \n",a)

# Look into a matrix
a = np.array([[1, 2, 3, 4, 56], [23, 44, 6, 8, 9]])
print("Print element in second position: \n", a[0:1, 1])
print("Print the second column: \n", a[..., 1], "\nOr: \n", a[:, 1])  # Two different ways

# Around function (Arrotondamento)
a = np.array([[1.5, 6.4], [2.2, 4.7]])
print("Matrix a \n", a)
print("Arrotondo: \n", np.around(a))
print("Arrotondo per difetto:\n", np.floor(a)) # np.ceiL(a) Arrotondo per difetto
