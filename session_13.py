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

print("NumPy Array:", array)  # NumPy Array: [[ 1  2  3  4  5][ 6  7  8  9 10]]
print("Array Type:", type(array))   # Array Type: <class 'numpy.ndarray'>
print("Array Data Type:", array.dtype)  # Array Data Type: int64
print("Array Shape:", array.shape) # Array Shape: (2, 5)


#3D array
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("3D Array:", array_3d)  # Array content
print("3D Array Type:", type(array_3d))  # Type: <class 'numpy.ndarray'>
print("3D Array Data Type:", array_3d.dtype)  # Data type: int32
print("3D Array Shape:", array_3d.shape)  # Shape: (2, 2, 3)
print("3D Array Size:", array_3d.size)  # Size: 12
print("3D Array Dimensions:", array_3d.ndim)  # Dimensions: 3
print("3D Array Item Size:", array_3d.itemsize)  # Item size: 4
print("3D Array Strides:", array_3d.strides)  # Strides: (24, 12, 4)
print("3D Array Nbytes:", array_3d.nbytes)  # Total bytes: 96
print("3D Array Buffer:", array_3d.data)  # Buffer: <memory at ...>
print("3D Array Buffer Type:", type(array_3d.data))  # Buffer type: <class 'memoryview'>
print("3D Array Buffer Format:", array_3d.data.format)  # Buffer format: 'B'
print("3D Array Buffer Read Only:", array_3d.data.readonly)  # Buffer read-only: False

# ---------------------------------------------------example---------------------------------------------------
#  3D array: 4 months, 2 stores, 3 products
sales_data = np.array([
    [[10, 15, 20], [12, 18, 22]],  # Month 1
    [[11, 16, 21], [13, 19, 23]],  # Month 2
    [[12, 17, 22], [14, 20, 24]],  # Month 3
    [[13, 18, 23], [15, 21, 25]]   # Month 4
],dtype=int)  # Sales data for 4 months, 2 stores, 3 products

print("Sales Data:\n", sales_data)
print("Shape:", sales_data.shape)  # Output: (4, 2, 3)

# Analysis
print("Average sales per product across all months/stores:", np.mean(sales_data, axis=(0, 1)))
print("Total sales for Store 1, Month 1:", np.sum(sales_data[0, 0]))



# ------------------------------------------3D array: 5 time points, 2 rows, 3 columns---------------------------------

temp_data = np.random.uniform(20, 30, (5, 2, 3))  # Random temps between 20-30°C

print("Temperature Data:\n", temp_data.round(1))
print("Shape:", temp_data.shape)  # Output: (5, 2, 3)

# Analysis
print("Average temp at first time point:", np.mean(temp_data[0]).round(1))
print("Max temp across all data:", np.max(temp_data).round(1))








# Creating a 1D array using the arange() function
# The arange() function creates an array with evenly spaced values within a given range.  
# It is similar to the built-in range() function in Python, but it returns a NumPy array instead of a list.
# The arange() function takes three arguments: start, stop, and step.
# The start argument is the starting value of the sequence. The default value is 0.
# The stop argument is the end value of the sequence. The default value is None.  
# The step argument is the difference between each pair of consecutive values in the sequence. The default value is 1.
# The arange() function can also take a dtype argument to specify the data type of the array.
# The dtype argument can be a string or a NumPy data type object.
# The dtype argument can be used to specify the data type of the array.
# The data type can be specified as a string or as a NumPy data type object.
# The arange() function can also take a shape argument to specify the shape of the array.
# The shape argument can be a tuple or a list of integers.
# The shape argument can be used to specify the shape of the array.
# The shape can be specified as a tuple or as a list of integers.
# The shape argument can be used to specify the shape of the array.
# The shape can be specified as a tuple or as a list of integers.

array_1d = np.arange(0, 10, 2)  # Create a 1D array with values from 0 to 10 with a step of 2
print("1D Array:", array_1d)  # 1D Array: [0 2 4 6 8]


#----------------------------resape() function--------------------------------------------------
# The reshape() function is used to change the shape of an array without changing its data.   
# It takes a tuple as an argument, which specifies the new shape of the array.
# The reshape() function can also take a dtype argument to specify the data type of the array.
# The dtype argument can be a string or a NumPy data type object.
# The dtype argument can be used to specify the data type of the array.
# The data type can be specified as a string or as a NumPy data type object.
# The reshape() function can also take a shape argument to specify the shape of the array.
# The shape argument can be a tuple or a list of integers.
# The shape argument can be used to specify the shape of the array.
# The shape can be specified as a tuple or as a list of integers.
# The shape argument can be used to specify the shape of the array.


reshape_array = np.arange(1, 13).reshape(4, 3)  # Reshape the 1D array into a 2D array with shape (4, 3)
print("Reshaped Array:\n", reshape_array)  


# ------ones() function--------------------------------------------------
# The ones() function creates an array filled with ones.  
# It takes a shape argument, which specifies the shape of the array.
# The shape argument can be a tuple or a list of integers.
# The shape argument can be used to specify the shape of the array.
# The shape can be specified as a tuple or as a list of integers.
# The ones() function can also take a dtype argument to specify the data type of the array.
# The dtype argument can be a string or a NumPy data type object.
# The dtype argument can be used to specify the data type of the array.
# The data type can be specified as a string or as a NumPy data type object.
# The ones() function can also take a shape argument to specify the shape of the array.


ones_array = np.ones((3, 4),dtype=int)  # Create a 2D array filled with ones with shape (3, 4)
print("Ones Array:\n", ones_array)  # Ones Array: [[1. 1. 1. 1.][1. 1. 1. 1.][1. 1. 1. 1.]]


# ------zeros() function--------------------------------------------------
# The zeros() function creates an array filled with zeros.
# It takes a shape argument, which specifies the shape of the array.  
# The shape argument can be a tuple or a list of integers.
# The shape argument can be used to specify the shape of the array.
# The shape can be specified as a tuple or as a list of integers.
# The zeros() function can also take a dtype argument to specify the data type of the array.
# The dtype argument can be a string or a NumPy data type object.
# The dtype argument can be used to specify the data type of the array.
# The data type can be specified as a string or as a NumPy data type object.
# The zeros() function can also take a shape argument to specify the shape of the array.
# The shape argument can be a tuple or a list of integers.

zeros_array = np.zeros((4, 5),dtype=int)  # Create a 2D array filled with zeros with shape (4, 5)
print("Zeros Array:\n", zeros_array)  # Zeros Array: [[0 0 0 0 0][0 0 0 0 0][0 0 0 0 0][0 0 0 0 0]]


random_array = np.random.rand(3, 4)  # Create a 2D array with random values between 0 and 1 with shape (3, 4)
print("Random Array:\n", random_array.round(2))  # Random Array: [[0.5488135  0.71518937 0.60276338 0.54488318][0.4236548  0.64589411 0.43758721 0.891773][0.96366276 0.38344152 0.79172504 0.52889492]]


# Creating a 1D array using the linspace() function
# The linspace() function creates an array with evenly spaced values over a specified range.
# It takes three arguments: start, stop, and num.
# The start argument is the starting value of the sequence.
# The stop argument is the end value of the sequence.
# The num argument is the number of samples to generate.
# The linspace() function can also take a dtype argument to specify the data type of the array.
# The dtype argument can be a string or a NumPy data type object.
# The dtype argument can be used to specify the data type of the array.
# The data type can be specified as a string or as a NumPy data type object.
# The linspace() function can also take a shape argument to specify the shape of the array.
# The shape argument can be a tuple or a list of integers.
# The shape argument can be used to specify the shape of the array.
# The shape can be specified as a tuple or as a list of integers.
# The shape argument can be used to specify the shape of the array.
linspace_array = np.linspace(-10, 10, 20)  # Create a 1D array with 20 evenly spaced values between -10 and 10
print("Linspace Array:", linspace_array.round(2))  # Linspace Array: [0.  0.25 0.5  0.75 1. 




# identity() function--------------------------------------------------
# The identity() function creates a square identity matrix of a given size.         
# It takes a single argument, which specifies the size of the matrix.
# The identity() function can also take a dtype argument to specify the data type of the array.
# The dtype argument can be a string or a NumPy data type object.
# The dtype argument can be used to specify the data type of the array.
# The data type can be specified as a string or as a NumPy data type object.
# The identity() function can also take a shape argument to specify the shape of the array.
# The shape argument can be a tuple or a list of integers.
# The shape argument can be used to specify the shape of the array.
# The shape can be specified as a tuple or as a list of integers.
# The shape argument can be used to specify the shape of the array.
identity_array = np.identity(3)  # Create a 3x3 identity matrix
print("Identity Array:\n", identity_array)  # Identity Array: [[1. 0. 0.][0. 1. 0.][0. 0. 1.]]





# numpy Attributss and Methods
# NumPy arrays have a number of attributes and methods that can be used to manipulate and analyze the data in the array.  
# Some of the most commonly used attributes and methods are:
# 1. shape: Returns the shape of the array as a tuple.
# 2. dtype: Returns the data type of the array.
# 3. ndim: Returns the number of dimensions of the array.
# 4. size: Returns the total number of elements in the array.
# 5. itemsize: Returns the size of each element in the array in bytes.
# 6. nbytes: Returns the total number of bytes used by the array.
# 7. strides: Returns the number of bytes to step in each dimension when traversing the array.
# 8. data: Returns the buffer object pointing to the start of the array.  
# 9. T: Returns the transpose of the array.
# 10. flatten(): Returns a copy of the array collapsed into one dimension.
# 11. ravel(): Returns a flattened array.
# 12. reshape(): Returns an array containing the same data with a new shape.
# 13. transpose(): Returns the transposed array.
# 14. sum(): Returns the sum of the array elements along a given axis.
# 15. mean(): Returns the mean of the array elements along a given axis.
# 16. std(): Returns the standard deviation of the array elements along a given axis.
# 17. var(): Returns the variance of the array elements along a given axis.
# 18. min(): Returns the minimum value of the array elements along a given axis.
# 19. max(): Returns the maximum value of the array elements along a given axis.
# 20. argmin(): Returns the indices of the minimum values along an axis.
# 21. argmax(): Returns the indices of the maximum values along an axis.
# 22. sort(): Returns a sorted copy of the array.
# 23. argsort(): Returns the indices that would sort the array.
# 24. unique(): Returns the unique elements of the array.
# 25. where(): Returns the indices of elements that satisfy a given condition.
# 26. any(): Returns True if any element of the array is True.
# 27. all(): Returns True if all elements of the array are True.
# 28. clip(): Limits the values in an array to a specified range.
# 29. concatenate(): Joins two or more arrays along an existing axis.
# 30. stack(): Joins a sequence of arrays along a new axis.
# 31. split(): Splits an array into multiple sub-arrays.
# 32. hsplit(): Splits an array into multiple sub-arrays horizontally (column-wise).
# 33. vsplit(): Splits an array into multiple sub-arrays vertically (row-wise).
# 34. dsplit(): Splits an array into multiple sub-arrays along the third axis (depth-wise).
# 35. copy(): Returns a copy of the array.
# 36. view(): Returns a new view of the array with the same data.
# 37. fill(): Fills the array with a specified value.
# 38. resize(): Resizes the array to a specified shape.
# 39. repeat(): Repeats elements of an array.
# 40. tile(): Constructs an array by repeating the input array.
# 41. broadcast(): Broadcasts an array to a specified shape.
# 42. broadcast_to(): Broadcasts an array to a new shape.
# 43. meshgrid(): Returns coordinate matrices from coordinate vectors.
# 44. einsum(): Evaluates the Einstein summation convention on the operands.
# 45. dot(): Computes the dot product of two arrays.
# 46. matmul(): Computes the matrix product of two arrays.
# 47. cross(): Computes the cross product of two arrays.
# 48. inner(): Computes the inner product of two arrays.
# 49. outer(): Computes the outer product of two arrays.
# 50. tensordot(): Computes the tensor dot product of two arrays.
# 51. corrcoef(): Computes the correlation coefficient of two arrays.
# 52. cov(): Computes the covariance matrix of two arrays.
# 53. histogram(): Computes the histogram of a set of data.
# 54. bincount(): Counts the number of occurrences of each value in an array.
# 55. digitize(): Returns the indices of the bins to which each value in input array belongs.
# 56. histogram2d(): Computes the two-dimensional histogram of two data samples.



a1 = np.arange(10,dtype=np.int64)  # 1D array with values from 0 to 9
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

#---------------------------------------------------ndim---------------------------------------------------
# The ndim attribute returns the number of dimensions of the array.
# It is an integer value that indicates how many dimensions the array has.
# The ndim attribute is useful for determining the dimensionality of the array.
# It can be used to check if the array is a 1D, 2D, or 3D array.

print("a1 ndim:", a1.ndim)  # a1 ndim: 1
print("a2 ndim:", a2.ndim)  # a2 ndim: 2
print("a3 ndim:", a3.ndim)  # a3 ndim: 3



#---------------------------------------------------shape---------------------------------------------------
# The shape attribute returns the shape of the array as a tuple.
# It is a tuple of integers that indicates the size of each dimension of the array.
# The shape attribute is useful for determining the size of the array in each dimension.
# It can be used to check the number of rows and columns in a 2D array, or the number of elements in each dimension of a 3D array.
# The shape attribute can also be used to reshape the array.
# It can be used to change the shape of the array without changing its data.
print("a1 shape:", a1.shape)  # a1 shape: (10,)
print("a2 shape:", a2.shape)  # a2 shape: (3, 4)
print("a3 shape:", a3.shape)  # a3 shape: (2, 2, 2)



#---------------------------------------------------size---------------------------------------------------
# The size attribute returns the total number of elements in the array. 
# It is an integer value that indicates how many elements are in the array.
# The size attribute is useful for determining the total number of elements in the array.
# It can be used to check the total number of elements in a 1D, 2D, or 3D array.
# The size attribute can also be used to reshape the array.
# It can be used to change the shape of the array without changing its data.
# The size attribute can also be used to check the total number of elements in the array.
print("a1 size:", a1.size)  # a1 size: 10
print("a2 size:", a2.size)  # a2 size: 12
print("a3 size:", a3.size)  # a3 size: 8

#---------------------------------------------------itemsize---------------------------------------------------
# The itemsize attribute returns the size of each element in the array in bytes.  
# It is an integer value that indicates how many bytes each element in the array takes up.

# The itemsize attribute is useful for determining the size of each element in the array.
# It can be used to check the size of each element in a 1D, 2D, or 3D array.
# The itemsize attribute can also be used to check the size of each element in the array.
# The itemsize attribute can also be used to check the size of each element in the array.
print("a1 itemsize:", a1.itemsize)  # a1 itemsize: 8
print("a2 itemsize:", a2.itemsize)  # a2 itemsize: 8
print("a3 itemsize:", a3.itemsize)  # a3 itemsize: 8
#---------------------------------------------------nbytes---------------------------------------------------
# The nbytes attribute returns the total number of bytes used by the array.
# It is an integer value that indicates how many bytes the array takes up in memory.
# The nbytes attribute is useful for determining the total number of bytes used by the array.
# It can be used to check the total number of bytes used by a 1D, 2D, or 3D array.

# The nbytes attribute can also be used to check the total number of bytes used by the array.
print("a1 nbytes:", a1.nbytes)  # a1 nbytes: 80
print("a2 nbytes:", a2.nbytes)  # a2 nbytes: 96
print("a3 nbytes:", a3.nbytes)  # a3 nbytes: 64
#---------------------------------------------------strides---------------------------------------------------
# The strides attribute returns the number of bytes to step in each dimension when traversing the array.
# It is a tuple of integers that indicates how many bytes to step in each dimension when traversing the array.
# The strides attribute is useful for determining how many bytes to step in each dimension when traversing the array.
# It can be used to check how many bytes to step in each dimension when traversing a 1D, 2D, or 3D array.


#----------------------------------------------------astype---------------------------------------------------
# The astype() method is used to cast the array to a specified data type.
# It takes a single argument, which specifies the data type to cast the array to. 
# The data type can be specified as a string or as a NumPy data type object.

# The astype() method can be used to change the data type of the array without changing its data.
# It can be used to change the data type of the array to a different data type.
# The astype() method can also be used to change the data type of the array to a different data type.

print(a3.dtype)  # dtype: int64
print(a3.astype(np.float32).dtype)  # dtype: float32



# array operations
# NumPy arrays support a wide range of mathematical operations, including addition, subtraction, multiplication, and division.  
# These operations can be performed element-wise on the array, meaning that the operation is applied to each element of the array individually.
# NumPy arrays also support broadcasting, which allows for operations between arrays of different shapes. 
# Broadcasting automatically expands the smaller array to match the shape of the larger array, allowing for element-wise operations.
# Broadcasting is a powerful feature of NumPy that allows for operations between arrays of different shapes.
# It allows for operations between arrays of different shapes without the need for explicit loops or reshaping.


a1 = np.random.random((3,3))
a1 = np.round(a1*10)
a2 = np.random.random((3,3))
a2 = np.round(a2*10)
print("a1:\n", a1)  # a1: [[ 1.  2.  3.][ 4.  5.  6.][ 7.  8.  9.]]
print("a2:\n", a2)  # a2: [[10. 11. 12.][13. 14. 15.][16. 17. 18.]]


# Element-wise addition
a3 = a1 + a2  # Add a1 and a2 element-wise
print("Element-wise addition:\n", a3)  # Element-wise addition: [[11. 13. 15.][17. 19. 21.][23. 25. 27.]]

# Element-wise subtraction
a4 = a1 - a2  # Subtract a2 from a1 element-wise
print("Element-wise subtraction:\n", a4)  # Element-wise subtraction: [[-9. -9. -9.][-9. -9. -9.][-9. -9. -9.]]

# Element-wise multiplication
a5 = a1 * a2  # Multiply a1 and a2 element-wise
print("Element-wise multiplication:\n", a5)  # Element-wise multiplication: [[10. 22. 36.][52. 70. 90.][112. 136. 162.]] 

# Element-wise division
a6 = a1 / a2  # Divide a1 by a2 element-wise
print("Element-wise division:\n", a6)  # Element-wise division: [[0.1 0.2 0.3][0.4 0.5 0.6][0.7 0.8 0.9]]

# Element-wise exponentiation
a7 = a1 ** 2  # Raise a1 to the power of 2 element-wise
print("Element-wise exponentiation:\n", a7)  # Element-wise exponentiation: [[ 1.  4.  9.][16. 25. 36.][49. 64. 81.]]

# Element-wise square root
a8 = np.sqrt(a1)  # Take the square root of a1 element-wise 
# Note: The square root of a negative number is not defined in the real number system, so it will return NaN for negative numbers.
print("Element-wise square root:\n", a8)  # Element-wise square root: [[1. 1.41421356 1.73205081][2. 2.23606798 2.44948974][2.64575131 2.82842712 3.]]

# Element-wise logarithm
a9 = np.log(a1)  # Take the natural logarithm of a1 element-wise
# Note: The logarithm of a negative number is not defined in the real number system, so it will return NaN for negative numbers.  



print("Element-wise logarithm:\n", a9)  # Element-wise logarithm: [[0. 0.69314718 1.09861229][1.38629436 1.60943791 1.79175947][1.94591015 2.07944154 2.19722458]]
# Element-wise sine 
a10 = np.sin(a1)  # Take the sine of a1 element-wise
print("Element-wise sine:\n", a10)  # Element-wise sine: [[0.84147098 0.90929743 0.14112001][0.6569866  0.95892427 0.41211849][0.6569866  0.90929743 0.14112001]]
# Element-wise cosine
a11 = np.cos(a1)  # Take the cosine of a1 element-wise
print("Element-wise cosine:\n", a11)  # Element-wise cosine: [[-0.54030231 -0.41614684 -0.9899925 ][-0.75390225 -0.28366219 -0.91113026][-0.75390225 -0.41614684 -0.9899925 ]]
# Element-wise tangent
a12 = np.tan(a1)  # Take the tangent of a1 element-wise
print("Element-wise tangent:\n", a12)  # Element-wise tangent: [[-1.55740772 -2.18503986 -0.14254654][-0.87144798 -3.38051501 -0.45231565][-0.87144798 -2.18503986 -0.14254654]]



#relational operators
# NumPy arrays support relational operators, which can be used to compare the elements of the array.  
# The relational operators include:
# 1. ==: Equal to
# 2. !=: Not equal to
# 3. >: Greater than
# 4. <: Less than
# 5. >=: Greater than or equal to
# 6. <=: Less than or equal to
# These operators can be used to compare the elements of the array and return a new array with the results of the comparison.
# The relational operators can be used to compare the elements of the array and return a new array with the results of the comparison.    
# The relational operators can be used to compare the elements of the array and return a new array with the results of the comparison.

print(a2==3)  # Compare a2 with 15 and return a new array with the results of the comparison
# Output: [[False False False][False False  True][False False False]] 

print(a2!=3)  # Compare a2 with 15 and return a new array with the results of the comparison
# Output: [[ True  True  True][ True  True False][ True  True  True]]
print(a2>3)  # Compare a2 with 15 and return a new array with the results of the comparison
# Output: [[False False False][ True  True  True][ True  True  True]]
print(a2<3)  # Compare a2 with 15 and return a new array with the results of the comparison
# Output: [[ True  True  True][False False False][False False False]]
print(a2>=3)  # Compare a2 with 15 and return a new array with the results of the comparison
# Output: [[False False False][ True  True  True][ True  True  True]]
print(a2<=3)  # Compare a2 with 15 and return a new array with the results of the comparison
# Output: [[ True  True  True][False False False][False False False]]



#vectorized operations
# NumPy arrays support vectorized operations, which allow for operations between arrays of different shapes.  
# Broadcasting automatically expands the smaller array to match the shape of the larger array, allowing for element-wise operations.
# Broadcasting is a powerful feature of NumPy that allows for operations between arrays of different shapes.
# It allows for operations between arrays of different shapes without the need for explicit loops or reshaping

#arithmatic operations
# NumPy arrays support a wide range of mathematical operations, including addition, subtraction, multiplication, and division.
print(a1+a2)  # Print the array a1
# Output: [[ 1.  2.  3.][ 4.  5.  6.][ 7.  8.  9.]]
print(a1-a2)  # Print the array a1
# Output: [[-9. -9. -9.][-9. -9. -9.][-9. -9. -9.]]
print(a1*a2)  # Print the array a1
# Output: [[10. 22. 36.][52. 70. 90.][112. 136. 162.]]
print(a1/a2)  # Print the array a1
# Output: [[0.1 0.2 0.3][0.4 0.5 0.6][0.7 0.8 0.9]]
print(a1**2)  # Print the array a1
# Output: [[ 1.  4.  9.][16. 25. 36.][49. 64. 81.]]
print(np.sqrt(a1))  # Print the array a1
# Output: [[1. 1.41421356 1.73205081][2. 2.23606798 2.44948974][2.64575131 2.82842712 3.]]
print(np.log(a1))  # Print the array a1
# Output: [[0. 0.69314718 1.09861229][1.38629436 1.60943791 1.79175947][1.94591015 2.07944154 2.19722458]]
print(np.sin(a1))  # Print the array a1





#methods
# NumPy arrays have a number of methods that can be used to manipulate and analyze the data in the array.
# Some of the most commonly used methods are:MAX/MIN/SUM/prod/mean/std/var
# 1. max(): Returns the maximum value of the array elements along a given axis.
# 2. min(): Returns the minimum value of the array elements along a given axis.
# 3. sum(): Returns the sum of the array elements along a given axis.
# 4. prod(): Returns the product of the array elements along a given axis.
# 5. mean(): Returns the mean of the array elements along a given axis.
# 6. std(): Returns the standard deviation of the array elements along a given axis.
# 7. var(): Returns the variance of the array elements along a given axis.
# 8. median(): Returns the median of the array elements along a given axis.
# 9. percentile(): Returns the nth percentile of the array elements along a given axis.
print("a1 max:", a1.max())  # a1 max: 9.0
print("a1 min:", a1.min())  # a1 min: 0.0
print(np.max(a1,axis=(0,1)))  # a1 max: 9.0
print(np.min(a1,axis=(0)))  # a1 min: 0.0
print(np.sum(a1,axis=(0)))  # a1 sum: 45.0
print(np.prod(a1,axis=(0)))  # a1 prod: 362880.0 
print(np.mean(a1,axis=(0)))  # a1 mean: 5.0
print(np.std(a1,axis=(0)))  # a1 std: 2.581988897471611
print(np.var(a1,axis=(0)))  # a1 var: 6.666666666666667
print(np.median(a1,axis=(0)))  # a1 median: 5.0
print(np.percentile(a1, 50,axis=(0)))  # a1 percentile: 5.0

#dot product
# The dot() method computes the dot product of two arrays.
# It takes two arguments: the first array and the second array.
# The dot() method can be used to compute the dot product of two arrays.
# The dot() method can also be used to compute the dot product of two arrays.


print(np.dot(a1,a2))  # a1 dot: [[ 90.  96. 102.][216. 232. 248.][342. 368. 394.]]
print(np.dot(a1,a2.T))  # a1 dot: [[ 90.  96. 102.][216. 232. 248.][342. 368. 394.]]



#rounding
# The round() method rounds the elements of the array to the nearest integer.
# It takes a single argument, which specifies the number of decimal places to round to.
# The round() method can be used to round the elements of the array to the nearest integer.
print(np.round(np.random.random((2,3))*100))  # a1 round: [[ 1.  2.  3.][ 4.  5.  6.][ 7.  8.  9.]]


#floor
# The floor() method rounds the elements of the array down to the nearest integer.
# It takes a single argument, which specifies the number of decimal places to round to.
# The floor() method can be used to round the elements of the array down to the nearest integer.

print('*'*50)
print(np.floor(np.random.random((2,3))*100))  # a1 floor: [[ 1.  2.  3.][ 4.  5.  6.][ 7.  8.  9.]]





#----------------------------------------------------indexing and slicing---------------------------------------------------
# NumPy arrays support indexing and slicing, which allow for accessing and modifying the elements of the array.
# Indexing allows for accessing individual elements of the array, while slicing allows for accessing a range of elements in the array.
# Indexing and slicing can be used to access and modify the elements of the array.

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)


# locating individual element in 2d array
print("#"*50)
print("locating array element")
print(a2)
print(a2[1,2])  # Print the element at row 0, column 0 of a2
# locating individual element in 3d array
print("#"*50)
print("locating 3D array element")
print(a3)
print(a3[1,0,1])  # Print the element at row 1, column 0, depth 1 of a3
print(a3[0,0,0])



# slicing
# Slicing allows for accessing a range of elements in the array.
# It takes two arguments: the start index and the end index.
# The start index is the index of the first element to include in the slice, while the end index is the index of the first element to exclude from the slice.
# The slice operator can be used to access a range of elements in the array.
print("#"*50,"printin first row of a2","#"*50)
print(a2[0,:])
print("#"*50,"printin 3rd column of a2","#"*50)
print(a2[:,2])
print(a2[1:3,1:3])  # Print the elements from row 1 to 2 and column 1 to 2 of a2 [[ 5  6][ 9 10]]



a5=np.arange(27).reshape(3,3,3)
print("#"*50,"printin 3D array a5","#"*50)
print(a5)
print(a5[1,1:,1:])  # Print the elements from row 1 to 2 and column 1 to 2 of a5 [[ 5  6][ 9 10]]
print("columns")
print(a5[1,:,:1])



#----------------------------------------------------itration---------------------------------------------------
# NumPy arrays support iteration, which allows for iterating over the elements of the array.
# Iteration can be used to access and modify the elements of the array.

for i in a1:
    print(i)  # Print each element of a1

for i in a2:  
    print(i)  # Print each row of a2

for i in a5:
    print(i)  # Print each row of a5

for i in a5.flat:
    print(i)  # Print each element of a5

for i in a5.flatten():
    print(i)  # Print each element of a5

for i in np.nditer(a5):
    print(i)  # Print each element of a5


# Transpose
# The transpose() method transposes the array, which means that it swaps the rows and columns of the array.     
# It takes no arguments.
# The transpose() method can be used to transpose the array.
# The transpose() method can also be used to transpose the array.
# The transpose() method can also be used to transpose the array.
print("#"*50,"printin transpose of a2","#"*50)
print(a2)  
print(a2.T)  # Print the transpose of a2





#-------------------------------------------stacking------------------------------
# Stacking is the process of joining two or more arrays along a new axis. 
# It can be used to combine multiple arrays into a single array.
# Stacking can be done along any axis, and it can be used to combine arrays of different shapes.


a6=np.arange(12).reshape(3,4)
a7=np.arange(12,24).reshape(3,4)
# ---------------------------------------------horizonatl stacking------------------------------
print("#"*50,"printin horizontal stacking","#"*50)
print(np.hstack((a6,a7)))  # Stack a6 and a7 horizontally

# ---------------------------------------------vertical  stacking------------------------------
print("#"*50,"printin vertical stacking","#"*50)
print(np.vstack((a6,a7)))  # Stack a6 and a7 vertically
# ---------------------------------------------depth stacking------------------------------ 
print("#"*50,"printin depth stacking","#"*50)
print(np.dstack((a6,a7)))  # Stack a6 and a7 depth-wise


#---------------------------------------------------------splitting---------------------------------------------------
# Splitting is the process of dividing an array into multiple sub-arrays.
# It can be used to split an array into multiple sub-arrays along a specified axis.
# Splitting can be done along any axis, and it can be used to split arrays of different shapes.


#horizontal splitting
print("#"*50,"printin horizontal splitting","#"*50) 
print(np.hsplit(a6,2))  # Split a6 into two sub-arrays horizontally
#vertical splitting
print("#"*50,"printin vertical splitting","#"*50)
print(np.vsplit(a6,3))  # Split a6 into three sub-arrays vertically