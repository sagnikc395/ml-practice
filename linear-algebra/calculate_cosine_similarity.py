
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	mag_v1 = np.linalg.norm(np.array(v1))
	mag_v2 = np.linalg.norm(np.array(v2))
    result = np.dot(np.array(v1),np.array(v2))
    res = result / (mag_v1 * mag_v2)
    return float("{:.3f}".format(res))
