"""Accessing array elements."""

import numpy as np 

def test_run():
	a = np.random.rand(5,4)
	print "Array:\n", a

	"""Accessing elements in an array:"""	

	# # Accessing element at position (3, 2)
	# print a[3, 2] 

	# # Accessing elements in defined range
	# print a[0, 1:3]
	# print a[0:2, 0:2]

	# # Slicing [n:m:t] specifies a range that starts at n, and stops before m, in steps of size t
	# print a[:, 0:3:2] # will select columns 0, 2 for every row

	"""Modifying array elements:"""

	# Assigning a value to a patilular location:
	# a[0, 0] = 1
	# print "\nModified (replaced one element):\n", a

	# a[0,:] = 2
	# print "\nModified (replaced a row with a single value):\n", a

	# a[:, 3] = [1,2,3,4,5]
	# print "\nModified (replaced a column with a list):\n", a





if __name__ == '__main__':
	test_run()