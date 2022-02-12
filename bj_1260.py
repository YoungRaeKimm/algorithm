from audioop import reverse
from collections import deque, defaultdict

def dfs(graph, start_node):
    visited = []
    need_visited = deque()
    
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            if graph.get(start_node) != None:
                need_visited.extend(graph[node])
    print()

def bfs(graph, start_node):
    visited = []
    need_visited = deque()
    
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.popleft()
        
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            if graph.get(start_node) != None:
                need_visited.extend(sorted(graph[node]))

graph = defaultdict()
n, m ,v = map(int, input().split())
for i in range(m):
    start, dest = map(int, input().split())
    if graph.get(start) == None:
        graph[start] = [dest]
    elif len(graph[start]) > 0:
        graph[start].append(dest)
        graph[start].sort(reverse = True)
        
    if graph.get(dest) == None:
        graph[dest] = [start]
    elif len(graph[dest]) > 0:
        graph[dest].append(start)
        graph[dest].sort(reverse = True)
dfs(graph, v)
bfs(graph, v)