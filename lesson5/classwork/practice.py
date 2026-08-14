# Problem 1
# Search the list and print whether "banana" is found.
fruits = ["apple", "orange", "banana", "grape"]

found = False
for i in range(len(fruits)):
    item = fruits[i]
    if item == "banana":
        found = True

if found == True:
    print("Found banana")
else:
    print("No banana found")

# Problem 2
# Count how many numbers are greater than 10 in the list.
numbers = [4, 18, 2, 30, 7, 12]

counter = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 10:
        counter = counter + 1

print(counter, "numbers are greater than 10")

# Problem 3
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]

total = 0
for i in range(len(numbers)):
    item = numbers[i]
    total = total + item

print("The total is:", total)

# Problem 4
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0]

biggest = numbers[0]
for i in range(len(numbers)):
    item = numbers[i]
    if item > biggest:
        biggest = item

print("The biggest number is:", biggest)

# Problem 5
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]

total = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item % 2 == 0:
        total = total + item

print("The sum of even numbers is:", total)