import sys
from collections import deque

def sol():
    M, N, H = map(int, input().split())
    grid = [ [ list(map(int, input().split())) for _ in range(N)] for _ in range(H) ]
    # grid inform [HIGH][ROW][COLUMN]
    start_point_lst = []
    # h = high, r = row, c = column
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if grid[h][r][c] == 1:
                    start_point_lst.append((h,r,c))
    bfs(grid,start_point_lst,H,N,M)
    ans = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if grid[h][r][c] == 0:
                    print(-1)
                    return
                elif ans < grid[h][r][c]:
                    ans = grid[h][r][c]
    print(ans-1)
def bfs(grid, start_point_lst, H,N,M):
    queue = deque()
    dir_6 = [ (-1,0,0), (1,0,0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    for h,r,c in start_point_lst:
        queue.append((h,r,c))
    
    while queue:
        h, r, c = queue.popleft()
        for high, R, C in dir_6:
            post_h, post_r, post_c = h + high, r + R, c + C
            if 0 <= post_h < H and 0<= post_r < N and 0<= post_c < M and grid[post_h][post_r][post_c] ==0:
                grid[post_h][post_r][post_c] = grid[h][r][c] + 1
                queue.append((post_h,post_r,post_c))

sol()