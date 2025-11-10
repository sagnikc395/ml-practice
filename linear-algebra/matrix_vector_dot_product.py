import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	mat_a = np.array(a)
	vec_b = np.array(b)
	
    #shape compatibility
	if mat_a.shape[1] != vec_b.shape[0]:
		return -1
	result = np.dot(mat_a,vec_b)
	return result.tolist()