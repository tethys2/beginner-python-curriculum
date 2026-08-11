name = input("What is your name? ")
print("Hi", name)

# Always returns a string
year = input("What year is it? ")
print("It is currently", year)

# Error: cannot add an integer to a string
# print("Next year is", year + 1)

year_num = int(year)
print("Next year is", year_num + 1)

user_number = int(input("Give me a number: "))
print(user_number + 1)