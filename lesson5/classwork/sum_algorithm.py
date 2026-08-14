numbers = [5, -8, 35, -3, 6, 2]
print(numbers)

total = sum(numbers)
print("The sum is:", total)

print("Our algorithm")

total = 0
for i in range(len(numbers)):
    item = numbers[i]
    total = total + item
print("The sum is:", total)

# Only positive
total = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 0:
        total = total + item
print("The sum of only the positive numbers is:", total)