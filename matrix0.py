matrix=[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]

#Brute Force
def markInfinity(matrix,row,cols):
    r=len(matrix)
    c=len(matrix[0])
    for i in range(0,r):
        if matrix[i][cols]!=0:
            matrix[i][cols]=float("inf")
    for j in range (0,c):
        if matrix[row][j]!=0:
            matrix[row][j]=float("inf")

def setZeroes(matrix):
    r=len(matrix)
    c=len(matrix[0])
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j]==0:
                markInfinity(matrix,i,j)
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j]==float("inf"):
                matrix[i][j]=0
    return matrix
print(setZeroes(matrix))