import numpy as np
from numpy import pi

zeros = np.zeros((5, 5))
print(zeros)

a = np.arange(15).reshape(5, 3)
print(a)

ones = np.ones((3, 5), dtype=np.int64)

print(np.dot(a, ones))

print(id(a))
c = a.view()

print(c.base is a, id(c), id(a), id(c.base), )

x = np.linspace(0, 2 * pi, 9)
print(np.sin(x))

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(A * B)
print(A @ B)

print(np.empty((2, 3)))
print(np.empty((2, 3)))

print(np.arange(12) ** 2)
