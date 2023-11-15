 
print("Hello, Welcome To Simple Calculator")

num1=float(input("Enter First Number : "))
num2=float(input("Enter Second Number: "))

operator=input("Enter Operator (+,-,/,//,%,**) : ")

if(operator=='+'):
    print("Sum is : ",(num1+num2))

elif(operator=='-'):
    print("Sub is : ",(num1-num2))

elif(operator=='*'):
    print("Mul is : ",(num1*num2))

elif(operator=='/'):
    print("Div is : ",(num1/num2))

elif(operator=='*'):
    print("DivP is : ",(num1//num2))

elif(operator=='%'):
    print("Rem is : ",(num1%num2))

elif(operator=='**'):
    print(num1,"Power of ",num2,"is : ",(num1**num2))

else:
    print("You Typed Worng, Please Try Again!!")