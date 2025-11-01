import sys
import heapq

input = sys.stdin.readline
INF = float("inf")

def sol():
    N, M = map(int, input().split())
    # 변수 선언 및 초기화 부분
    grid = [ list(map(int, input().split())) for _ in range(N) ]
    graph = [ [ set() for _ in range(M) ] for _ in range(N) ]
    target_point_r, target_point_c = find_target_point(N,M, grid) # target

    dir4 = [ (-1,0), (1, 0), (0, 1), (0, -1) ]
    distance = [ [INF] * M for _ in range(N) ]
    zero_lst = []
        
    distance[target_point_r][target_point_c] = 0 # 시작점 초기
    
    for row in range(N):
        for column in range(M):
            if grid[row][column] != 0:
                for x, y in dir4:
                    if 0 <= row + x < N and 0 <= column + y < M and grid[row+x][column+y] != 0:
                        graph[row][column].add((row+x, column+y, 1))
            else:
                zero_lst.append((row,column))

    dijkstra(graph, distance, target_point_r, target_point_c) # 다익스트라 호출
    
    for row, column in zero_lst: # 갈 수 없는 땅 셋팅
        distance[row][column] = 0
    for row in range(N):
        for column in range(M):
            if distance[row][column] == INF:
                distance[row][column] = -1
    for ans in distance:
        print(*ans)


def dijkstra(graph, distance, r, c):
    # start = (r,c)
    pq = []
    heapq.heappush(pq, (0, r, c))
    
    while pq:
        dist, now_r, now_c = heapq.heappop(pq)
        if dist > distance[now_r][now_c]:
            continue
        for next_r, next_c, weight in graph[now_r][now_c]:
            cost = dist + weight
            if cost < distance[next_r][next_c]:
                distance[next_r][next_c] = cost
                heapq.heappush(pq, (cost, next_r, next_c))
        
def find_target_point(n, m, grid):
    # 목표 지점 찾는 함수
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 2:
                target_point_R, target_point_C = r,c
                return target_point_R, target_point_C
    return None

sol()