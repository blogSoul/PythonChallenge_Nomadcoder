def minus(a, b):
    return a - b

result = minus(b = 30, a = 1)
print(result)

def say_hello(name, age):
    return f"Hello {name} you are {age} years old"
def say_hello2(name, age):
    return "Hello " + name + " you are" + age + " years old"
hello = say_hello(name = "Soul", age = "20")
hello2 = say_hello2("Soul", "20")
print(hello)
print(hello2)