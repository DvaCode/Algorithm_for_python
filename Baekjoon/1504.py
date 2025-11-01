import sys
import heapq
from collections import defaultdict

INF = float('inf')
input = sys.stdin.readline

def sol():
    N, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        u,v,w = map(int, input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
        
    V1, V2 = map(int, input().split())
    
    dist = dijkstra(graph,1, N)
    dist1 = dijkstra(graph,V1, N)
    dist2 = dijkstra(graph,V2, N)
    
    sum1 = dist[V1] + dist1[V2] + dist2[N]
    sum2 = dist[V2] + dist2[V1] + dist1[N]
    ans = min(sum1, sum2)
    print(-1 if ans == INF else ans)
            

    # 목적지는 N
    # 거점 V1, V2
    
def dijkstra(graph, start, N):
    distance = [INF] * (N + 1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        
        for next_node, weight in graph[now]:
            cost = weight + dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    
    return distance

sol()