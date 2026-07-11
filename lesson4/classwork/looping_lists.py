numbers = [4, 7, 12, 3]

for i in range(len(numbers)):
    print(numbers[i])

animals = ["cat", "dog", "rabbit"]

for i in range(len(animals)):
    print("Animal", i, "is", animals[i])

sum = 0
for i in range(len(numbers)):
    sum = sum + numbers[i]
print("Sum is", sum)