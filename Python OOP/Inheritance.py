

class A:
    def __init__(self,a,b):
        self.a=a 
        self.b=b

    def sum(self):
        return self.a+self.b

class B(A):
     def __init__(self,a,b):
        self.a=a 
        self.b=b

     def sub(self):
        return self.a-self.b
     
n1=B(5,3)
print(n1.sub())
print(n1.sum())

n2=A(10,20)
print(n2.sum())

