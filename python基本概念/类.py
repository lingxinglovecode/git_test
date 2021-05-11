
##本节主要简述与类相关的操作


class Dog:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def __add__(self, other):
        return self.age + other.age

    def __str__(self):
        return self.name

dog_1 = Dog(12,'Bob')
dog_2 = Dog(4,'Jack')
print(dog_1+dog_2)
print(dog_2)