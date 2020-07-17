import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

def plot_digit(digit, label=None, shape=(28,28)):
  """Plot the given digit image with label (if provided)."""
  digit = digit.reshape(*shape)
  plt.imshow(digit, cmap='gray')
  if label is not None:
    plt.title("True label: " + str(label))


# this loads the MNIST digits from the notebook sample data (see "Files")
mnist = read_csv('C:/Users/fish2/PycharmProjects/untitled/data/mnist_data.csv')
mnist = np.array(mnist)
print("Data loaded. Shape: ", mnist.shape)

y = mnist[:,0]
print("Nella prima colonna troviamo i label :\n", np.unique(y))

x = mnist[:, 1:]
print("Array per ogni sample: ", x.shape)

idx = 0
digit = x[idx,:]
label = y[idx]
print(label)
print(digit.shape)

# Print one digit
plt.figure()
plot_digit(digit, label, shape=(28,28))        # shape=(28,28) transform the array in a matrix
# plt.show()

# I want to plot 10 different examples of class k
k=7
# y the labels
# x are the digits stored by rows (one digit = one row)
xk = x[y==k,:]
xk = np.array(xk)

num_of_k_digits = (y==k).sum()
print("Shape xk: \n",xk.shape)
print("Number of digits in class " + str(k) + ": ", num_of_k_digits)


plt.figure()
for i in range(10):  # loop over subplots
  plt.subplot(2,5,i+1)
  plot_digit(xk[i,:], k)

plt.show()


