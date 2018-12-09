"""Accessing array elements."""

import numpy as np 

def test_run():
	a = np.random.rand(5,4)
	print "Array:\n", a

	# Accessing element at position (3, 2)
	print a[3, 2] 

	# Accessing elements in defined range
	print a[0, 1:3]
	print a[0:2, 0:2]

	# Slicing [n:m:t] specifies a range that starts at n, and stops before m, in steps of size t
	print a[:, 0:3:2] # will select columns 0, 2 for every row

if __name__ == '__main__':
	test_run()