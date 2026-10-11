fruit = ["apple", "banana", "apple"]

if "apple" in fruit:
    print("Found the apple at", fruit.index("apple"))
else:
    print("no apples found")

print("Our algorithm:")

# Find if apple in list and print its index.W

found = False
index = -1

for i in range(len(fruit)): # 0, 1, 2 ... len(fruit) - 1 = len(fruit) iterations in total
    if fruit[i] == "apple":
        found = True # Mark as found
        index = i # Save the index
        break # Exists the loop, means we find the first instance of apple

if found == True:
    print("Found the apple at", index)
else:
    print("No apples in the list")