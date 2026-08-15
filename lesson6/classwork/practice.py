# Problem 1
# Write a function that returns your favorite fruit and print it.

def favorite_fruit():
    fruit = "mango"
    return fruit
print("My favorite fruit is:", favorite_fruit())

# Problem 2
# Write a function that takes one parameter num.
# The function should return the value of num multiplied by 2.

def multiply_by_two(num):
    return num * 2

print(multiply_by_two(7))

# Problem 3
# Create a variable for a book, then print it.
# Modify it inside a function and print it again.

book = "The Hobbit"

def show_book():
    print("Current book is", book)

def change_book():
    global book
    book = "Lord Of The Rings"

show_book()
change_book()
show_book()

# Problem 4
# Use a while loop to print the numbers from 1 to 7 (inclusive).

i = 1
while i < 8:
    print(i)
    i = i + 1

# Problem 5
# Use a while loop to print each element in the list.
items = ["chair", "table", "desk"]

i = 0
while i < len(items):
    print(items[i])
    i = i+1