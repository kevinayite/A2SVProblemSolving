number_testcase = int(input())
number_of_solved = 0
for _ in range(number_testcase):
    a,b,c = map(int, input().split())
    if sum([a,b,c])>=2:
        number_of_solved+=1
print(number_of_solved)
