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

# ----------------------------- BFS from a Given Source in an Undirected Graph
from collections import deque

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
    
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
    
    
if __name__ == "__main__":
    V = 5
    adj = []
    
    # creating adjacency list
    for i in range(V):
        adj.append([])
        
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 0)
    addEdge(adj, 2, 0)
    addEdge(adj, 2, 3)
    addEdge(adj, 2, 4)

    res = bfs(adj)

    for node in res:
        print(node, end=" ")


# ----------------------------- BFS of a Disconnected Undirected Grap
from collections import deque

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


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
  
  
if __name__ == "__main__":
    V = 6
    adj = []
    
    # creating adjacency list
    for i in range(V):
        adj.append([])
        
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 0)
    addEdge(adj, 0, 3)
    addEdge(adj, 4, 5)

    res = bfs(adj)

    for node in res:
        print(node, end=" ")