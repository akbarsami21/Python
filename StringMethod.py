name="Akbar Sami"
fruit='mango'
bird="doel!"
print('Name Length : ',len(name)) #length of string
print(name[0], name[9])           #index 0 element ande index 9 element
print(name[2:4])                  #index 2 to 4
print(name[:-3])                  #0 to len(name)-3
print(name.split())               #space hisab kore list e convert kore

print(name.upper())               #upper case convert
print(name.lower())               #lover case convert
print(name.find("S"))
print(name.index("A"))
print(name.isupper())            #return boolean true or false 
print(fruit.islower())
print(name.capitalize())         #sentece er first letter ke capital kore de
print(fruit.title())             #sentence er sob word er first letter ke capital kore de
print(name.startswith('K'))
print(fruit.endswith('o'))
print(name.replace("Akbar","Mohammed"))
print(bird.rstrip("!"))          #symbol type chracter remove 
print(name.isalnum())
print(bird.isalpha())

name="MOHAMMED SAMI"
print(name.swapcase())
