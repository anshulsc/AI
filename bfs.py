#------BFS Psudocode ------

'''
create a queue Q 
mark v as visited and put v into Q 
while Q is non-empty 
    remove the head u of Q 
    mark and enqueue all (unvisited) neighbours of u
'''


# Graph representation using adjacency list
# Path: bfs.py
#------BFS Psudocode ------

class Graph:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        self.adjancey_list = {node: [] for node in range(num_of_nodes)}

    def add_edge(self, u, v):
        self.adjancey_list[u].append(v)
        self.adjancey_list[v].append(u)

    def print_graph(self):
        for node in range(self.num_of_nodes):
            print(node, "->", self.adjancey_list[node])

def bfs(graph,start):
    visited = [False]*graph.num_of_nodes
    queue = []
    queue.append(start)
    visited[start] = True
    while queue:
        start = queue.pop(0)
        print(start,end=" ")
        for i in graph.adjancey_list[start]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


def BFS_MIT(start,graph):
    level = {start: 0}
    parent = {start: None}
    i = 1
    frontier = [start]
    while frontier:
        next = []
        for u in frontier:
            for v in graph.adjancey_list[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    return level, parent


def print_bfs_mit(start, graph):
    level, parent = BFS_MIT(start, graph)
    max = 0
    for i in level:
        if  max < level[i]:
            max = level[i]

    for i in range(max+1):
        print("Level",i,":",end=" ")
        for j in level:
            if level[j] == i:
                print(j,end=" ")
        print()

# Driver code
from collections import deque
def BFS_JUG(a, b, target):
 
    level = {}
    isSolvable = False
    path = []
 
    frontier = deque()
    parent = {}
    frontier.append((0, 0))
    parent[(0, 0)] = (-1, -1)
  
    i = 0
    while len(frontier) > 0:

        u = frontier.popleft()
 
        if (u[0], u[1]) in level:
            continue
 
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue

        if [u[0], u[1]] not in path:
            path.append([u[0], u[1]])
            level[(u[0], u[1])] = i
 
        if u[0] == target or u[1] == target:
            isSolvable = True
 
            if u[0] == target:
                if u[1] != 0:
                    path.append([u[0], 0])
                    if (u[0], 0) not in parent.keys():
                        parent[(u[0], 0)] = [u[0], u[1]]
            else:
                if u[0] != 0:
                    path.append([0, u[1]])
                    parent[(0, u[1])] = [u[0], u[1]]
            return path,level,parent
        if (a,u[1]) not in parent.keys():
            parent[(a, u[1])] = [u[0], u[1]]
        if (u[0],b) not in parent.keys():    
            parent[(u[0], b)] = [u[0], u[1]]
        frontier.append([a, u[1]]) # Fill Jug1
        frontier.append([u[0], b])  # Fill Jug2
         
 
        for ap in range(max(a, b) + 1):
 
            c = u[0] + ap
            d = u[1] - ap
 
            if c == a or (d == 0 and d >= 0):
                frontier.append([c, d])
                if ((c, d) not in parent.keys()):
                    parent[(c, d)] = [u[0], u[1]]
 
            c = u[0] - ap
            d = u[1] + ap
 
            if (c == 0 and c >= 0) or d == b:
                frontier.append([c, d])
                if ((c, d) not in parent.keys()):
                    parent[(c, d)] = [u[0], u[1]]
        i += 1
 
    if not isSolvable:
        return None,None,None



if __name__ == "__main__":
    V = 8

    # Create graph and edges
    graph = Graph(V)
    # graph.add_edge(3, 4)
    # graph.add_edge(3, 5)
    # graph.add_edge(4, 6)
    # graph.add_edge(4, 7)
    # graph.add_edge(5, 1)
    # graph.print_graph()
    # print_bfs_mit(7, graph)

    path,level,parent = BFS_JUG(4,3,2)
    if path == None:
        print("No solution")
    else:
        li = []
        val = path[-1]
        while val != (-1,-1):
            li.append(val)
            val = tuple(parent[tuple(val)])

        print("Path from initial state to solution state ::")
        for i in li[::-1]:
            print(i,"->",end=" ")
        print("End")