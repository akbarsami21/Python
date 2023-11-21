
class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

        
    def __add__(self,other):
        return f'{self.real+ other.real} + {self.imaginary+other.imaginary}i'
    
c1=ComplexNumber(1,2)
c2=ComplexNumber(3,4)
print(c1+c2)        