
class Employee:
    def __init__(self,name,age):
        self.name=name 
        self.age=age

    @classmethod
    def fromString(cls,string):
        return cls(string.split(",")[0],int(string.split(",")[1]))
    
#Class Methods as Alternative Constructors
string="Akbar Sami,21"
e1=Employee.fromString(string)
print(e1.name,e1.age)

        