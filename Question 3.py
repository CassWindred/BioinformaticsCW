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




def WPGMA(filename):
    f = open(filename, "r")
    matrix=[]
    for i in f:
        print(i, end="")
        matrix.append(i.split(" "))
        matrix[-1][-1]=matrix[-1][-1].rstrip('\n') #Remove /n at end
    matrix=np.array(matrix)

    G = nx.Graph()

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

        G.add_node(xletter)
        G.add_node(yletter)
        G.add_node(newname)
        G.add_edge(xletter, newname)
        G.add_edge(yletter,newname)

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
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()



WPGMA("matrix2(1).txt")