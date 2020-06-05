fruits = ["apple", "banana", "cherry"]
frutti = fruits

fruit = fruits[0]
print(fruits)

print("Länge der Liste: ", len(fruits))

# Datentyp von List-Element an Index 0
print(type(fruit))

# index von Wert zurückgeben lassen
print(fruits.index("banana"))

fruits[0] = "Strawberry"
print(fruits)

# neues Element einfügen auf Index
fruits.insert(1, "lemon")
print(fruits)
print(fruits.index("banana"))

# Element an Liste anhängen
fruits.append("pineapple")
print(fruits)

# Mehrere Elemente an Liste anhängen
# fruits = fruits + ["coconut", "strawberry", "apple"]
fruits += ["coconut", "strawberry", "apple", "apple"]

# alternative Möglichkeit
fruits.extend(["Orange", "Quitte"])
print(fruits)

if "apple" in fruits:
    print("jo, der Apfel ist hier drin")
    fruits.remove("apple")
    fruits.remove("apple")

print(fruits)
s = fruits.pop()
print(s)
print(fruits)

# fruits.clear()
# print(fruits)

# Listen Element löschen
# del fruits[0]

# Liste aus dem Speicher entfernen
# del fruits
print(fruits)
print(frutti)