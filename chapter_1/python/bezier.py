import numpy as np
import matplotlib.pyplot as plt

# from scipy.special import comb

# def bernstein(n, t, i):
#     res = 0
#     ant = 1-t
#     res = comb(n,i, exact=True)*(ant**n-i)*(t**i)
#     return res
class bezier():

    def __init__(self, p0 : tuple, p1 : tuple, p2 : tuple, p3 : tuple):
        self.x0, self.y0 = p0
        self.x1, self.y1 = p1
        self.x2, self.y2 = p2
        self.x3, self.y3 = p3

    def xc(self, t : int):
        tmp = 1-t
        return (tmp**3)*self.x0 + 3*t*(tmp**2)*self.x1 + 3*(t**2)*tmp*self.x2 + (t**3)*self.x3

    def yc(self, t : int):
        tmp = 1-t
        return (tmp**3)*self.y0 + 3*t*(tmp**2)*self.y1 + 3*(t**2)*tmp*self.y2 + (t**3)*self.y3


# P0, P1, P2, P3 = (0, 0), (0, 8), (7, 6), (5, 0)
# P0, P1, P2, P3 = (0, 0), (0, 24), (9, 12), (5, 0)
P0, P1, P2, P3 = (0, 0), (1, 1), (2, 7), (3, 0)
B = bezier(P0, P1, P2, P3)
t = np.arange(0, 1, 0.0000001)


plt.plot(B.xc(t), B.yc(t), 'b')

plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Bezier curve: ' + 'P0 = ' + str(P0) + ' P1 = ' \
 + str(P1) + ' P2 = ' + str(P2) + ' P3 = ' + str(P3))
plt.show()
