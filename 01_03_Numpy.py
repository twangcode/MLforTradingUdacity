'''Creating Numpy arrays. '''

import numpy as np 

def get_max_index(a):
	"""Return the index of the maximum value in given 1D array."""
	return a.argmax()
	
def test_run():
	#List to 1-D array
	# print np.array([2,3,4])
	print np.array([(2,3,4), (5,6,7)])
	
	# Empty array
	# print np.empty(5)
	# print np.empty((5,4))

	#Array of 1s, specifying the datatype
	# print np.ones((5,4), dtype=np.int_)

	# Generate an array full of random numbers, uniformly sampled from [0.0, 1.0)
	# print np.random.random((5,4)) # pass in a size tuple
	# print np.random.rand(5,4) # same as random different in syntax
	# print np.random.normal(0, 10, size=(2,3))
	# print np.random.randint(0,10,size=(2,3))

	# Array attributes:
	# a = np.random.random((5,4))
	# print a
	# print a.shape
	# print a.shape[0] # row
	# print a.shape[1] # column
	# print len(a.shape) # dimensions
	# print a.size # number of elements
	# print a.dtype # data type	

	# np.random.seed(693) # seed the random number generator, get same output every time
	# a = np.random.randint(0,10,size=(5,4)) 
	# print "Array:\n", a	

	# #Sum of all elements
	# print "Sum of all elements: ", a.sum()
	# print "Sum of each column:\n", a.sum(axis=0)
	# print "Sum of each row:\n", a.sum(axis=1)

	# Statistics: min, max, mean(across rows, cols, and overall)
	# print "Minimum of each column:\n", a.min(axis=0)
	# print "Maximum of each row:\n", a.min(axis=1)
	# print "Mean of all elements:", a.mean()

	# a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32) # 32-bit integer array 
	# print "Array:", a 
	# # Find the maximum and its index in array 
	# print "Maximum value:", a.max() 
	# print "Index of max.:", get_max_index(a)	


if __name__ == '__main__':
	test_run()