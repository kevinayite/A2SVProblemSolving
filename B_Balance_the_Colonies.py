number_test_cases = int(input())
for _ in range(number_test_cases):
    n = int(input())
    if n%2 ==0:
        number_groups = n//2
    elif n%3 ==0:
        number_groups = n//3
    else:
        
