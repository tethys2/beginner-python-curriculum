# comparison operators -> true or false
# logical operators turn true or false back into true false

age = int(input("How old are you? "))
has_ticket = input("Do you have a movie ticket? (yes/no) ")

if age >= 13 and has_ticket == "yes": #And is only true if the conditions on the right AND left are true
    print("You can enter the PG-13 movie.")
else:
    print("Sorry, you can't enter")
print("Movie check complete")

has_pass = input("Do you have a bus pass? (yes/no) ")
has_coins = input("Do you have coins to pay? (yes/no) ")

if has_pass == "yes" or has_coins == "yes": #Or is only false if the conditions on the right and left are false
    print("You can ride the bus.")
else:
    print("You can't ride the bus.")
print("Bus check complete.")

homework_done = input("Did you do your homework? (yes/no) ")

if not homework_done == "yes": #Not flips true to false and false to true
    print("Go finish your homework")
else:
    print("Nice job! you're all done")

is_raining = input("Is it raining? (yes/no) ")
has_umbrella = input("Do you have an umbrella? (yes/no) ")

if is_raining == "yes" and not has_umbrella == "yes":
    print("You might get wet! Stay inside")
elif is_raining == "yes" and has_umbrella == "yes":
    print("You're ready to go outside!")
else:
    print("No rain - you're good to go!")
print("Rain check complete")