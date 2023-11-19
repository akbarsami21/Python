

a=15
b=15
print(a==b)  #== value check kore

a=16
b='16'
print(a==b) #== value check kore

a='16'
b='16'
print(a==b) #== value check kore

a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(a is b) # ekoi objet kina check kore, ekane a,b 2 ta alada object tai
              # eta true na,jodi ekta object er value hoto taile true hot

a=[1,2,3,4,5]
b=a
print(a is b)