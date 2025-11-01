import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def sol():
    N = int(input())
    V = int(input())
    graph = defaultdict(list)
    for _ in range(V):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = bfs(graph, N)
    print(cnt)

def bfs(graph, N):
    visited = [False] * (N + 1)
    queue = deque([1])
    visited[1] = True
    cnt = 0

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    cnt = sum(1 for i in visited[1:] if i)
    return cnt - 1

sol()
