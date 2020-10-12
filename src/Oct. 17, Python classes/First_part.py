import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from sklearn.metrics.pairwise import euclidean_distances


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


class NMC(object):

    def __init__(self):
        self._centroids = None

    @property
    def centroids(self):
        return self._centroids

    @centroids.setter
    def centroids(self, value):
        self._centroids = value

    def fit(self, x, y):
        """Fitting the NMC classifier to data by
        estimating centroids for each class."""
        num_classes = np.unique(y).size
        num_features = x.shape[1]  # x.shape => (9999, 784)
        self._centroids = np.zeros(shape=(num_classes, num_features))  # (10, 784)
        for k in range(num_classes):
            self._centroids[k, :] = x[y == k, :].mean(axis=0)

    def predict(self, x):
        if self._centroids is None:
            # the clf has not been trained / centroids not estimated
            raise ValueError("Run fit first to estimate centroids!")
        dist = euclidean_distances(x, self._centroids, squared=True)
        y_pred = np.argmin(dist, axis=1)
        return y_pred


x, y = load_mnist()
# rescale all images in [0,1]
x = x / 255
print('Data loaded. Shape: ', x.shape, y.shape)

n_reps = 10
fract_tr = 0.8
clf = NMC()

test_error = np.zeros(shape=(n_reps,))

for i in range(n_reps):
    x_tr, x_ts, y_tr, y_ts = split_data(x, y, fract_tr=fract_tr)
    clf.fit(x_tr, y_tr)  # estimate the centroids from training data
    y_pred = clf.predict(x_ts)
    test_error[i] = (y_ts != y_pred).mean()
    print("Error at rep. " + str(i) + ": " + str(test_error[i]))

avg = test_error.mean()
std = test_error.std()
print("Mean error and std. dev.: " + str(avg) + "+/-" + str(std))
