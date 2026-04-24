
def solve():
    # Score before Kevin left
    score1_team1, score1_team2 = map(int, input().split())
    # Score when Kevin returned
    score2_team1, score2_team2 = map(int, input().split())
    
    # A tie is unavoidable if and only if the leading team switches.
    # Case 1: team 1 was leading before, team 2 is leading after
    team1_led_then_lost = score1_team1 > score1_team2 and score2_team1 < score2_team2
    # Case 2: team 2 was leading before, team 1 is leading after
    team2_led_then_lost = score1_team1 < score1_team2 and score2_team1 > score2_team2

    if team1_led_then_lost or team2_led_then_lost:
        print("NO")
    else:
        print("YES")
t = int(input())
for _ in range(t):
    solve()