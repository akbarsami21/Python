
class Library:
    def __init__(self):
        self.books=["Bangla","Arabic","English","Sciecne","ICT"]
    
    @property
    def bname(self):
        return self._bookName
    @bname.setter
    def bname(self,bookname):
        self._bookName=bookname

l=Library()
l.bname="Physics"
print(l.bname)
for i in l.books:
    print(i)