
list=["Akbar","Sami","Hello","World",[1,2,3,4,5],True,False]
print(list[0])
print(list[2:6])
print(list[0:7:2])

for i in list:
    if "Hell" in list:
        print("Hello")
        break
    else:
        print("Not Found")
        break

m=[i for i in range(6)]
print(m)
