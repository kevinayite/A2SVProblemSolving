number_test_cases = int(input())
for _ in range(number_test_cases):
    n = int(input())
    if n<= 3:
        print(n)
    elif n % 2 ==0:
        print(0)
    else:
        print(1)
        