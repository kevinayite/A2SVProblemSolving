number_test_cases = int(input())
for _ in range(number_test_cases):
    a, b , c = map(int, input().split())
    nums = [a, b, c]
    increments = 5
    while increments > 0:
        nums.sort()          
        nums[0] += 1         
        increments -= 1
    a, b, c = nums
    print(a * b * c)
