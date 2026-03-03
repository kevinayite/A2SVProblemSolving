w, t = map(int, input().split())
result = "The Fallen Champion"
number_test_cases = int(input())
for _ in range(number_test_cases):
    win, time = map(int, input().split())
    if (win > w or win==w) and time < t:
        result = "The Fallen Champion"
        break
    else:
        result = "The Champion Saves the Accused"
print(result)
