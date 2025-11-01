import sys
import heapq
from collections import defaultdict

INF = float('inf')
input = sys.stdin.readline

def sol():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    distance = [INF] * (N + 1)
    distance[1] = 0
    dijkstra(distance, graph)
    # print(distance)
    print(distance[N])

def dijkstra(distance, graph):
    pq = []
    heapq.heappush(pq, (0,1))
    
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

sol()