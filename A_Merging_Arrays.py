first_arr, second_arr = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
i, j = 0,0

while i < first_arr and j < second_arr:
    if arr2[j]> arr1[i]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1
result.extend(arr1[i:])
result.extend(arr2[j:])
print(*result)


