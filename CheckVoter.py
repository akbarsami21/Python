
age=int(input("Enter Your Age : "))

if(age<18 and age>=0):
    print("Not Voter")
    
elif(age>=18):
    print("Voter")
else:
    print("Something Went Wrong. Try Agian!!")
