
try:
    num1=int(input('Enter First  Number : '))
    num2=int(input('Enter Second Number : '))
    print(f'Division Is : {num1/num2}')
except Exception as e:
    print('The Error Is : ',e)

finally:
    print('Inside Of Finally Block All line Will Always Executed')

# def add(a,b):
#     try:
#         return print(a+b)
#     except Exception as e:
#         print(e)
#         return 0
#     finally:
#        print("Hello World")

# add(5,"sami")