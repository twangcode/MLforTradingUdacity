"""Array Indexing"""

import numpy as np 

def test_run():

	# a = np.random.rand(5)
	# print a

	# # accessing using list of indices
	# indices = np.array([1,1,2,3])
	# print a[indices]

	a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
	print a

	#calculating mean
	mean = a.mean()
	print mean

	#masking
	print a<mean
	print a[a<mean]
	a[a<mean] = mean
	print a

if __name__ == '__main__':
	test_run()
