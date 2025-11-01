import sys
import heapq
from collections import defaultdict

INF = float('inf')
input = sys.stdin.readline

def sol():
    graph = defaultdict(list)
    
    N = int(input())
    friend_lst = list(map(int, input().split()))
    M = int(input())
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    lst = []
    tp = [] # size N, last element N-1
    for fri in friend_lst:
        lst.append(dijkstra(graph, fri, N))
    # lst[0] = distance lst at start A
    # lst[1] = distance lst at start B
    # lst[2] = distance lst at start C
    
    for idx in range(1, N+1):
        tp.append((lst[0][idx], lst[1][idx], lst[2][idx]))
    # tp = [ (1,2,3), (3,4,5), (...), ... ]
    max_val = -1
    max_idx = -1
    idx = 0
    for val1, val2, val3 in tp:
        if max_val < min(val1,val2,val3):
            max_val = min(val1,val2,val3)
            max_idx = idx
        idx += 1
    # print(max_val, max_idx)
    # print(tp[max_idx])
    # print(tp[4])
    # print(tp)
    idx = 0
    ans = []
    for val1, val2, val3 in tp:
        if min(tp[max_idx]) == min(val1,val2,val3):
            ans.append(idx+1)
        idx += 1
    # print(ans)
    print(min(ans))

def dijkstra(graph, friend_No, N):
    distance = [INF] * (N + 1)
    distance[friend_No] = 0
    pq = []
    heapq.heappush(pq, (0, friend_No))
    
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