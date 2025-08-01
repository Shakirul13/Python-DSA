#By converting the integer to a string, we can iterate over each digit.
#  n=5634
#  for i in str(n):
#   print(i)

def extract_digits(n):

 while n>0:
    digit=n%10
    print(digit)
    n=n//10

def main():
  n=int(input("Enter a number:"))
  extract_digits(n)
main()

#Another approach is by using range().Prints integers in right order
# n=5634
# for i in range(len(str(n))):
#     print(str(n)[i])
