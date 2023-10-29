# V = π·r²·h
# A=2πrh+2πr2
import math

pi = math.pi


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = pi * self.radius ** 2 * self.height
        return vol

    def surface_area(self):
        area = (2 * pi * self.radius * self.height) + 2 * pi * self.radius ** 2
        return area


c = Cylinder(2, 3)
print(f"volume of cylinder is {c.volume()}")
print(f"area of cylinder is {c.surface_area()}")

print("\n________________________\n")


# math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2


    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        d = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
        return d
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        s = (y2-y1)/(x2-x1)
        return s


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())

