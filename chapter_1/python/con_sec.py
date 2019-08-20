import numpy as np
import matplotlib.pyplot as plt


class conic_section():

    def __init__(self, p1 : tuple, p2 : tuple, p3 : tuple, w : double):
        self.x1, self.y1 = p1
        self.x2, self.y2 = p2
        self.x3, self.y3 = p3
        self.w = w

    def xc(self, t : double):
        tmp = 1-t
        num = (tmp**2)*self.x1 + 2*tmp*t*self.w*self.x2 + (t**2)*self.x3
        den = tmp**2 + 2*tmp*t*self.w + t**2
        return num/den

    def yc(self, t : double):
        tmp = 1-t
        num = (tmp**2)*self.y1 + 2*tmp*t*self.w*self.y2 + (t**2)*self.y3
        den = tmp**2 + 2*tmp*t*self.w + t**2
        return num/den


P1, P2, P3 = (0, 1), (1, 1), (1, 0)
w = 1/(2**(1/2))
C = conic_section(P1, P2, P3, w)
t = np.arange(0, 1, 0.00001)


plt.plot(C.xc(t), C.yc(t), 'b')
plt.plot(C.xc(1/2), C.yc(1/2), 'r')
print(w)
print(C.xc(1/2), C.yc(1/2))

plt.plot([P1[0], P2[0], P3[0]], [P1[1], P2[1], P3[1]], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Conic section: ' + ' P1 = ' + str(P1) + ' P2 = ' + str(P2) + ' P3 = ' + str(P3))
plt.show()
