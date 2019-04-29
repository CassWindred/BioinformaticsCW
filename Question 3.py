import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def findClosest(matrix):
    closestcoord=[0]*2
    minvalue=None
    sidelen=matrix.shape[0]

    for x in range(1,sidelen):
        for y in range(1,sidelen):
            val=matrix[x][y]
            if x!=y and (minvalue==None or minvalue>val):
                minvalue=val
                closestcoord[0]=x
                closestcoord[1]=y
    return closestcoord




def addnodes(G, node1, node2, parentnode, distance):

    distance=float(distance)
    G.add_node(node1)
    G.add_node(node2)
    G.add_node(parentnode, height=distance/2)
    G.add_edge(node1, parentnode)
    G.add_edge(node2, parentnode)


    #Position the nodes
    if len(node1)==1:
        G.graph["pos"][node1]=(G.graph["nodecount"],1)
        G.graph["nodecount"]+=1
        G.node[node1]["height"]=0

        G.graph["nodelabels"][node1]=node1

    if len(node2)==1:
        G.graph["pos"][node2] = (G.graph["nodecount"], 1)
        G.graph["nodecount"]+=1
        G.node[node2]["height"] = 0

        G.graph["nodelabels"][node2] = node2



    parentxpos=(G.graph["pos"][node1][0]+G.graph["pos"][node2][0])/2 #Get the average x-coord of the child nodes
    G.graph["pos"][parentnode]=(parentxpos,len(parentnode))

    #Find edge weights
    G.graph["edgeweights"][node1,parentnode]=(distance/2)-G.node[node1]["height"]
    G.graph["edgeweights"][node2, parentnode] = (distance / 2) - G.node[node2]["height"]





def WPGMA(filename):
    f = open(filename, "r")
    matrix=[]
    for i in f:
        print(i, end="")
        matrix.append(i.split(" "))
        matrix[-1][-1]=matrix[-1][-1].rstrip('\n') #Remove /n at end
    matrix=np.array(matrix)

    #Create graph with parameters for positioning nodes
    G = nx.Graph(nodecount=0, pos={}, edgeweights={}, nodelabels={})

    print()
    complete=False
    while complete==False:
        sidelen = matrix.shape[0]
        closest=findClosest(matrix)
        xletter=matrix[closest[0]][0] #Find the species in the x axis
        yletter = matrix[0][closest[1]] #Find the species in the y axis
        newname=yletter+xletter #Find the combined name of the species

        newrow=[None]#*sidelen-2
        newrow[0]=newname

        addnodes(G, xletter, yletter, newname, matrix[closest[0]][closest[1]])

        for i in range(1,sidelen):
            if i not in closest:
                newval=(float(matrix[closest[0]][i])+float(matrix[closest[1]][i]))/2 #Find value for new spot
                newrow.append(newval)
        newrow=np.array(newrow)
        #Remove rows and collumns
        matrix = np.delete(matrix, closest[1],0)
        matrix = np.delete(matrix, closest[1], 1)
        matrix = np.delete(matrix, closest[0], 0)
        matrix = np.delete(matrix, closest[0], 1)
        #Add new row and collumn
        matrix = np.vstack([matrix,newrow])

        newrow = np.append(newrow,0.0)



        matrix = np.column_stack([matrix, newrow])
        print(matrix)
        if matrix.shape[0] <=2:
            complete=True

    print("Results:")
    print(str(G))
    nx.draw(G, G.graph["pos"], with_labels=False, font_weight='bold')
    nx.draw_networkx_edge_labels(G, G.graph["pos"], edge_labels=G.graph["edgeweights"])
    nx.draw_networkx_labels(G, G.graph["pos"], labels=G.graph["nodelabels"])
    plt.show()



WPGMA("matrix-wikipedia.txt")