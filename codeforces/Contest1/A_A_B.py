number_test_cases = int(input())
for _ in range(number_test_cases):
    operation = input()
    print(sum([int(operation[0]), int(operation[-1])]  ))