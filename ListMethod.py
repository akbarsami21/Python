
list=[1,1,5,3,6,2,0]
print("Before Sort : ",list)

list.sort()
print("After Accending Sort  : ",list)

list.sort(reverse=True)
print("After Deccending Sort  : ",list)

list.append(5)
list.append(["Akbar","Sami"])
print("After Append: ",list)

list.reverse()
print("After Reverse : ",list)

list.insert(0,"Python")
print("After Insert Value In 0 Index : ",list)

newList=["Bangladesh","India","Nepal"]
list.extend(newList)
print("After Extend New List In Old List : ",list)

print("1 Value In = ",list.count(1))

anotheList=list.copy()
print("The List Value After Using Clear Mehtod",list.clear())
print(list)

anotheList.append("China")
print(anotheList)

anotheList.pop(5)
print("After Delete The 5 Index Value 3 : ",anotheList)

print("2 Index Value Is : ",anotheList.index(2))

