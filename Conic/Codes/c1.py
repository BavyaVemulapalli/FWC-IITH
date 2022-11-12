from sympy.core.evalf import quadts
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sympy as sym

#Generating points on an ellipse
def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse

#if using termux
import subprocess
import shlex
import math
#end if


#Input parameters
V1 = np.array(([1,0],[0,4]))
u1 = np.array(([0],[0]))
f1=np.array(([-4]))
q=np.array(([0],[1]))
V2=np.array(([1,0],[0,2]))
u2 = np.array(([0],[0]))
f2=np.array(([-6]))
e1 = np.array(([1,0]))#standard basis vector
e2 = np.array(([0,1]))#standard basis vector
O=np.array((0,0))
#n1 = A[0,:]
#n2 = A[1,:]
#c1 = b[0]
#c2 = b[1]

x=sym.Symbol('x')
y=sym.Symbol('y')
X=np.array((x,y))

print("------------------------")
print("Vector V of the 1st Ellipse")
print(V1)

print("------------------------")
print("Vector u of the 1st Ellipse")
u1=-O@V1
print(u1)

print("------------------------")
print("Equation of the Tangent at q to the 1st ellipse is")
t_eq= ((V1@q).transpose()@X)+(u1.transpose()@q)+f1
print("{}=0".format(t_eq))




m = np.array(([-4],[0]))
#print(n)
mu1 = (2*LA.norm(m))/(m.T@V2@m)
P = q + mu1*m
mu2 = (-2*LA.norm(m))/(m.T@V2@m)
Q = q + mu2*m
print("------------------------")
print("Points of intersection of tangent of the 1st ellipse to the second ellipse is")
print(P)
print(Q)

print("------------------------")
print("Vector V of the 2nd Ellipse")
print(V2)

print("------------------------")
print("Vector u of the 2nd Ellipse")
u2=-O@V2
print(u2)


print("------------------------")
print("Equation of the Tangent at P to the 2nd ellipse is")
P_eq= ((V2@P).transpose()@X)+(u2.transpose()@P)+f2
print("{}=0".format(P_eq))


print("------------------------")
print("Equation of the Tangent at Q to the 2nd ellipse is")
Q_eq= ((V2@Q).transpose()@X)+(u2.transpose()@Q)+f2
print("{}=0".format(Q_eq))


P1 = (V2@P)
Q1 = (V2@Q)
print("------------------------")
angle=P1.transpose()@Q1
print("P1.transpose()@Q1 = ",angle)


##plotting##

#Plotting all lines
x = np.linspace(-5,5,5)
plt.plot(x, 3+x, '-b',label='$line: -x+y=3$')
plt.plot(x, 3-x, '-m',label='$line: x+y=3$')

point1 = [-7,1]
point2 = [7,1]
x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]
plt. plot(x_values, y_values, '-g', label='$y=1$')

O = np.array([0,0])
Maj1=2
Min1=1
Maj2=np.sqrt(6)
Min2=np.sqrt(3)

ellipse1 = ellipse_gen(Maj1,Min1)
plt.plot(ellipse1[0,:],ellipse1[1,:], '-y', label='$Ellipse:x^2+4y^2-4=0$')

ellipse2 = ellipse_gen(Maj2,Min2)
plt.plot(ellipse2[0,:],ellipse2[1,:], '-y', label='$Ellipse:x^2+2y^2-6=0$')


plt.annotate("P", (-2,1))
plt.annotate("Q", (2,1))
plt.annotate("q", (0,1))
plt.annotate("A", (0,3))
plt.xlim(-7,7)
plt.ylim(-7,7)
plt.legend()
plt.grid()
#if using termux
plt.savefig('/sdcard/Github/Conic/Images/c1.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Github/Conic/Images/c1.pdf")) 
#else
