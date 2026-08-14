fruit = ["banana", "apple"]

if "apple" in fruit:
    print("found apple")
else:
    print("no apples found")

print("Our algorithm")

found = False
index = -1

for i in range(len(fruit)):
    if fruit[i] == "apple":
        found = True
        index = i
        break # Exit the loop after finding

if found == True:
    print("Found apple at", index)
else:
    print("No apples in the list")