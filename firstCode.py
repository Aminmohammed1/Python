print("Hello World")
students_count = 1000
rating = 4.99
is_published = True
print(students_count)
message = """
Hello John,
    Welcome to the Python programming course!"""
print(len(message))
print(message[5])
print(message[-1])
print(message[0:5])
print(message[:5])
print(message[5:])
print(message[:])
first = "mosh"
last = "hamedani"
print(f"{first} {last}")
print(f"{len(first)} {last}")
print(first.upper())
print(message.rstrip())
print(message.find("to"))

#to take user input use input("varbleName:") note the value comes as string.
# x = input("x: ")
# print(type(x))
# y = int(x)+1
# print(f"x: {x}  y:{y}")

#Falsy values for boolean expression..
#""
#0
#None

temp = 15
if temp > 30:
    print("Dring water")
elif temp > 20:
    print("Drink water")
else:
    print("dont drink")
print("Done")

age = 22

message = "Eligible" if age>18 else "Not Elgible"
print(message)

for number in range(1, 4):
    print("Attempt", number, (number)* ".")