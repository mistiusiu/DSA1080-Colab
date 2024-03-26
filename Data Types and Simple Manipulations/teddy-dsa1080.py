fruits=["mango","kiwi","melon","apple","pineaple"]
print(fruits)
#adding another fruits
fruits.append("orange")
print(fruits)
#replacing the second fruit with banana
fruits[1]="banana"
print(fruits)
#remove the last fruit from the list
fruits.remove("orange")
print(fruits)

fruits1=[fruits[0],fruits[4]]
fruits=fruits[1::2]

print(fruits1)