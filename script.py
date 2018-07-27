
import numpy as np
from scipy.optimize import minimize
from vertex import Vertex
# import objectiveFunctions
from bezier import *
from objectiveFunctions import CamberFunciton

pp = [Vertex(0,0),Vertex(0.25,0.25),Vertex(0.5,0.5),Vertex(0.75,0.25),Vertex(1.0,0.0)]
bz = Bezier(pp)
bz.getPoint
fig = plt.figure()
bz.plot()
point = Vertex(0.2,0.2)
plt.scatter(point.x,point.y)
xn = bz.findNearPoint(point)
plt.scatter(point.x,point.y)
plt.scatter(bz.getPoint(xn).x, bz.getPoint(xn).y)
# пример многомерной минимизации
# x0 = 0.5
# res = minimize(findNearPoint, x0, method='nelder-mead',options={'xtol':1e-6,'disp':True})
camberF = CamberFunciton(bz,point)
camberF.increase()#проверить
x0 = [0.3,0.3,0.3,0.3,0.3,0.3]
res = minimize(camberF.value, x0, method='nelder-mead',options={'xtol':1e-6,'disp':True})

fig2 = plt.figure()
plt.scatter(point.x,point.y)
camberF.plot()
plt.axis('equal')
plt.show()

