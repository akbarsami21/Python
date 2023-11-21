
class Person:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location

    def hello(self):
        print('hello world')

class Student(Person):
    def __init__(self, name, age:int, location,cgpa:float,id:int):
        super().__init__(name, age, location)
        self.cgpa=cgpa
        self.id=id
        
    def info(self):
        print(f'{self.name},{self.age},{self.location},{self.cgpa},{self.id}')
        super().hello()

p=Student("Akbar Sami",21,"Hathazari",3.81,2253)
p.info()





        