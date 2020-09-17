import numpy as np
from pandas import read_csv

def load_mnist(csv_filename='C:/Users/fish2/PycharmProjects/untitled/data/mnist_data.csv'):
    """Load the MNIST digits from the notebook sample data (see "Files")"""
    mnist = read_csv(csv_filename)
    mnist = np.array(mnist)
    y = mnist[:, 0]  # get the labels from the first column
    x = mnist[:, 1:]  # get the data from the other columns
    return x, y

x,y=load_mnist()
print("Data loaded. Shape: ", x.shape, y.shape)

# split data into training and testing sets
fraction_tr_samples = 0.6


num_samples = y.size  # number of samples in data, equal to x.shape[0]
n_tr = int(fraction_tr_samples * num_samples)
n_ts = num_samples-n_tr
print(num_samples, n_tr, n_ts)

# 1) create a vector of indexes (ordered integer vector): [0, 1, 2, ...]
idx = np.arange(num_samples)
print(idx)

# 2) shuffle it
np.random.shuffle(idx)  # you can comment this line for debugging
print(idx)

# 3) idx_tr <- extract the first n_tr elem. from the shuffled idx vector
idx_tr = idx[:n_tr]
print ("tr. idx: ", idx_tr.shape, idx_tr)

# 4) idx_ts <- extract the following n_ts elem. from the shuffled idx vector
idx_ts = idx[n_tr:]
print ("ts. idx: ", idx_ts.shape, idx_ts)

assert(n_ts == idx_ts.size)  # assert is useful in unit testing

# 5) extract training and testing samples from x (along with their labels y)
x_tr = x[idx_tr, :]
y_tr = y[idx_tr]

x_ts = x[idx_ts, :]
y_ts = y[idx_ts]

print(x_tr.shape, y_tr.shape)
print(x_ts.shape, y_ts.shape)

