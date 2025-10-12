def hello():
    print("Hello, World!")


def add_numbers(a, b):
    result = a + b
    return result


class TestClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")


x = 5
y = 10
z = x + y
print(z)
