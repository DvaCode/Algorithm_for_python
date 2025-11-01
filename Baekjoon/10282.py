import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = float("inf")

def sol():
    T = int(input())
    for _ in range(T):
        n, d, c = map(int, input().split())
        graph = defaultdict(list)
        distance = [INF] * (n + 1)
        distance[c] = 0
        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((a,s))

        count, time = dijkstra(graph, distance, c)
        print(f"{count} {time}")

def dijkstra(graph, distance, start):
    pq = []
    heapq.heappush(pq, (0, start))
    cnt = 1
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue

        for next_node, weight in graph[now]:
            cost = weight + dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    cnt = sum(1 for i in distance[1:] if i != INF)
    max_num = -1
    for num in distance[1:]:
        if max_num < num and num != INF: max_num = num
    return cnt, max_num

sol()
