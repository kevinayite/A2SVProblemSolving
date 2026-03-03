number_testcase = int(input())
result = 0
for _ in range(number_testcase):
    operation = input()
    if operation == "++X" or operation == "X++":
        result+=1
    elif operation =="--X" or operation == "X--":
        result-=1
print(result)