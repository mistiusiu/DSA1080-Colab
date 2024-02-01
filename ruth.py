#Creating a list
fruit=["apple","mango","avocado","kiwi","pawpaw"]

#Adding another fruit to the end
fruit.append("grape")

#Replacing the second fruit 
fruit[1]="Banana"

#Removing the last fruit
fruit.remove("grape")

print(fruit)

#creating a tuple
colors=("red","blue","pink","black","purple")

#changing the second color
try:
	colors[1] = "Green"
except TypeError as e:
	print(e)
print(colors)

#converting the tuple into a list
y=list(colors)
y[0]="silver"
colors=tuple(y)

print(colors)

#list slicing
fruits_list=[fruit[0],fruit[-1]]
fruit_slice=[fruit[1:-1:2]]
print(fruits_list)
print(fruit_slice)

#combining lists and tuples
combined=fruit + y
print(combined)

print(combined[1:-1:3])
