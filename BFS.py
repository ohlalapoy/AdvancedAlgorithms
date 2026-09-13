'''
---- Psudocode ---- อ่านเรียงจากบนลงล่าง จากซ้ายไปขวา ลงไปทีละชั้น 
BFS(start):
    สร้าง Queue
    ใส่ start ลง Queue
    mark start ว่า visited

    while Queue ไม่ว่าง:
        node = เอาตัวแรกออกจาก Queue

        ทำอะไรบางอย่างกับ node

        for neighbor ของ node:
            ถ้ายังไม่เคยเจอ:
                mark ว่า visited
                ใส่ neighbor ลง Queue

BFS has various applications in graph theory and computer science, including:
- Shortest Path Finding
- Cycle Detection
- Connected Components
- Network Routing
'''
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# BFS for single connected component
def bfs(adj):
    V = len(adj)
    visited = [False] * V
    res = []
    
    src = 0
    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        # visit all the unvisited
        # neighbours of current node
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
                
    return res

# BFS for a single connected component
def bfsConnected(adj, src, visited, res):
    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        # visit all the unvisited
        # neighbours of current node
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

# BFS for all components (handles disconnected graphs)
def bfs(adj):
    V = len(adj)
    visited = [False] * V
    res = []

    for i in range(V):
        if not visited[i]:
            bfsConnected(adj, i, visited, res)
    return res