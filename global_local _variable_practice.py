APPLE = 100
a = None
def fun():
    global a
    a = 20
    return a+100
print("past a = ", a)
print(fun())
print("a now = ", a)


class Calculator:
    name = 'Good Calculator'
    price = 18
    def add(self, x, y):
        print(self.name)
        result = x + y
        print(result)
