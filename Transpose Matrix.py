user_input = eval(input("Enter matrix in []: "))
result = []
for row in range(len(user_input[0])):
    matrix = []
    for column in range(len(user_input)):
        matrix.append(user_input[column][rrow])
    result.append(matrix)
print(result)