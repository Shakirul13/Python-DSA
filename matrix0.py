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

matrix1=[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]

#Optimal
def optimal(matrix1):
    r=len(matrix1)
    c=len(matrix1[0])
    row_track=[0 for _ in range(r)]
    col_track=[0 for _ in range(c)]
    for i in range(0,r):
        for j in range(0,c):
            if matrix1[i][j]==0:
                row_track[i]=-1
                col_track[j]=-1
    for i in range (0,r):
        for j in range(0,c):
            if row_track[i]==-1 or col_track[j]==-1:
                matrix1[i][j]=0
    return matrix1
print(optimal(matrix1))