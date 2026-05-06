# overriding

class Animal:

    def speak(self):
        print("animals sound like")
    
class Dog(Animal):
    def speak(self):
        print("bow wow")

class Cat(Animal):
    def speak(self):
        print("meow meow")

class Reset(Animal):
    def speak(self):
        return super().speak()

animal = Animal()
animal.speak()

dog = Dog()
cat = Cat()
reset = Reset()
dog.speak()
cat.speak()
reset.speak()


# 다형성
print("다형성 예제--------------------")
animals = [
    Dog(),
    Cat(),
    Reset()
]

for a in animals:
    a.speak()