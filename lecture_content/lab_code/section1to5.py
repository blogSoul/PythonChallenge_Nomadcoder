def say_hello(who = "big"):
    print("hello", who)
say_hello("Nicolas")
say_hello()

def plus(a, b):
    print(a + b)
plus(1, 2)

def minus(a, b = 0):
    print(a -b)
minus(2, 5)
minus(2)