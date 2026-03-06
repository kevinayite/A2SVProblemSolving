first_lenght, second_lenght = map(int, input().split())
first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))
counter = 0
result = []
for i in range(second_lenght):
    while counter < first_lenght and first_arr[counter] < second_arr[i]:
        counter += 1
    result.append(counter)
print(*result)