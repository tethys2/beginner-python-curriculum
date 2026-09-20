num_str = "42"
num_int = int(num_str)
print(num_int + 1)

# Error: it thinks we are concatenating, and you cannot concatenate a number to a string
# print(num_str + 1)

float_str = "3.14"
num_float = float(float_str)
print(num_float + 2.19)

# Error: it thinks we are concatenating, and you cannot concatenate a number to a string
# print(float_str + 2.19)

int_num = 7
float_num = float(int_num)
print(float_num)

float_num2 = 9.99
int_num2 = int(float_num2)
print(int_num2)

num = 20 
num_str2 = str(num) # Convert 20 to "20"
print("This shirt costs $" + num_str2)

# Error:
# print("This shirt costs $" + num)