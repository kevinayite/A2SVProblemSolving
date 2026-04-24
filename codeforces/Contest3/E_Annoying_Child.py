import sys

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))

    # Sort coins in decreasing order so we always try to use the largest ones
    coins.sort(reverse=True)

    even = []          # list of even coins
    max_odd = 0        # largest odd coin

    # Separate even coins and find the maximum odd coin
    for num in coins:
        if num % 2 == 1:
            max_odd = max(max_odd, num)
        else:
            even.append(num)

    # Sum of all even coins
    sum_even = sum(even)

    # Smallest even coin (used later in parity adjustment)
    if even:
        smallest_even = even[-1]
    else:
        smallest_even = max_odd

    # ----------------------------
    # CASE 1: no odd coins exist
    # ----------------------------
    # Impossible to create an odd sum
    if max_odd == 0:
        print(" ".join(["0"] * n))
        continue

    answers = []

    # ---------------------------------
    # k = 1
    # Best result is the largest odd
    # ---------------------------------
    answers.append(max_odd)

    # Current sum while adding even numbers
    current_sum = max_odd

    # Pointer over even numbers
    e = 0

    # ---------------------------------
    # Compute answers for k = 2 ... n
    # ---------------------------------
    for k in range(2, n + 1):

        # ---------------------------------
        # FIRST PART OF CASE 3
        # Use even numbers with the max odd
        # odd + even = odd → safe
        # ---------------------------------
        if k <= len(even) + 1:
            current_sum += even[e]
            answers.append(current_sum)
            e += 1

        else:
            # ---------------------------------
            # SECOND PART OF CASE 3 / CASE 2
            # Only odd numbers remain
            # We must keep final sum odd
            # ---------------------------------

            extra_odds = k - (len(even) + 1)

            # If number of extra odds is odd → parity breaks
            if extra_odds % 2 == 1:
                if k == n:
                    answers.append(0)
                else:
                    answers.append(sum_even + max_odd - smallest_even)

            else:
                answers.append(sum_even + max_odd)

    # Print result
    print(*answers)