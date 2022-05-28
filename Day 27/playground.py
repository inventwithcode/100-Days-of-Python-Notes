# Unlimited arguments using *args
# *anything can also be used

def sum(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


# print(sum(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    n -= kwargs["subtract"]
    n /= kwargs["divide"]
    return n


# print(calculate(2, add=2, multiply=4, subtract=9, divide=7))


class Animal():
    def __init__(self, **kwargs):
        self.color = kwargs.get("color", "grey")
        self.type = kwargs.get("type", "aquatic")


whale = Animal(color="blue")
crocodile = Animal(color="green", type="multi")
# print(whale.type)
# print(whale.color)
# print(crocodile.type)
# print(crocodile.color)
