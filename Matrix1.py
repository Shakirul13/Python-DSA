nums=[[5,6,9],[-1,3,10],[2,4,8]]
rows=len(nums)
cols=len(nums[0])
#Upper triangle of matrix
for i in range(0,rows):
    for j in range(0,cols):
        if j>=i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()     
   
print()
#Lower Triangle of matrix
for i in range(0,rows):
    for j in range(0,cols):
        if i>=j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

print()
#Diagonal of the matrix
for i in range(0,rows):
    for j in range(0,cols):
        if i==j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

print()
#reverse diagonal
for i in range(0, rows):
    for j in range(0,cols):
        if i+j==rows-1:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()