def solve():
    s = input().strip()
    t = input().strip()

    if len(s) != len(t):
        print("No")
        return

    vowels = set("aeiou") # we are using set here because it's time complexity is O(1)
#     x in ['a','e','i','o','u']	O(n)
# x in "aeiou"	O(n)
# 	x in {'a','e','i','o','u'}	O(1)

    for i in range(len(s)):
        if (s[i] in vowels) != (t[i] in vowels):
            print("No")
            return

    print("Yes")

solve()