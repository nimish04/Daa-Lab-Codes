import math
class Graph :
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[]

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def bellman(self,source):
        dist=[math.inf]*self.v
        dist[source]=0

        for i in range(self.v-1):
            for u,v,w in self.graph:
                if dist[u]+w<dist[v]:
                    dist[v]=w+dist[u]

        print(dist)
        print(self.graph)

        for u,v,w in self.graph:
            if dist[u]+w<dist[v]:
                print("Negative cycle")
                return
g=Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)
	 
#Print the solution
g.bellman(0)
        
