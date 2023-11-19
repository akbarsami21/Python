
#file read by line by line
f=open('MyFile-1.txt','r')

while True:
    line=f.readline()
    if not line:
        break
    print(line)


# list=["My Name is Akbar Sami\n","I am 21 years old\n","I live in Chittagong",]
# f=open('MyFile-2.txt','w')
# f.writelines(list)
# f.close()


# f=open('MyFile-2.txt','a')
# list=["20","40","60"]
# for i in list:
#     f.write(i+"\n")
