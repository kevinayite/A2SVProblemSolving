t = int(input()) 

for _ in range(t):
    n, k = map(int, input().split()) 
    s = input().strip()  

    count = 0  # To count valid '1's

    for i in range(n):
        # Check if current character is '1'
        if s[i] == '1':
            # Determine the starting index of the window
            windows = max(0, i - k + 1)

            must_protect = False  # Flag to check if another '1' exists in the window

            # Check all positions in the window before index i
            for j in range(windows, i):
                if s[j] == '1':
                    # If another '1' is found, mark as protected
                    must_protect = True
                    break

            # If no previous '1' in the window, count this '1'
            if not must_protect:
                count += 1

    print(count) 