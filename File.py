
# # file create and write
# f=open("MyFile-1.txt",'w')
# f.write("hello world, my name is akbar sami.")
# f.close()


#file read
f=open("MyFile-1.txt",'r')
read=f.read()
print(read)
f.close()

#append not overright previous text
# f=open("MyFile-1.txt",'a')
# f.write("""Python is a high-level, general-purpose programming language.
# Its design philosophy emphasizes code readability with the use of significant indentation.
# Python is dynamically typed and garbage-collected. It supports multiple programming paradigms,
# including structured, object-oriented and function""")
# f.close()

#with keyword automatic file close kroe dibe
# with open("MyFile-1.txt",'a') as f:
#     f.write("Python is My Favourite Programming language.")