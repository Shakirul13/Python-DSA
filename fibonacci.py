def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
def main():
    n=int(input("Enter the nth number :"))
    ans=fib(n)
    print(ans)
main()
