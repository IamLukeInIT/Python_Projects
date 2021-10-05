name = "John"
print("Hello " + name)

name = "Bob"
number = 7
print("Hello " + name + ". This is your lucky number " + str(number) + ".")

color = input("What is your favourite color?\n")  # \n make new line
print("Your favourite color is " + color)

if color == "green":
    print("I like " + color + " too!")
else:
    print("Oh I prefer green")

status = not False
print(status)

print(type(name))
print(type(number))
print(type(status))
