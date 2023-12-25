class Point:
    color = 'red'
    circle = 2


Point.color = 'black'
a = Point.color
print(a)


c = Point()
c.color = 'green'
print(c.__dict__)

Point.type_pt = 'disc'

d = Point()

print(c.type_pt)

setattr(Point, 'prop', 1)

print(c.prop)

