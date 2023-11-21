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

b=B()
b.dislay()
B.hello()