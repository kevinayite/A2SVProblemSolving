number_test_cases = int(input())
for _ in range(number_test_cases):
    n, k = map(int, input().split())
    health_arr = list(map(int, input().split()))
    position_arr =  list(map(int, input().split()))
    monsters = []
    for i in range(n):
        monsters.append(((abs(position_arr[i])), health_arr[i]))
    monsters.sort() # by default it will sort accoring to the position_arr
    total_health = 0
    possible = True
    for dist, health in monsters:
        total_health += health
        if total_health > k * dist:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")
