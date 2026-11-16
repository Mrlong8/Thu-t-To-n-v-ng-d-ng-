import heapq

n, m = map(int, input().split())
adj = [[] for i in range(n + 1)]

for i in range(m):
    u,v,w = map(int,input().split())

    adj[u].append((v,w))
    adj[v].append((u,w))

INF = float('inf')
dist = [INF] * (n + 1)
dist[1] = 0

hp = [(0,1)]
while len(hp) > 0:
    d, u = heapq.heappop(hp)
    if d >  dist[u]: continue
    if u == n:
        break
    for v,w in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] =dist[u] + w
            heapq.heappush(hp,(dist[v],v))

if dist[n] == INF:
    print(-1)
else:
    print(dist[n])
