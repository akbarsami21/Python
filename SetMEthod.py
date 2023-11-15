
Set={5,10,15,20}
Set.add(25)
print(Set)

s1={1,2,3,4,5,6}
s2={2,4,6,8,9}
s1.update(s2) #s2 er je value gulu s1 ei nai ogulu s1 er valur sathe print korbe
print(s1)
print(s1.union(s2))
print(s1.intersection(s2))

name1={"apple","banana","orrange","guava"}
name2={"Strawberry","sami","orrange","guava"}
print(name1.symmetric_difference(name2)) #mane dui ti set er modde je value gulu common na ogului print hobe

a={4,5,2,3,1}
a.remove(2)
print(a)