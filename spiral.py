matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def spiral(matrix):
    if not matrix:
        return []
    result=[]
    top,left=0,0
    bottom,right=len(matrix)-1,len(matrix[0])-1
    while top<=bottom and left<=right:
        #traversing from left to right
            for i in range(top,right+1):
                result.append(matrix[top][i])
            top+=1

        #traversing from top to bottom
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1

        #traversing from right to left
            if top<=bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom-=1

        #traversing from bottom to top
            if left<=right:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
    return result
print(spiral(matrix1))
print(spiral(matrix2))