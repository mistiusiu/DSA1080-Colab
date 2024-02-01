#Q1
#Create a list named 'fruits' containing at least five different fruits
fruits=["apple", "mango","kiwi","Avocado","pawpaw"]
#add another fruit at the end of the list
fruits.append("Grapes")
print(fruits)
#Replace the second fruit in the list with the word "Banana"
fruits[1]="banana"
print(fruits)
#Replace the second fruit in the list with the word "Banana"
fruits.remove("pawpaw")
print(fruits)
#2
##tuple exploration
#Create a tuple named 'colors' containing at least four different colors
colours=("Red","Blue","pink","Black","Purple")

# colours[1] = "Green"
print("colours")

#Convert the tuple into a list, change the first color to "Silver", and convert it back to a tuple
converted=list(colours)
converted[0]="silver"
tuple(converted)
print(converted)

#Q3
#List Slicing
#Using the 'fruits' list, create a new list containing only the first and last fruit in the
#original list.
fruits_sliced=fruits[0],fruits[4]
print(fruits_sliced)
#Create a slice of 'fruits' that contains every second fruit in the list

fruits_sliced2=fruits[1::2]
fruits_sliced2

#Q4
#Combine the 'fruits' list and the 'colors' tuple into a new list named 'combined'.
#Create a slice of the 'combined' list that contains every third item.
colours=("Red","Blue","pink","Black","Purple")
combined=fruits.extend(colours)
combined=fruits
print(combined)
#printing the third
combined_third=combined[1::3]
print(combined_third)



#Create a slice of 'fruits' that contains every second fruit in the list

fruits_sliced2=fruits[::2]
fruits_sliced2


