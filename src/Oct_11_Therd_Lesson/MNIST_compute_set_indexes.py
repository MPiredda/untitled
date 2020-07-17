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

# print the first digit in each class
hist_list = []  # this will contain the histogram of each digit (one per class)
plt.figure()
for k in range(10):  # loop over subplots/classes
    plt.subplot(2, 5, k + 1)
    # idx = idx_per_class[k][0]  # takes the first idx in class k
    sel_rand = np.random.randint(0, idx_per_class[k].size)
    print("Sel_rand: \n", sel_rand)
    idx = idx_per_class[k][sel_rand]  # takes a random element from idx of class k
    plot_digit(x[idx, :], k)          # The second parameter is what we print
    hist_list.append(histogram(x[idx, :]))  # get (values,hist_val) for this digit

plt.figure()
for k in range(10):  # loop over subplots/classes
    plt.subplot(2, 5, k + 1)
    # plot horizontal histograms (in logscale to de-emphasize differences/peaks)
    plt.barh(hist_list[k][0], np.log(hist_list[k][1]))    # plt.bar print vertical




