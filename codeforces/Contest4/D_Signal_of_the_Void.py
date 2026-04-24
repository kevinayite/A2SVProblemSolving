t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    hubs = []
    for i in range(n):
        if b[i] < p:
            hubs.append((b[i], a[i]))
    hubs.sort() # it will be sorted according to b[i]
    total_cost = p
    total_reached = 1
    for cost_relay, capacity in hubs:
        if total_reached >= n: # no need to continue
            break
        needed = n - total_reached
        can_reach = min(capacity, needed)  

        total_cost += can_reach * cost_relay
        total_reached += can_reach

    if total_reached < n: # here we are done with our distribution with the hub
    # and it is less costly to share from the earth
        total_cost += (n - total_reached) * p
    print(total_cost)

