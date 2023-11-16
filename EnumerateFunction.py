
countries=["Afganistan","India","Srilanka","Bangladesh","Australia"]

# for i in range(len(country)):
#     print(i,", ",country[i])

# index=0
# for country in countries:
#     print(f'{index} {country}')
#     index +=1

#using enumerate fucntion

for index, country in enumerate(countries):
    print(index," ",country)
    if(index==3):
        print(f"    {countries[index]}This is my country")

# for index, country in enumerate(countries,start=1):
#     print(index," ",country)
#     if(index==3):
#         print(f"    {countries[index]}This is my country")