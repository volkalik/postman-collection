class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print('call method set_coords', '\n')

    def get_coords(self):
        return (self.x, self.y)

pt = Point()

pt.set_coords(1,2)
print(pt.get_coords())
