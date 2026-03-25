import sys

read_input = sys.stdin.readline

num_tests = int(read_input())
results = []

for _ in range(num_tests):
    length = int(read_input())
    numbers = list(map(int, read_input().split()))
    
    numbers.sort()
    unique_values = sorted(set(numbers))
    
    max_group_size = 0
    left_pointer = 0
    
    for right_pointer in range(len(unique_values)):
        while unique_values[right_pointer] - unique_values[left_pointer] > length - 1:
            left_pointer += 1
            
        current_size = right_pointer - left_pointer + 1
        max_group_size = max(max_group_size, current_size)
    
    results.append(str(max_group_size))

print('\n'.join(results))