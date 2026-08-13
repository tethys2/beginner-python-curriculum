colors = ["red", "green", "blue", "yellow"]

print(colors)
print("First color:", colors[0])
print("Second color:", colors[1])
print("Third color:", colors[2])
print("Fourth color:", colors[3])

# Error: list index out of range
# Maximum is length - 1
# print("Eleventh color:", colors[10])

colors.append("orange")
print("After append:", colors)

colors.insert(2, "purple")
print("After insert at index 2:", colors)

colors.remove("green")
print("After removing green:", colors)

# Eror: finding index of item not in list
# colors.remove("pink")

popped_color = colors.pop()
print("Popped color:", popped_color)
print("After pop:", colors)

popped_color_at_index = colors.pop(1)
print("Popped color at index 1:", popped_color_at_index)
print("After pop at index 1:", colors)

index_of_blue = colors.index("blue")
print("Index of 'blue':", index_of_blue)

# Eror: finding index of item not in list
# colors.index("pink")

colors.append("blue")
blue_count = colors.count("blue")
print("Count of 'blue':", blue_count)

colors.sort()
print("After sort:", colors)

colors.reverse()
print("After reverse:", colors)

