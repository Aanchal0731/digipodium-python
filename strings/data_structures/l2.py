#getting list slices

l = [10,'A',30,'B',50,'C',70,'D',90,100]
slice1 = l[4:-1]
print(slice1)

#append function

fruits = []
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Guava")
fruits.append("Cherry")
print(fruits)

#Insert function

fruits = ['Apple','banana','Cherry']
fruits.insert(3,"orange")
fruits.append("Mango")
print(fruits)

#.......

noble_metals = ['gold','silver','platinum']
noble_metals.append(noble_metals)

noble_metals.extend(noble_metals) #add multiple elements to the end of the list
print(noble_metals)

#Extend function

fruits = ['apple','Banana','cherry','Guava']
dry_fruits = ['Almond','cashew','walnut']
fruits.extend(dry_fruits)
print(fruits)
