# Simple class demonstrator

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, init_x, init_y):
        """ Create a new point at the origin. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_self(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


def distance(point1, point2):
    x_diff = point2.get_x()-point1.get_y()
    y_diff = point2.get_y()-point1.get_y()

    dist = math.sqrt(x_diff**2 + y_diff**2)
    return dist

p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)
print(p.get_x())
print(p.get_y())
print(q.get_x())
print(q.get_y())
print(p.distance_from_self())
print(distance(p, q))
print(p)
print(mid)
print(mid.get_x())
print(mid.get_y())




