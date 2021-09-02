#More Deeper Understanding on Dictionaries

#Update Method-Concatenation
fruit={"Apple":"I love apple",
       "Orange":"I love to ear orange"}
print(fruit)
veg={"Cabbage":"Every Child's Favourite",
     "Spinach":" Can I have some spinach?"}
frui3=fruit.copy()

print(veg)

veg.update(fruit)
print(veg)
fruit.update(veg)
print(fruit)

print("-------")

#copy Method

fruit_new=fruit.copy()
print(fruit_new)
fruit_new.update(veg)
print("----")
print(fruit_new)
print(frui3)

#All the keys in a dictionary should be unique
