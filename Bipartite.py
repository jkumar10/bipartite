from ast import literal_eval as createTuple
import itertools

# Reading File
def readFile():
    edges = []
    with open("bipartite2.txt","r") as fp:
        for line in fp:
            line = line.split()
            for l in line:
                edges.append(createTuple(l))
        n=edges.pop(0)
        unique=set(itertools.chain.from_iterable(edges))
    createAdj(n,unique,edges)


# Creating adjacency list
def createAdj(n,unique,edges):
    #print "Number of vertices: {}".format(n)
    #print "Graph: {}".format(edges)
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

    #print "Adjacency List: {}".format(adj)
    checkBipartite(n,unique,edges,adj)



# Checking if graph is Bipartite or not
def checkBipartite(n,unique,edges,adj):
    Q=[]
    color={}
    vertices=list(unique)
    flag=0
    blue=[]
    red=[]


    # Initialization
    # WHITE color denotes all unexplored vertices
    # BLUE color denotes vertices in first partition
    # RED color denotes vertices in second partition
    for vertex in vertices:
        if vertex not in color:
            color[vertex]="WHITE"

    source=vertices[0]
    color[source]="BLUE"
    Q.append(source)
    while len(Q)!=0:
        u=Q.pop()
        if u in adj[u]:
            flag=1
            break

        for v in vertices:
            if v in adj[u] and color[v]=="WHITE":
                if color[u]=="BLUE":
                    color[v]="RED"
                    blue.append(u) if u not in blue else 0
                    red.append(v) if v not in red else 0

                elif color[u]=="RED":
                    color[v]="BLUE"
                    red.append(u) if u not in red else 0
                    blue.append(v) if v not in blue else 0
                Q.append(v)

            elif v in adj[u] and color[v]==color[u]:
                flag=1
                break


    result(flag,red,blue)

def result(flag,red,blue):
    if flag==1:
        print "Graph is not Bipartite"
    elif flag==0:
        print "Graph is Bipartite"
        print "Two partitions are:"
        print "First partition: {}".format(red)
        print "Second partition: {}".format(blue)



readFile()
