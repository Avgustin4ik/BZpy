from math import sqrt
class Vector(object):
    x = float(0)
    y = float(0)
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
    def normalize(self):
        pass
    def increase(self, value):
        self.x *= value
        self.y *= value
    def setLength(self, value):
        pass
        
class Vertex(object):
    x = float(0)
    y = float(0)
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
    def length(self, point):
        return sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
    def move(self, vector : Vector):
        self.x += vector.x
        self.y += vector.y