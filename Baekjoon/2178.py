import sys
from collections import deque

input = sys.stdin.readline

def sol():
    N, M = map(int, input().split())
    grid = [ list(map(int, input().strip())) for _ in range(N) ]
    ans = bfs(grid, N, M)
    print(ans[N-1][M-1])

def bfs(grid, N, M):
    queue = deque([(0,0)])
    visited = [ [False] * M for _ in range(N) ]
    Dir4 = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    cnt = 1
    ans_matrix = [[0] * M for _ in range(N)]
    ans_matrix[0][0] = 1

    while queue:
        r, c = queue.popleft()
        visited[r][c] = True

        for dir_r, dir_c in Dir4:
            if 0 <= dir_r + r < N and 0 <= dir_c + c < M:
                if not visited[dir_r + r][dir_c + c] and grid[dir_r + r][dir_c + c]:
                    visited[dir_r + r][dir_c + c] = True
                    queue.append((dir_r + r, dir_c + c))
                    ans_matrix[dir_r + r][dir_c + c] = ans_matrix[r][c] + 1

    return ans_matrix
sol()
