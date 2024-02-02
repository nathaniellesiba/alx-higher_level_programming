#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):

try:
# Convert the input lists into numpy arrays and perform matrix multiplication
result = np.dot(np.array(m_a), np.array(m_b))
return result
except ValueError:
raise ValueError("m_a and m_b can't be multiplied")
except Exception as e:
raise type(e)(str(e))

