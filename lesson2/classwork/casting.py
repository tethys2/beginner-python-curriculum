num_str = "42"
# "42" -> 42
num_value = int(num_str)
print(num_value + 1)

decimal_str = "3.14"
# "3.14" -> 3.14
decimal_value = float(decimal_str)
print(decimal_value + 2.19)

# "16" not 16
age_text = input("How old are you? ")
age = int(age_text)
print("Next year you will be", age + 1, "years old.")

num = 20
# 100 -> "100"
num_str2 = str(num)
print("This burger costs $" + num_str2)
