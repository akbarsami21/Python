
num=input('Enter Number : ')
print(f'The Multiplication Table Of {num} Is : ')

try:
    for i in range(1,11):
        print(f'{int(num)} X {i} = {int(num)*i}')
except Exception as e:
    print(f'The Error Is : {e}')