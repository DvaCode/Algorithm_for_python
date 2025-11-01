import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = float("inf")

def dijstra(s, graph, N):
    
    distance = [INF] * (N + 1)
    distancce[s] = 0 
    pq = []
    heapq.heappush(pq, (0,s))
    
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

def sol():
    
    n, m, x = map(int, input().split())
    
    graph = defaultdict(list)
    graph_rev = defaultdict(list)
    
    for _ in range(m):
        u,v,w = map(int, input().split())
        graph[u].append((v,w))
        graph_rev[v].append((u,w))
        
    ans = -1
    dist_rev = dijstra(x, graph, n)
    for i in range(1, n+1):
        dist = dijstra(i, graph, n)
        
        if ans < dist[x] + dist_rev[i]:
            ans = dist[x] + dist_rev[i]
            
    print(ans)

if __name__ == "__main__":
    sol()