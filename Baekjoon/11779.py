import sys
import heapq
from collections import defaultdict

INF = float('inf')
input = sys.stdin.readline
def sol():
    N = int(input())
    M = int(input())
    graph = defaultdict(list)
    for _ in range(M):
        u,v,w = map(int, input().split())
        graph[u].append((v,w))
    
    A, B = map(int, input().split())
    
    distance = [INF] * (N + 1)
    
    visited_city_lst = [-1] * ( N + 1)
    
    
    dijkstra(graph, distance, visited_city_lst, A)
    a = B
    count = 1
    b = []
    b.append(a)
    while visited_city_lst[a] != -1:
        b.append(visited_city_lst[a])
        a = visited_city_lst[a]
        count += 1
    print(distance[B])
    print(count)
    print(*b[::-1])
    
def dijkstra(graph, distance, visited_city_lst, A):
    pq = []
    distance[A] = 0
    heapq.heappush(pq, (0, A))
    
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
                visited_city_lst[next_node] = now

sol()