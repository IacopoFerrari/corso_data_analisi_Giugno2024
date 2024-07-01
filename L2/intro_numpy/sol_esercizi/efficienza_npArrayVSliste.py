import time
# Defining the size of the arrays
SIZE = 1000000

# Creating lists and NumPy arrays of integers from 0 to SIZE - 1
list1 = range(SIZE)
list2 = range(SIZE)
arra1 = np.arange(SIZE)
arra2 = np.arange(SIZE)

# Measuring the time taken to aggregate elements from each iterable using a list comprehension
start_list = time.time()  # Marking the start time
result = [x+y for x, y in zip(list1, list2)]  # Aggregating elements from 'list1' and 'list2' using list comprehension
print("Time to aggregate elements from each of the iterables:")
print("List:")
print((time.time() - start_list) * 1000)  # Printing the execution time in milliseconds

# Measuring the time taken to add NumPy arrays element-wise
start_array = time.time()  # Marking the start time
result = arra1 + arra2  # Performing element-wise addition on 'arra1' and 'arra2' using NumPy
print("NumPy array:")
print((time.time() - start_array) * 1000)  # Printing the execution time in milliseconds
