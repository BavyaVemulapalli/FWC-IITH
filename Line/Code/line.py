import numpy as np
import math
from matplotlib import pyplot as plt, patches
from matplotlib.patches import Polygon
t1 = np.array([[-1,0], [0,0], [3,5.19]])
x1=t1[2,0]
y1=t1[2,1]
x2=t1[1,0]
y2=t1[1,1]
slope=(y2-y1)/(x2-x1)
print("Slope of QR = Tan(x) = ",'%.2f'%slope)
theta=round(math.degrees(math.atan(slope)))
print("Angle of QR with origin = ",theta)
pqr=int(180-theta)
print("Angle PQR = ",pqr)
r = math.radians(pqr)
q = math.tan(r)
qm = round(q,2)
print("Slope of the angular bisector of PQR = ", qm)
p1 = Polygon(t1, closed=True)
point1 = [0,0]
point2 = [-1,5.19]
x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]
plt. plot(x_values, y_values)
ax = plt.gca()
ax.add_patch(p1)
ax.set_xlim(1,10)
ax.set_ylim(1,10)
p1.set_facecolor('none')
p1.set_edgecolor('black')
plt.xlim(-2,4)
plt.ylim(0,6)
plt.ylabel("Y-axis ")
plt.xlabel("X-axis ")
plt.annotate("P", (-1,0))
plt.annotate("Q", (0,0))
plt.annotate("R", (3,5.19))
plt.annotate("M", (-1,5.19))
plt.show()
