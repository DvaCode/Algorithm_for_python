import sys
from collections import deque
input = sys.stdin.readline

def sol():
    N = int(input())
    grid = [ list(map(int,input().strip())) for _ in range(N)]

    # 연결 정보가 담긴 인접 리스트 형태의 그래프가 필요함

    ans = []
    visited = [ [False]* N for _ in range(N) ]
    for r in range(N):
        for c in range(N):
            if grid[r][c] and not visited[r][c]:
                visited[r][c] = True
                ans.append(bfs(N, r, c, grid, visited))
    ans.sort()
    print(len(ans))
    for i in ans:
        print(i)

def bfs(N,r,c,grid, visited):
    queue = deque([(r,c)])
    cnt = 1
    dir4 = [ (-1,0), (1,0), (0,-1), (0, 1) ]
    while queue:
        u_row, u_column = queue.popleft()

        for sr, sc in dir4:
            if 0<= u_row + sr < N and 0 <= u_column + sc < N:
                if grid[u_row+sr][u_column+sc] and not visited[u_row+sr][u_column+sc]:
                    visited[u_row+sr][u_column+sc] = True
                    queue.append((u_row+sr, u_column+sc))
                    cnt += 1
    return cnt

sol()
