n = int(input())
for _ in range(n):
    word = input()
    if len(word) > 10:
        middle = str(len(word) -2)
        print(word[0] + middle + word[-1])
    else:
        print(word)
