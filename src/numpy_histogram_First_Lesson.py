import numpy as np
import matplotlib.pyplot as plt

#  np.random.seed(0)            # In order to have always the same matrix

# generate a random image (i.e., a matrix) with pixels in {0, 1, ..., 255}
n_rows, n_cols = 100, 100
x = np.random.randint(0, 256, (n_rows, n_cols))
print("Print random matrix: ")
print(x)

# compute histogram
values = list(range(0, 256))  # this creates a list containing [0, 1, ..., 255]
print("Order array from 0 to 255: ")
print(values)

# compute how many times i appears in the matrix x
i = 147
matched_elems = x == i
number_of_matches = matched_elems.sum()

print("Matrix true in the correspondent position: ")
print(matched_elems)
print("Number of match element: ")
print(number_of_matches)

hist_values = np.zeros(shape=(256,))  # a vector of 255 elements equal to 0
for i in values:  # for i in [0,...,255]
    # we count how many times i appears in x
    # and store it in hist_values at index i,
    # such that hist_values[0] will contain how many times 0 appears in x, etc.
    hist_values[i] = (x == i).sum()

# plotting the first 10 elements {0, ..., 9}
plt.subplot(2, 1, 1)
plt.bar(values[:10], hist_values[:10])

# plotting the full histogram
plt.subplot(2, 1, 2)
plt.bar(values, hist_values)

plt.show()

# what happens if you sample a larger image? How should the histogram look like?
# ... TRY IT!
