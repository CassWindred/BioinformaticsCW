#!/usr/bin/python
import time
import sys
#SCORE CONSTANTS
matchA=4
matchC=3
matchG=2
matchT=1
mismatch=-3
indel=-2

# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix
def initTable(firstseq, secondseq):
    table=[]*(len(firstseq)+2)
    for i in table:
        table[i]=[""]*(len(secondseq)+2)
        if i>=2:
            table[i][0]=firstseq[i-2]
    for i in table[0]:
        if i>=2:
            table[0][i]=secondseq[i-2]
    return table

def checkint(inp): #returns inp if integer, otherwise returns -1
    if type(inp)==int:
        return inp
    else:
        return -1

def matchscore(x,y, scoretable):
    xval=scoretable[x][0]
    yval=scoretable[0][y]
    if xval==yval:
        if xval="A":
            return matchA
        if xval="C":
            return matchC
        if xval="G":
            return matchG
        if xval="T":
            return matchT
    else:
        return mismatch

def populateTables(scoretable,backtrack):
    xlen=len(scoretable) #Length of table in x axis
    ylen=len(scoretable[0]) #Length of table in y axis
    scoretable[1][1]=0
    for x in range(1,xlen):
        for y in range(1,ylen):
            if not (x==1 and y==1):
                top=scoretable[x][y-1]+indel
                left=scoretable[x-1][y]+indel
                diag=scoretable[x-1][y-1]+matchscore(x,y,scoretable)
                scoretable[x][y]=max(top,left,diag, key=checkint) #OPTIMISING: MAYBE REMOVE KEY AND CHECK IN IF STATEMENTS BELOW
                if scoretable[x][y]==top:
                    backtrack[x][y].append("U")
                if scoretable[x][y]==left:
                    backtrack[x][y].append("L")
                if scoretable[x][y]==diag:
                    backtrack[x][y].append("D")

# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
scoretable=initTable(seq1,seq2)
backtrack=scoretable.copy()


# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 



#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

