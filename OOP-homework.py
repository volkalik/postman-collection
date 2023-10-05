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