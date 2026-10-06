def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result = []
	for row in range(len(matrix)):
		num = 0
		temp = []
		
		for column in range(len(matrix[0])):
			num = matrix[row][column] * scalar
			temp.append(num)
		result.append(temp)

	return result
