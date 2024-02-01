#list
fruits=["apple","mango","avocado","kiwi","pawpaw"]

#adding grape to the list
fruits.append("grape")
print(fruits)

#replacing "mango" with "banana"
fruits[1]= "banana"
print(fruits)
#remove grape from the list
fruits.remove("grape")
print(fruits)


colours = ("red","blue","purple","pink")

try:
    colours.insert(1,"green")
except AttributeError as e:
    print(e)

print(colours)

#QUESTION 2
thistuple = ("red","black","pink","purple")
y = list(thistuple)
y.append("siver")
thistuple = tuple(y)
print(thistuple)

#QUESTION 3
fruits = ["apple","mango","avocado","kiwi","pawpaw"]
print(fruits[0],fruits[-1])

fruits = ["apple","mango","avocado","kiwi","pawpaw"]
s = fruits[::2]
print(s)

#QUESTION 4
fruits = ["apple", "banana", "orange"]
colors = ("red", "green", "blue")

# Combine the 'fruits' list and the 'colors' tuple into a new list named 'combined'
combined = fruits + list(colors)







