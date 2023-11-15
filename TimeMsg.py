
import time

name=input("Hey, Whats Your Name = ")
LocalTime=time.strftime("%H:%M:%S")
hours=int(time.strftime("%H"))
print("Now Time Is: ",LocalTime)

if(5<=hours<12):
    print("Good Morning,",name)

elif(12<=hours<18):
    print("Good Afternoon,",name)

else:
    print("Good Evening,",name)