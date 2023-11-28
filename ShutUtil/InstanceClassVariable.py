
class Student:
    
    dept="CSE"
    noOfStudent=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.noOfStudent+=1

    def show(self):
        return print(f'Name : {self.name}, Age : {self.age}, Department : {self.dept}, Number Of Student : {self.noOfStudent}')
        # return print(f'Name : {self.name}, Age : {self.age}, Department : {Student.dept}, Number Of Student : {Student.noOfStudent}')

s=Student("Akbar Sami",21)
s.show()

s1=Student("Sakib Chowdury",22)
s1.show()

s3=Student("Samy",23)
s3.dept="EEE"
s3.show()
