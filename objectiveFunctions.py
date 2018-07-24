from bezier import *
import math
e = 1e-6 #точность
def half_divide_method(a, b, f):
    e = 1e-6
    x = (a + b) / 2
    while math.fabs(f(x)) >= e:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    return (a + b) / 2

def newtons_method(a, b, f, f1):
    x0 = (a + b) / 2
    x1 = x0 - (f(x0) / f1(x0))
    while True:
        if math.fabs(x1 - x0) < e: return x1
        x0 = x1
        x1 = x0 - (f(x0) / f1(x0))
# from vertex import *
class CamberFunciton(Bezier):
    isRecompute = True # перестраивать кривую или нет
    point = Vertex(0.5,0.5)
    def __init__(self, bezier, _point):
        self = Bezier(bezier.ppoints)
        self.point = _point
    def recompute(self,x):
        size = len(x)
        v0 = self.dt(0.0).increase(x[0])
        vn = self.dt(1.0).increase(x[-1])
        pp = []
        pp.append(self.controlPoints[0].move(v0**2))
        for i in range(1,size-1,2):
            px = x[i]
            py = x[i+1]**2
            pp.append(Vertex(px,py))
        pp.append(self.controlPoints[-1].move(vn**2))
        self.setControlPoints(pp)
    def consider(self,x):
        return (self.getPoint(self.findNearPoint(self.point)).length(self.point))**2
    def tangent(self,x):
        pass
    def curvature(self,x):
        pass
    def value(self,x):
        self.recompute(x)
        return self.consider(x) + self.tangent(x) + self.curvature(x)