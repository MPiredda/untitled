# do some refactoring to separate (random) digit selection and plot functionalities

import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv


def histogram(x, values=None):
    """Compute histogram of x."""
    if values is None:
        # generate values
        values = np.unique(x)
        # print(values)  # used to "debug"
    values = np.array(values)  # casting the list to ndarray
    hist_values = np.zeros(shape=(values.size,))
    for idx, val in enumerate(values):  # for i in [0,...,255]
        # we count how many times i appears in x
        # and store it in hist_values at index i,
        # such that hist_values[0] will contain how many times 0 appears in x, etc.
        hist_values[idx] = (x == val).sum()
    return values, hist_values


def plot_digit(digit, label=None, shape=(28, 28)):
    """Plot the given digit image with label (if provided)."""
    digit = digit.reshape(*shape)
    plt.imshow(digit, cmap='gray')
    if label is not None:
        plt.title("True label: " + str(label))


def load_mnist(csv_filename='C:/Users/fish2/PycharmProjects/untitled/data/mnist_data.csv'):
    """Load the MNIST digits from the notebook sample data (see "Files")"""
    mnist = read_csv(csv_filename)
    mnist = np.array(mnist)
    y = mnist[:, 0]  # get the labels from the first column
    x = mnist[:, 1:]  # get the data from the other columns
    return x, y


def plot10(digits):
    if digits.shape[0] != 10:
        raise ValueError("the input matrix does not have 10 rows!")
    plt.figure()
    for k in range(10):  # loop over subplots/classes
        plt.subplot(2, 5, k + 1)
        plot_digit(digits[k, :], k)


def hist10(digits):
    plt.figure()
    for k in range(10):  # loop over subplots/classes
        plt.subplot(2, 5, k + 1)
        # plot horizontal histograms (in logscale to de-emphasize differences/peaks)
        values, hist_values = histogram(digits[k, :])
        plt.barh(values, np.log(hist_values))


x, y = load_mnist()
print('Data loaded. Shape: ', x.shape, y.shape)

# we can use where to extract indexes of elements
# belonging to a given class
# [0] after "where" extracts the first element in the tuple
# returned by where, which is the set of indexes we're interested in
idx_0 = np.where(y == 0)[0]
print(idx_0[0:10], type(idx_0), len(idx_0))

# we do it for all classes
idx_per_class = []
for k in range(10):
    idx_k = np.where(y == k)[0]
    idx_per_class.append(idx_k)
    print("No. of " + str(k) + ": ", len(idx_k))

# take 10 digits (one per class)
digits = np.zeros(shape=(10, 784))
for k in range(10):
    sel_rand = np.random.randint(0, idx_per_class[k].size)
    idx = idx_per_class[k][sel_rand]  # takes a random element from idx of class k
    digits[k, :] = x[idx, :]

# example of try-catch with a specific exception
try:
    plot10(x)
except ValueError:
    plot10(digits)

hist10(digits)

# Now: compute average digit per class, and show them along with their hists
xk = x[y == 0, :]
print(xk.shape)
print(xk.mean(axis=0).shape)
print(xk.mean(axis=1).shape)

avg_digits = np.zeros(shape=(10, 784))
for k in range(10):
    avg_digits[k, :] = x[y == k, :].mean(axis=0)

plot10(avg_digits)
hist10(avg_digits)

