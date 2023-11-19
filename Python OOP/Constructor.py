

class Student:
    def __init__(self,name,id,age,semester,result):
        self.name=name
        self.id=id
        self.age=age
        self.semester=semester
        self.result=result

    def display(self):
        print("My Name is  : ",self.name)
        print("ID Numher is: ",str(self.id))
        print("Age         : ",str(self.age))
        print("Semstere    : ",self.semester)
        print("Result      : ",str(self.result))

sami=Student("Akbar Sami",2253,21,"3rd",3.81)
sami.display()

print("******************************")
sakib=Student("Sakib Chowdury",2241,21,"3rd",3.75)
sakib.display()
        
        