import numpy as np


'''                  What is numpy?
NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
NumPy is the fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object, and useful linear algebra, Fourier transform, and random number capabilities.
NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types'''
'''Numpy Arrays Vs Python Sequences
NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.

The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.

NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.'''



# Creating a NumPy array
# NumPy arrays are created using the array() function.
# The array() function takes a list as an argument and converts it into a NumPy array.
# The array() function can also take a tuple or a list of lists as an argument.
# The array() function can also take a dtype argument to specify the data type of the array.
# The dtype argument can be a string or a NumPy data type object.
# The dtype argument can be used to specify the data type of the array.
# The data type can be specified as a string or as a NumPy data type object.
# it is a 2D array
# The array() function can also take a shape argument to specify the shape of the array.
# The shape argument can be a tuple or a list of integers.
# The shape argument can be used to specify the shape of the array.
# The shape can be specified as a tuple or as a list of integers.
# The shape argument can be used to specify the shape of the array.
array = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])

print("NumPy Array:", array) 
print("Array Type:", type(array))
print("Array Shape:", array.shape)