
a = 2
b = 0
try:
    print(a / b)
except TypeError as e:
    print(e)
except ZeroDivisionError:
    print(1)