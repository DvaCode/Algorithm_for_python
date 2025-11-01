import sys
import heapq
from collections import defaultdict

INF = float('inf')
input = sys.stdin.readline



def dijstra(s, graph, distance):
    pq = []
    heapq.heappush(pq, (0, s))
        
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
                
def sol():
    V, E = map(int, input().split())
    start = int(input())
    graph = defaultdict(list)
    
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v,w))

    distance = [INF] * (V + 1)
    distance[start] = 0
    
    dijstra(start, graph, distance)
    for i in range(1, V + 1):
        print("INF" if distance[i] == INF else distance[i])
    


if __name__ == "__main__":
    sol()