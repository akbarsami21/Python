
tuple=("Akbar","Sami",5,3,4,2,7) #tupple is like list with constant value the means tupple is immuitable
print(tuple.index(2))
print(tuple[0:4])

for i in tuple:
    print(i)

#convert tupple to list for add new value
list=list(tuple)
list.append(4)
print(tuple)
print(list)

#merge two tupple
firstTupple=("Akbar","Sami","Sakib","Saikat")
secondTupple=("Bangladesh","India","Nepal")
mergeTupple=firstTupple+secondTupple
print(mergeTupple)

for i in mergeTupple:
    print(i)