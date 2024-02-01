list = ["apple","mango","kiwi","pawpaw","avocado"]

list.append("grape")
print(list)

list[1] = "Banana"
print(list)

list.remove("grape")
print(list)

colors=("red","blue","pink","black","purple")

try:
	colors.replace("blue","Green")
except AttributeError or TypeError as e:
	print(e)
	
print(colors)

list= ["apple","mango","kiwi","pawpaw","avocado"]
print(list[1:5:2])

fruitslist = ["apple","mango","kiwi","pawpaw","avocado"]
colorslist = ["red","blue","pink","black","purple"]

combined = fruitslist+colorslist
print(combined)

print(combined[1:10:4])