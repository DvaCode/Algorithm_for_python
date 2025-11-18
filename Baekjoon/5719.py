# 5719.py
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = float("inf")

def sol():
    # 최단 경로 탐색, if distance[Destination] != INF
    # dijkstra 알고리즘 다시 돌림
    # 값 초기화
    # 최단 경로에 포함된 도로들은 먼저 방문 처리
    # 거의 최단 경로 탐색
    # if exist, print(dist[D]) else print(-1)
    def dijkstra(graph, S, distance):

        pq = []
        heapq.heappush(pq, (0, S))

        while pq:
            dist, now = heapq.heappop(pq)
            if dist > distance[now]:
                continue
            for next, weight in graph[now]:
                cost = weight + dist
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(pq, (cost, next))
        return distance

    def dijkstra_remove(graph, graph_rev, D, N, distance):

        distance_rev = [INF] * N
        distance_rev[D] = 0
        Dist = distance[D]
        distance_rev = dijkstra(graph_rev, D, distance_rev)
        to_delete = {}

        for idx in range(N):
            for v, w in graph[idx]:
                if Dist == distance_rev[v] + distance[idx] + w:
                    to_delete.setdefault(idx, set()).add((v,w,))

        for u, edges in to_delete.items():
            lst = graph.get(u)
            if not lst:
                continue
            lst[:] = [(to, wt) for (to, wt) in lst if (to, wt) not in edges]
            if not lst:
                del graph[u]

    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        graph = defaultdict(list)
        graph_rev = defaultdict(list)
        S, D = map(int, input().split())
        for _ in range(M):
            U, V, dist = map(int, input().split())
            graph[U].append((V,dist))
            graph_rev[V].append((U,dist))

        distance = [INF] * N
        distance[S] = 0

        distance = dijkstra(graph, S, distance)
        if distance[D] == INF:
            print(-1)
            continue
        dijkstra_remove(graph, graph_rev, D, N, distance)

        distance = [INF] * N
        distance[S] = 0
        distance = dijkstra(graph, S, distance)
        if distance[D]!= INF:
            ans = distance[D]
        else:
            ans = -1
        print(ans)

sol()
