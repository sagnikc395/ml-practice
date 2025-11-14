import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	try:
		#Write your code here and return a python list after reshaping by using numpy's tolist() method
		arr = np.array(a)
		arr_reshape = np.reshape(arr,new_shape)
		return arr_reshape
	except ValueError as e:
		return []

	
