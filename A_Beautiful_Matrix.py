import math
matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            row_index, col_index = i,j         
print(sum([abs(row_index -2),abs(col_index - 2) ]))