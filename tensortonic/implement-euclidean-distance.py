import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    arr_x = np.array(x)
    arr_y = np.array(y)

    diff = arr_x - arr_y
    return np.linalg.norm(diff,ord=2)
