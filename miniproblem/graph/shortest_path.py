# graph/shortest_path.py

import sys
import copy


class Dijkstra():
    """
    Compute Dijkstra's algorithm from all sources taking an adjacency matrix
    as input and writing all steps in assets/exit.txt
    """
    def __init__(self, graph):
        file = open("assets/exit.txt","r+")
        file.truncate(0)
        file.close()
        self.graph = graph
        self.V = len(graph) #number of vertices

    def print_solution(self, dist): 
        with open('assets/exit.txt', 'a') as f:
            f.write("Vertex \t Distance from Source \n")
            for node in range(1, self.V + 1): 
                f.write(str(node) + "\t" + str(dist[node - 1]) + "\n")
            f.write("\n")
            f.close()

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
            self.print_solution(dist)

    @staticmethod
    def run(graph):
        path = Dijkstra(graph)
        path.dijkstra(0)


class BellmanFord():
    """
    Compute Bellman-Ford's algorithm from all sources taking an adjacency matrix
    as input and writing all steps in assets/exit.txt
    """
    def __init__(self, graph):
        file = open("assets/exit.txt","r+")
        file.truncate(0)
        file.close()
        self.V = len(graph)
        self.transform_matrix(graph)
        self.E = len(self.graph)

    def transform_matrix(self, graph):
        self.graph = []
        for u in range(self.V):
            for v in range(self.V):
                if graph[u][v] != 0:
                    self.graph.append((u, v, graph[u][v]))

    def bellman_ford(self, src):
        dis = [sys.maxsize] * self.V
        dis[src] = 0
        for i in range(self.V - 1): 
            for j in range(self.E): 
                if dis[self.graph[j][0]] + self.graph[j][2] < dis[self.graph[j][1]]: 
                    dis[self.graph[j][1]] = dis[self.graph[j][0]] + self.graph[j][2]
        
        for i in range(self.E): 
            x = self.graph[i][0] 
            y = self.graph[i][1] 
            weight = self.graph[i][2] 
            if dis[x] != sys.maxsize and dis[x] + weight < dis[y]: 
                print("Graph contains negative weight cycle.") 
     
        with open("assets/exit.txt", "a") as f:
            f.write("Vertex Distance from Source: \n")
            for i in range(self.V): 
                f.write(str(i + 1) + "\t" + str(dis[i]) + "\n")
            f.close()

    @staticmethod
    def run(graph):
        path = BellmanFord(graph)
        path.bellman_ford(0)


class FloydWarshall():
    """
    Compute Floy-Warshall's algorithm from all sources taking an adjacency matrix
    as input and writing the final matrix in an exit file given as input.
    """
    def __init__(self, graph, file):
        file = open(file,"r+")
        file.truncate(0)
        file.close()
        self.inf = sys.maxsize
        self.V = len(graph)
        self.transform_matrix(graph)

    def transform_matrix(self, graph):
        self.graph = graph
        for u in range(self.V):
            for v in range(self.V):
                self.graph[u][v] = self.inf if graph[u][v] == 0 else graph[u][v]

    def floyd_warshall(self, file):
        self.dist = list(map(lambda i : list(map(lambda j : j, i)), self.graph))
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])
            self.print_solution(file)
 
    def print_solution(self, file):
        temp = copy.deepcopy(self.dist)
        for i in range(len(temp)):
            for j in range(len(temp)):
                if i != j:
                    temp[i][j] = "INF" if temp[i][j] == sys.maxsize else temp[i][j]
                else:
                    temp[i][j] = 0
        with open(file, "w") as f:
            for i in range(len(temp)):
                f.write(str(i + 1) + "\t" + str(temp[i]) + "\n")
            f.close()

    @staticmethod
    def run(graph, file):
        path = FloydWarshall(graph, file)
        path.floyd_warshall(file)
