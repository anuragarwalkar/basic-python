class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
    def draw(self):
        print("draw")


point = Point(1, 2)
point.x = 10
point.y = 20

point2 = Point(4, 5)

point2.x = 300

print(point.x)

point.draw()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"I'm taking to you {self.name}")


anurag = Person("Anurag")

anurag.talk()

