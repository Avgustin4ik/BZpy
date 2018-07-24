import matplotlib.pyplot as plt
import math
# import objectiveFunctions
from vertex import Vertex
from vertex import Vector
class Bezier():
    controlPoints =  [Vertex]
    bernstein = []
    m = 0 
    def __init__(self, ppoints):
        for i in ppoints:
            self.controlPoints.append(i)
        self.m = len(self.controlPoints) - 1
        self.compute()
    def compute(self):
        for i in range(self.m + 1):
            value = math.factorial(self.m) / math.factorial(i) / math.factorial(self.m-i)
            self.bernstein.append(value)
    def getPoint(self,t):
        # вставить исключение проверяющее значение t
        r = Vertex(0,0) 
        for i in range(self.m + 1):
            r.x = r.x + self.controlPoints[i].x * self.bernstein[i] * math.pow(t,i) * math.pow((1-t),(self.m - i))
            r.y = r.y + self.controlPoints[i].y * self.bernstein[i] * math.pow(t,i) * math.pow((1-t),(self.m - i))
        return r
    def plot(self):
        x = []
        y = []
        for i in range(101):
            t = i/100
            x.append(self.getPoint(t).x)
            y.append(self.getPoint(t).y)
        plt.plot(x,y)
        x.clear()
        y.clear()
        for i in self.controlPoints:
            x.append(i.x)
            y.append(i.y)
        plt.plot(x,y)
    def setControlPoints(self, pp):
        self.controlPoints = pp
        self.m = len(self.controlPoints - 1)
        self.bernstein.clear()
        self.compute()
    def dt(self,t):
        n = self.m - 1
        cp = self.controlPoints
        result = Vector(0,0)
        for i in range(0,n,1):
            bz = math.factorial(n) / math.factorial(i) / math.factorial(n-i)
            result.x = result.x + bz * (1 - t)**(n-i) * (cp[i+1].x - cp[i].x)
            result.y = result.y + bz * (1 - t)**(n-i) * (cp[i+1].y - cp[i].y)
        return result
    def ddt(self,t):
        pass
    def findNearPoint(self,point):
        a = 0
        b = 1
        dx = 0.001
        n = 0
        def f(x):
            return self.getPoint(x).length(point)
        while abs(b - a) > 1e-3:
            x = (a+b)/2
            f1 = f(x-dx)
            f2 = f(x+dx)
            if f1>f2:
                a = x
            else:
                b = x
            n += 1
        return (a+b)/2
