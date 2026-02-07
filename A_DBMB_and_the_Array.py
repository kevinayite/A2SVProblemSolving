number_test_case = int(input())
for _ in range(number_test_case):
    arr = list(map(int, input().split()))
    gift = list(map(int, input().split()))
    n = arr[0]
    s = arr[1]
    x = arr[2]
    sum_elements = sum(gift)
    diff = s - sum_elements
    
    if diff == 0:
        print("YES")
    
    elif diff < 0:
        print("NO")
        
    elif diff % x == 0:
        print("YES")
        
    else:
        print("NO")