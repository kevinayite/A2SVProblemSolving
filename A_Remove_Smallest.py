import math
number_of_test_cases = int(input())
for _ in range(number_of_test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    i = 0
    while i < len(arr) - 1:
        if abs(arr[i] - arr[i+1]) <= 1:
            if arr[i] < arr[i+1]:
                arr.pop(i)
            elif arr[i] == arr[i+1]:
                arr.pop(i)
            else:
                i+=1
        else:
            i += 1
    if len(arr) == 1:
        print("YES")
    else: 
        print("NO")
    