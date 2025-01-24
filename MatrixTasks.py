def find_minimum(matrix):
    min_element = matrix[0][0]
    
    for row in matrix: 
        for element in row:
            if element < min_element:
                min_element = element
    return min_element

matrix = [[2, 5, 7], [4,11,66], [77, 0, 9]]
print(find_minimum(matrix))


def sum_of_all(matrix):
    sum = 0 

    for row in matrix:
        for elements in row:
            sum += elements

    return sum
matrix = [[2, 5, 7], [4,11,66], [77, 0, 9]]
print(sum_of_all(matrix))


def occurrence_target(matrix, target):
    count = 0 
    
    for row in matrix:
        for element in row:
            if element == target:
                count += 1

    return count

matrix = [[2, 5, 7], [4,77,66], [77, 0, 9]]
target = 77
print(occurrence_target(matrix, target))


def find_indincies(matrix, target):
    indincies = []
    
    num_rows = len(matrix)
    for i in range(num_rows):
        num_cols = len(matrix[0])

        for j in range(num_cols):
            if matrix[i][j] == target:
                indincies.append([i, j])
    return indincies

matrix = [[2, 5, 7], [4,77,66], [77, 0, 9]]
target = 77
print(find_indincies(matrix, target))


def calculate_diagnol(matrix):
    diagonal_count = 0
    
    for num in range(len(matrix)):
        diagonal_count += matrix[num][num]
    return diagonal_count

matrix = [[2, 5, 7], [4,77,66], [77, 0, 9]]
print(calculate_diagnol(matrix))


def sum_of_secondary_calculate(matrix):
    n = len(matrix)
    all_sum = 0

    for i in range(n):
        all_sum += matrix[i][n-i-1]
    return all_sum
matrix = [[2, 5, 7], [4,77,66], [77, 0, 9]]
print(sum_of_secondary_calculate(matrix))

def column_calculate(matrix):
    num_of_columns = len(matrix[0])
    max_num_of_columns = []

    for column in range(num_of_columns):
        max_value = matrix[0][column]

        for row in range(0, len(matrix)):
            if matrix[row][column] > max_value:
                max_value = matrix[row][column]
        max_num_of_columns.append(max_value)
    return max_num_of_columns
matrix = [[2, 5, 7],
          [4,77,66], 
          [77, 0, 9]]
print(column_calculate(matrix))


def find_row_max(matrix):
    max_sum = 0
    max_row_index = -1
    for i in range(len(matrix)):
        row_sum = sum(matrix[i])

        if row_sum > max_sum:
            max_sum = row_sum
            max_row_index = i
    return max_row_index, max_sum
matrix = [[2, 5, 7],
          [4,77,66], 
          [77, 0, 9]]
print(find_row_max(matrix))


def find_column_min(matrix):
    min_sum = 98898989
    min_column_index = -1

    num_columns = len(matrix[0])
    num_rows = len(matrix)
    
    for i in range(num_columns):
        col_sum = 0

        for j in range(num_rows):
            col_sum += matrix[j][i]

        if col_sum < min_sum:
            min_sum = col_sum
            min_column_index = i

    return min_column_index, min_sum

matrix = [[2, 5, 7],
          [4,77,66], 
          [77, 0, 9]]
print(find_column_min(matrix))


def count_individuals(matrix):
    individual_nums = {}
    
    for row in matrix:
        for num in row:
            if num in individual_nums:
                individual_nums[num] += 1
            else:
                individual_nums[num] = 1
    return individual_nums

matrix = [
    [2, 5, 7], 
    [4,77,66], 
    [77, 0, 9]]
print(count_individuals(matrix))