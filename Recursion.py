
#fuction er bitor same fuction call korai holo recursion
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter Number : "))
print(f"The Factorial Of {n} Is = ",fact(n))
