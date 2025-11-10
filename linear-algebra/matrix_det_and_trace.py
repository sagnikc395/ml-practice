import numpy as np

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	trace = 0 
	for row_idx, row in enumerate(matrix):
		for col_idx,col in enumerate(row):
			if row_idx == col_idx:
				trace += matrix[row_idx][col_idx]
	determinant = np.linalg.det(matrix)
	return (determinant,trace)
	

						
			