#function or variable er age _ dile protected,__ dile private
#protected access korte parbo inheritance are te
#private only in same class

class A:
    def _hello(self):
        print('hello world')
        a=A()   
        a.__Hi() 
    def __Hi(self):
        print('hi everyone')


# class B:
#     def welcome(slef):
#         print("welcome to bangladesh")
#         # a1=A()
#         # a1.hello() #error asbe karon eti protected and inherit korinai

class B(A):
    def welcome(self):
        print('welcome to bangaldesh')
        a1=A()
        a1._hello() #error asbe na karon eti inherit korsi
        # a1.__Hi() #error asbe karon eti private

    
b1=B()
b1.welcome()

class C:
    def __init__(self):
        self.__name="Akbar Sami"
c=C()
print(c._C__name)


