number_test_cases = int(input())
for _ in range(number_test_cases):
    lenght = int(input())
    string = list(input())
    count = 0

    

    i = 0
    while i < lenght :
        if string[i]!= string[i+1]:
            string[i], string[i+1] = string[i+1], string[i]
            count +=1
        i +=2
        if i == lenght -1:
            break
    print(count)
  