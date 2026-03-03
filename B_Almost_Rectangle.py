number_testcases = int(input())
elememts_index = []
for _ in range(number_testcases):
    matrix_elements = int(input())
    matrix = []
    
    for i in range(matrix_elements):
        row_str = input()
        row_str = list(row_str)
        for j in range(matrix_elements):
            if row_str[j] == "*":
                elememts_index.append((i,j))
                
        matrix.append(row_str)
    print(elememts_index)
# print(elememts_index)
        