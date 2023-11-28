
class Cricketer:
    def __init__(self,name,totalRun:int,totalCentury:int) :
        self.name=name
        self.totalRun=totalRun
        self.totalCentury=totalCentury

    def info(self):
        print(f'{self.name} & {self.totalCentury} & {self.totalRun}')

print(dir(Cricketer))

c=Cricketer("Tamim",15000,25)
print(c.__dict__)

print(help(Cricketer)) #details about class 
        