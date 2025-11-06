#수정 버전
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def same(a,b):
    return a == b

def weak(a,b):
    if a == 'B' or b == 'B':
        return a == b
    return True

def sol():
    N = int(input())
    grid = [ list(input().strip()) for _ in range(N) ]
    ans, ans_ = bfs(grid, N, same), bfs(grid, N, weak)
    print(f"{ans} {ans_}")

def bfs_(grid, visited, N, r, c, cmp):
    queue = deque([(r,c)])
    dir4 = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    visited[r][c] = True

    while queue:
        row, column = queue.popleft()

        for dr, dc in dir4:
            if 0 <= dr + row < N and 0 <= dc + column < N:
                if not visited[dr + row][dc + column] and cmp(grid[dr + row][dc + column], grid[row][column]):
                    queue.append((dr + row, dc + column))
                    visited[dr + row][dc + column] = True

def bfs(grid, N, cmp):
    visited = [ [False] * N for _ in range(N) ]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                bfs_(grid, visited, N, r, c, cmp)
                cnt += 1
    return cnt

sol()
