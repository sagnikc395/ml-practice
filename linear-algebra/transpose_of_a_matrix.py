import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	mat_a = np.array(a)
	mat_a_t = mat_a.T 
	return mat_a_t 