# numbers = list(map())
numbers = list(map(str,input().split("+")))
numbers.sort()
if len(numbers)> 1:
    print("+".join(numbers))
else:
    print(numbers[0])