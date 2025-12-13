#Code 1 
matrix = []
print("Enter the elements of the 3x3 matrix:")
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1} (3 integers separated by space): ").split()))
    matrix.append(row)

main_diag_sum = sum(matrix[i][i] for i in range(3))
secondary_diag_sum = sum(matrix[i][2 - i] for i in range(3))

print("Sum of main diagonal:", main_diag_sum)
print("Sum of secondary diagonal:", secondary_diag_sum)

# Code 2 

matrix = []
print("Enter the elements of the 3x3 matrix:")
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1} (3 integers separated by space): ").split()))
    matrix.append(row)

num = int(input("Enter a number to search: "))

count = sum(row.count(num) for row in matrix)

print(f"The number {num} appears {count} time(s) in the matrix.")


# Code 3 
matrix = []
print("Enter the elements of the 3x3 matrix:")
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1} (3 integers separated by space): ").split()))
    matrix.append(row)

for col in range(3):
    max_val = max(matrix[row][col] for row in range(3))
    print(f"Maximum value in column {col+1}: {max_val}")





