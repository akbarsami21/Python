class A:
    name="sami"
    age=21
    university="premier university"

    def dislay(self):
        print(f'{self.name},{self.age},{self.university}')
class B(A):
    @staticmethod
    def hello():
        print("hello world")

class C(B):
    @staticmethod
    def print():
        print("hello world from c class")

c=C()
c.print()
c.dislay()
print(type(C))
