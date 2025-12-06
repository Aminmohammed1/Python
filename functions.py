def greet():
    print(f"Hello world")


greet()    

def greet_person(name):
    print(f"Hello {name}")

greet_person("amin")

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("amin")

file = open("greet.txt", "w")
file.write(message)
file.close