import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    visited = [[False] * m for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_volume = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and not visited[i][j]:
                # BFS to find the full lake and compute its volume
                volume = 0
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    r, c = queue.popleft()
                    volume += grid[r][c]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] != 0:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                max_volume = max(max_volume, volume)

    print(max_volume)

t = int(input())
for _ in range(t):
    solve()