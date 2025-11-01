import sys
import heapq
from collections import defaultdict

INF = float("inf")
input = sys.stdin.readline

def sol():
    grid = []

    dir_4 = [ (1,0), (-1,0), (0, 1), (0, -1) ]
    
    ans = 0
    count = 1
    while True:
        N =  int(input())
        if N == 0:
            return
        grid = [list(map(int, input().split())) for _ in range(N)]
        graph = defaultdict(list)
        for row in range(N):
            for column in range(N):
                idx = row * N + column
                for r, c in dir_4:
                    if 0 <= row + r < N and 0 <= column + c < N:
                        graph[idx].append(((row+r)*N + column+c, grid[row+r][column+c]))

        ans = dijkstra(grid, graph, N)
        print(f"Problem {count}: {ans}")
        count += 1

def dijkstra(grid,graph, N):
    SIZE = N * N
    distance = [INF] * (SIZE)
    distance[0] = grid[0][0] # 값 초기화

    pq = []
    heapq.heappush(pq, (distance[0], 0))
    
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        for next_node, weight in graph[now]:
            cost = weight + dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    # print(distance)
    return distance[SIZE - 1]

sol()