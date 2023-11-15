
def isGreater(a,b):
    if(a<b):
        print(b ," is greater")
    else:
        print(a,' is grater')

def isLesser(a,b):
    if(a<b):
        print(a ," is lesser")
    else:
        print(b,' is lesser')

num1=int(input("Enter First  Number: "))
num2=int(input("Enter Second Number: "))
isGreater(num1,num2)
isLesser(num1,num2)