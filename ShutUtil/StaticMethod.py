
class Math:

    def addTwoNum(self,a,b):
        return a+b
    
    @staticmethod
    def addThreeNum(a,b,c):
        return a+b+c
    
m1=Math()
print(m1.addTwoNum(4,6))
print(Math.addThreeNum(5,7,8))

