
class Employe:
    companyName="Google"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name=name

    def display(self):
        print(f'Name is : {self.name} and Company Name is : {Employe.companyName}')

    @classmethod
    def companyNameChange(self,companyName):
        self.companyName=companyName

e1=Employe()
e1.name="Akbar Sami"
e1.display()

e2=Employe()
e2.name="Mr.x"
e2.companyNameChange("Netflix")
e2.display()

print(Employe.companyName) #change hoye jave karon classmethod diye change kore disi