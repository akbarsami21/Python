
import time as t

def whileLoop():
    i =1
    while i<501:              
        print(i)
        i+=1

def forLoop():
    for i in range(1,501):
        print(i)

t1=t.time()
whileLoop()
t2=t.time()


t3=t.time()
forLoop()
t4=t.time()
print("while loop time = ",t2-t1)
print("for loop time   = ",t4-t3)

formatedTime=t.strftime("%H:%M:%S",t.localtime())
print("My Local Time : ",formatedTime)

t.sleep(5)
print("print after 5 second")