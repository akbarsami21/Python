
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def mul(self):
        return self.a*self.b
    
    def div(self):
        return self.a/self.b
    
class B(A):
    pass

class C(A):
    pass

class D(A):
    def __init__(self, a, b):
        super().__init__(a, b)
   

d=D(7,8)
print(d.add())
print(d.sub())
print(d.mul())
print(d.div())