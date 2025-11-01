import sys
import heapq
from collections import defaultdict

INF = float("inf")
input = sys.stdin.readline

def sol():
    N, M, K = map(int, input().split())
    
    graph_rev = defaultdict(list) # 역 그래프

    
    for _ in range(M):
        u,v,c = map(int, input().split())
        graph_rev[v].append((u,c))

    k_lst = list(map(int, input().split())) # 면접장 리스트
    
    
    ans = [ -1, -1 ] # 거리가 최대일 때 도시 번호, 면접장에서의 최대 거리
    ans = dijstra(k_lst, graph_rev, N)
    for i in ans:
        print(i)

def dijstra(k_lst, graph_rev, N):
    distance = [INF] * (N + 1)
    pq = []
    for i in k_lst:
        distance[i] = 0
        heapq.heappush(pq, (0,i))
    
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        for next_node, weight in graph_rev[now]:
            cost = weight + dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    
    # 최대 반환
    max_value = [-1, -1]
    for i in range(N + 1):
        if distance[i] != INF:
            if max_value[1] < distance[i]:
                max_value[0] = i
                max_value[1] = distance[i]
    
    return max_value

sol()