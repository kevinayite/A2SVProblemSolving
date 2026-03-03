# # Implementation of Bubble sort
array = [64, 25, 12, 22, 11]
size = len(array)
for i in range(size):
    for j in range(size - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]


# #Implementation of Selection Sort
array = [64, 25, 12, 22, 11]
size = len(array)
for i in range(size):
    min_idx = i
    for j in range(i + 1, size):
        if array[min_idx] >= array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]
return array

# # #Implementation of Insertion Sort

array = [64, 25, 12, 22, 11]
size = len(array)
for i in range(1, size):
    key = array[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
return array






costs = [1,3,2,5,1,3]
students = [1,2,3,4,5,6]
studentToCost = {}
for idx in range(len(students)):
    studentToCost[students[idx]] = costs[idx]
def customComparator(item):
    return studentToCost[item]
students.sort(key = customComparator)
print(students)
