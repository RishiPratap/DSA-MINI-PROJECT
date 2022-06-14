# Prim's Algorithm in Python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image  

INF = 9999999
final_sum=0

# number of vertices in graph
V=6
# create a 2d array of size 5x5
# for adjacency matrix to represent graph

filename = 'data.txt'

plt.title('Minimum Spanning Tree for given Graph')

data = np.loadtxt(filename, delimiter=',',dtype=int)
print("FOLLOWING DATA SHOWS WEIGHT BETWEEN EDGES")
print(data)
G = data
# Defining a Class
class GraphVisualization:

	def __init__(self):
		# visual is a list which stores all
		# the set of edges that constitutes a
		# graph
		self.visual = []
        
	# addEdge function inputs the vertices of an
	# edge and appends it to the visual list
	def addEdge(self, a, b):
		temp = [a, b]
		self.visual.append(temp)
		
	# In visualize function G is an object of
	# class Graph given by networkx G.add_edges_from(visual)
	# creates a graph with a given list
	# nx.draw_networkx(G) - plots the graph
	# plt.show() - displays the graph
	def visualize(self):
		H = nx.Graph()
		H.add_edges_from(self.visual)
		nx.draw_networkx(H)
		plt.show() 
        

# Driver code
H = GraphVisualization()
# create a array to track selected vertex
# selected will become true otherwise false



i=0
selected = []
while(i<V):
    j=0
    selected.append(j)
    i = i+1

# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
selected[0] = True
# print for edge and weight
print("Edge : Weight")
while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    final_sum = final_sum + G[x][y]
    H.addEdge(x, y)
    selected[y] = True
    no_edge += 1
H.visualize()
print("The minimum cost to lay path is, ",final_sum)