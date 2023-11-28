
class Calculation:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def mul(self):
        return self.a*self.b
    
    def div(self):
        return self.a/self.b
    
class H:
    def hello(self):
        print("hello world from class H")

class C(Calculation,A,H):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def display(self):
        print("hello world form class C")

c=C(5,4)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())
c.display()
c.hello()


    
        
        
            


