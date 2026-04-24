t = int(input())  

for _ in range(t):
    n, k = map(int, input().split()) 
    
    s = input().strip()  

    result = "YES"          # assume it's possible unless proven otherwise
    permutation = []        # the resulting permutation
    low, high = 1, n        # pointers for smallest and largest available values
    consecutives_ones = 0   # counts current streak of consecutive '1's

    # iterate through each position
    for i in range(n):
        if s[i] == '0':
            # assign a large value to '0' positions
            # this ensures '0' positions dominate intervals
            permutation.append(high)
            high -= 1

            # reset consecutive '1's counter
            consecutives_ones = 0
        else:
            # assign a small value to '1' positions
            # this prevents them from becoming maximum
            permutation.append(low)
            low += 1

            # increase streak of consecutive '1's
            consecutives_ones += 1

            # if we reach k consecutive '1's → impossible
            if consecutives_ones >= k:
                result = "NO"
                break

    # print result after processing the whole string (or breaking early)
    print(result)

    # only print permutation if a valid one exists
    if result == "YES":
        print(*permutation)