from ast import literal_eval as createTuple
import itertools

# Reading File
def readFile():
    edges = []
    with open("bipartite.txt","r") as fp:
        for line in fp:
            line = line.split()
            for l in line:
                edges.append(createTuple(l))
        n=edges.pop(0)
        unique=set(itertools.chain.from_iterable(edges))
    createAdj(n,unique,edges)


# Creating adjacency list
def createAdj(n,unique,edges):
    print "Number of vertices: {}".format(n)
    print "Graph: {}".format(edges)
    adj={}
    adj.fromkeys(unique)
    for key in unique:
        temp = []
        for edge in edges:
            if key==edge[0]:
                temp.append(edge[1])
            if key == edge[1]:
                temp.append(edge[0])
        adj[key]=temp

    print "Adjacency List: {}".format(adj)
    result=checkBipartite(n,unique,edges,adj)
    print result


# Checking if graph is Bipartite or not
def checkBipartite(n,unique,edges,adj):
    Q=[]
    color={}
    vertices=list(unique)
    flag=0


    # Initializion
    # WHITE color denotes all unexplored vertices
    # BLUE color denotes vertices in first disjoint set
    # RED color denotes vertices in second disjoint set
    for vertex in vertices:
        if vertex not in color:
            color[vertex]="WHITE"

    source=vertices[0]
    color[source]="BLUE"
    Q.append(source)
    while Q:
        u=Q.pop()
        if u in adj[u]:
            return False

        for v in vertices:
            if v in adj[u] and color[v]=="WHITE":
                if color[u]=="BLUE":
                    color[v]="RED"
                elif color[u]=="RED":
                    color[v]="BLUE"
                Q.append(v)

            elif v in adj[u] and color[v]==color[u]:
                return False

    return True






readFile()
