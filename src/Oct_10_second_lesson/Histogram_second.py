import numpy as np
import matplotlib.pyplot as plt


def histogram(x, values=None):
    """Compute histogram of x."""
    if values is None:
        # generate values
        values = np.unique(x)
        print("Print values: \n", values) # used to "debug"

    values = np.array(values)  # casting the list to ndarray
    hist_values = np.zeros(shape=(values.size,))
    # print(hist_values, np.shape(hist_values))
    for idx, val in enumerate(values):  # for i in [0,...,255]
        # we count how many times i appears in x
        # and store it in hist_values at index i,
        # such that hist_values[0] will contain how many times 0 appears in x, etc.
        hist_values[idx] = (x == val).sum()
    return values, hist_values


np.random.seed(0)

# generate a random image (i.e., a matrix) with pixels in {0, 1, ..., 255}
n_rows, n_cols = 28, 28
x = np.random.randint(0, 256, (n_rows, n_cols))

# hist_values = histogram(x, values)
values, hist_values = histogram(x)

plt.figure()
plt.imshow(x, cmap='gray')
# plt.show()

# plotting the full histogram
plt.figure()
plt.bar(values, hist_values)
# plt.show()


