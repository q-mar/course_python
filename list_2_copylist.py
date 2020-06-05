def add(liste):
    liste.append("apple")

fruits = ["birne", "cherry", "birne", ["birne"]]
new_fruits = fruits[:]
fruits[0] = "Pineapalle"
#print(id(p[0]))
#print(id(p[1]))
#print(id(p[2]))
#print(id(p[3][0]))

print(fruits)
print(new_fruits)