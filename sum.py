#using functional recursion
n=int(input("Enter the number:"))
def func(n):
    if n==1:
        return 1
    return n + func(n-1)
print(func(n))
    
#using parameterized recursion
# def func(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i,i+1,n) #sum+=1 cannot be written within a function

func(n)
#func(0,1,n) #function call