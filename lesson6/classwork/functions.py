def make_greeting():
    greeting = "Hello, world!"
    return greeting

def build_face():
    face = "(-_-)"
    return face

message = make_greeting()
person = build_face()

print(message)
print('Meet our human:', person)

def personalized_greeting(name):
    greeting = "Hello, " + name + "!"
    return greeting

print(personalized_greeting("Toby"))

def rectangle_area(length, width):
    area = length * width
    return area

print("The area of a 5x3 rectangle is:", rectangle_area(5, 3))