import numpy as np

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
    print(matrix)
    matrix=np.array(matrix)
    print(matrix)



    complete=False
    while complete==False:
        sidelen = matrix.shape[0]
        closest=findClosest(matrix)
        print(closest)
        xletter=matrix[closest[0]][0] #Find the species in the x axis
        yletter = matrix[0][closest[1]] #Find the species in the y axis
        newname=xletter+yletter #Find the combined name of the species
        print(newname)

        newrow=[None]#*sidelen-2
        newrow[0]=newname

        for i in range(1,sidelen):
            if i not in closest:
                newval=(int(matrix[closest[0]][i])+int(matrix[closest[1]][i]))/2 #Find value for new spot
                newrow.append(newval)
                print(newval)
        newrow=np.array(newrow)
        #Remove rows and collumns
        matrix = np.delete(matrix, closest[1],0)
        matrix = np.delete(matrix, closest[1], 1)
        matrix = np.delete(matrix, closest[0], 0)
        matrix = np.delete(matrix, closest[0], 1)
        #Add new row and collumn
        matrix = np.vstack([matrix,newrow])
        print(matrix)
        print(newrow)
        newrow = np.append(newrow,0.0)
        print(newrow)
        newrow = np.flip(newrow)
        print(newrow)
        matrix = np.hstack([matrix, newrow])

        complete=True



WPGMA("matrix1.txt")