t = int(input())  

for _ in range(t):
    n, c , d = map(int, input().split())
    b = list(map(int, input().split()))
    first_element = min(b) # if we understand the problem, 
    #the min of be will be the first array
    # so let's construct the array now as we know the first element
    # using a[i][j] = first_element + i*c + j*d (0-indexed)
    expected_result = []
    for row in range(n):
        for col in range(n):
            expected_result.append(first_element + row*c + col*d)
    if sorted(expected_result) == sorted(b): # checking if there is a match
        print("YES")
    else:
        print("NO")


"""
Explanation of the formula `a[i][j] = start + i*c + j*d`:

1. The progressive square rules:
   - Vertical: a[i+1][j] = a[i][j] + c
   - Horizontal: a[i][j+1] = a[i][j] + d

2. Start from a[0][0] = start.

3. First column (j=0) illustrates the vertical addition:
   case (1,1): a[1,1] = start
   case (2,1): a[2,1] = a[1,1] + c = start + 1*c
   case (3,1): a[3,1] = a[1,1] + 2*c
   ...
   case (i,1): a[i,1] = a[1,1] + (i-1)*c

4. First row (i=0) similarly illustrates horizontal addition:
   a[0,j] = start + j*d

5. Combining vertical and horizontal moves:
   a[i][j] = start + i*c + j*d

6. Example:
   start = 1, c = 2, d = 3, n = 3
   Matrix:
       1   4   7
       3   6   9
       5   8  11
   Each step down adds c, each step right adds d.
"""