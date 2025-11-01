import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def sol():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (N + 1)

    ans = 0
    for idx in range(1,N+1):
        if not visited[idx]:
            bfs(graph, visited, idx)
            ans += 1
    print(ans)
def bfs(graph, visited, start):

    q = deque([start])
    visited[start] = True

    while q:
        u = q.popleft()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

sol()
