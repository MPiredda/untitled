import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv


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


def plot10(digits, labels=None):
    if digits.shape[0] != 10:
        raise ValueError("the input matrix does not have 10 rows!")
    plt.figure()
    for k in range(10):  # loop over subplots/classes
        plt.subplot(2, 5, k + 1)
        if labels is None:  # assume that k is the true label (0, 1, 2...)
            plot_digit(digits[k, :], k)
        else:
            plot_digit(digits[k, :], labels[k])
    # plt.show()


def split_data(x, y, fract_tr=0.5):
    """Splits x,y into training and testing sets."""
    num_samples = y.size  # number of samples in data, equal to x.shape[0]
    n_tr = int(fract_tr * num_samples)
    n_ts = num_samples - n_tr
    # create a vector of indexes (ordered integer vector): [0, 1, 2, ...]
    idx = np.arange(num_samples)
    # shuffle it
    np.random.shuffle(idx)
    # extract training/testing idx from the shuffled idx vector
    idx_tr = idx[:n_tr]
    idx_ts = idx[n_tr:]
    assert (n_ts == idx_ts.size)  # assert is useful in unit testing
    # 5) extract training/testing samples from x (along with their labels y)
    x_tr = x[idx_tr, :]
    y_tr = y[idx_tr]
    x_ts = x[idx_ts, :]
    y_ts = y[idx_ts]
    return x_tr, x_ts, y_tr, y_ts


x, y = load_mnist()
print('Data loaded. Shape: ', x.shape, y.shape)

# we now implement fit: estimate the centroid for each class
num_classes = np.unique(y).size
num_features = x.shape[1]  # x.shape => (9999, 784)
centroids = np.zeros(shape=(num_classes, num_features))  # (10, 784)
for k in range(num_classes):
    centroids[k, :] = x[y == k, :].mean(axis=0)

plot10(centroids)


# create the fit function
def fit(x, y):
    """Fitting the NMC classifier to data by
    estimating centroids for each class."""
    num_classes = np.unique(y).size
    num_features = x.shape[1]  # x.shape => (9999, 784)
    centroids = np.zeros(shape=(num_classes, num_features))  # (10, 784)
    for k in range(num_classes):
        centroids[k, :] = x[y == k, :].mean(axis=0)
    return centroids


centroids1 = fit(x, y)

plot10(centroids1)

plot10(centroids - centroids1)

l2norm_of_difference = np.linalg.norm((centroids - centroids1).ravel())


print(l2norm_of_difference)

# check that the difference is basically zero (or very small)
assert (l2norm_of_difference <= 1e-10)
