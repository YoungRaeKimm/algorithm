import sys
import heapq

def dijkstra(adj, num, s, e):
    heap = []
    heapq.heappush(heap, [0, s])
    dist = [sys.maxsize] * (num + 1)
    dist[s] = 0
    
    while heap:
        c, n = heapq.heappop(heap)
        if dist[n] < c :
            continue
        for node, cost in adj[n]:
            if c + cost < dist[node]:
                dist[node] = c + cost
                heapq.heappush(heap, [cost + c, node])
    return dist[e]

def solution(n, s, a, b, fares):
    adj = [[] for _ in range(n + 1)]
    for x,y,c in fares:
        adj[x].append([y,c])
        adj[y].append([x,c])
    
    ans = dijkstra(adj, n, s, a) + dijkstra(adj, n, s, b)
    for i in range(1, n+1):
        if s != i:
            ans = min(ans, dijkstra(adj, n, s, i) + dijkstra(adj, n, i, a) + dijkstra(adj, n, i, b))
    return ans
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))