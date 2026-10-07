def double(number):
    return number * 2


def is_pass(score):
    return score >= 50


def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"


print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))
