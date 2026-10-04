import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

    total = len(a)* len(a[0])

    if total != new_shape[0] * new_shape[1]:
        return []

    result = []
    temp = []

    for row in a:
        for value in row:
            temp.append(value)

            if len(temp) == new_shape[1]:
                result.append(temp)
                temp = []

    return result
