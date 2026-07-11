import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.

cars = ["Toyota", "BMW", "Subaru", "Tesla"]
print(cars[0])
print(cars[len(cars) - 1])
cars.append("Ford")
print("After append:", cars)


# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.

nums = [13, 26, 39, 52, 65]
print(nums[2])
nums.insert(2, 99)
print("After insert:", nums)

# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then use a for loop to print each city.

cities = ["Tokyo", "Berlin", "Nairobi"]
print(len(cities))
for i in range(len(cities)):
    print(cities[i])

# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.

extensions = ["pdf", "docx", "pptx", "xlsx", "jpg", "mpg"]
rand_index = random.randint(0, len(extensions) - 1)
print(extensions[rand_index])
extensions.pop(3)
print("After pop at index 3:", extensions)

# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then use a for loop to print all the names.

users = ["alex01", "bravo12", "charlie23", "delta34", "echo45", "foxtrot56", "golf67", "hotel78"]
mid_index = len(users) // 2
print(users[mid_index])
for i in range(len(users)):
    print(users[i])