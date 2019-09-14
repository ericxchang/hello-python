import math

'two dimensional point geometric coordinates'
class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)

    def reset(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


print("__name__ value: ", __name__)

point1 = Point()
point2 = Point(1, 2)
point1.reset()
point2.move(5, 0)
print(point2.distance(point1))
point1.move(3, 4)
print(point1.distance(point2))
