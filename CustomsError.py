
num=int(input('Enter Number Between 1 to 5 : '))

if(num<=0 or num>5):
    raise ValueError("Value Should Be Between 1 to 5 ")
else:
    print(f'You Enter {num}')