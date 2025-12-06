def greet():
    print(f"Hello world")


greet()    

def greet_person(name):
    print(f"Hello {name}")

greet_person("amin")

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("amin")

# file = open("greet.txt", "w")
# file.write(message)
# file.close

# positional args in methods in python

def increment(by, number):
    return number+by

print(increment(number=5, by=2))


# optional parameters in a method
def increment_optional_by_parameter(number, by=1):
    return number+by

print(increment_optional_by_parameter(5))
print(increment_optional_by_parameter(5, 3))

# *args
def multiply(*numbers):
    total = 1
    for number in numbers:
        total = number*total
    return total

print(multiply(2,3,4,5))    