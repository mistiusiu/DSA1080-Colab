"""
The code below will work on:#
- Creating and modifying lists
- Exploration of tuples
- List Slicing
- Combining lists and tuples
"""

if __name__ == '__main__': # Prevent execution if imported into another file as a module
    # List operations
    fruits = ["Apple", "Mango", "Kiwi", "Avocado", "Pawpaw"]

    fruits.append("Grape")
    print(fruits)

    fruits[1] = "Banana"
    print(fruits)

    fruits.pop()
    print(fruits)

    # Tuple operations
    colors = ("Red", "Blue", "Pink", "Black", "Purple")
    try:
        colors[1] = "Green"
    except TypeError as e: # Catching expected error
        print(e)
    print(colors)

    (colors := list(colors))[0] = "Silver" # FAANG walrus operator
    print(colors := tuple(colors))

    # List slicing
    select_fruit = [fruits[0], fruits[-1]]
    print(select_fruit)
    second_fruits = fruits[1::2]
    print(second_fruits)

    # List and Tuple Combination
    combined = fruits + list(colors)
    print(combined)
    third_items = combined[2::3]
    print(third_items)