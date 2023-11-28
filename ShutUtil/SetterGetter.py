
# class Employe:
#     # def __init__(self,name,age,salary):
#     #     self.name=name
#     #     self.age=age
#     #     self.salary=salary



#     def getName(self):
#         return self.name
    
#     def setName(self,name):
#         self.name=name

# emp=Employe()
# emp.setName("Akbar Sami")
# print(emp.getName())
    
class Person:

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,n):
        self._name=n
    

p=Person()
p.name="sami"
print(p.name)
            

        