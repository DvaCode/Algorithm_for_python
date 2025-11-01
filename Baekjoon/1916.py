import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = float("inf")

def sol():
    N = int(input())
    M = int(input())
    
    graph = defaultdict(list)
    distance = [INF] * (N + 1)
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v,w))
    
    A, B = map(int, input().split())
    
    distance[A] = 0
    
    pq = []
    heapq.heappush(pq, (0,A))
    
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        
        for next_node, weight in graph[now]:
            cost = weight + dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    
    print(distance[B])

sol()