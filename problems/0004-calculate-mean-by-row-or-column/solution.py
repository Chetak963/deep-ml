def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	# result = []
	# temp = []
	# if mode == 'column':
	# 	for c in range(len(matrix[0])):
	# 		num = 0
	# 		count = 0
	# 		for r in range(len(matrix)):
	# 			num += matrix[r][c]
	# 			count = count + 1
	# 		num = num / count
	# 		temp.append(num)
	# elif mode == 'row':
	# 	for r in range(len(matrix)):
	# 		num = 0
	# 		count = 0 
	# 		for c in range(len(matrix[0])):
	# 			num += matrix[r][c]
	# 			count = count + 1
	# 		num = num / count
	# 		temp.append(num)
	# return temp


	

    if mode == 'column':
        return [
            sum(row[c] for row in matrix) / len(matrix)
            for c in range(len(matrix[0]))
        ]

    elif mode == 'row':
        return [
            sum(row) / len(row)
            for row in matrix
        ]