fruits = ["Orange", "Apple", "Kiwi", "Avacado"]
fruits.append("Grape")
fruits.pop(1)
fruits.insert(1,"Banana")
fruits.pop()
print(fruits)

#tuple exploration
tuple = ("Purple", "Red", "Pink", "Black",)
y = list (tuple)
y.append("Silver")
tuple = tuple(y)

fruits = ["Orange", "Apple", "Kiwi", "Avacado"]
fruits =(fruits[0]+","+ fruits[-1])
print(fruits)
fruits = (fruits[1:5:2])
print(fruits)

combine the fruits list and the colours tuple into a new list named combined
colours = ('Red', 'Blue', 'Pink', 'Purple')
fruits = ["Orange", "Apple", "Kiwi", "Avacado"]
combined = fruits + colours
print(combined)