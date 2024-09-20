from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("I can walk")
class dog(Animal):
    def move(self):
        print("I can bark")
class lion(Animal):
    def move(self):
        print("I can roar")
class snake(Animal):
    def move(self):
        print("I can slither")
class owl(Animal):
    def move(self):
        print("I can see in the dark")
h=human()
h.move()

d=dog()
d.move

l=lion()
l.move()

s=snake()
s.move()

o=owl()
o.move()