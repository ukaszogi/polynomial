from polynomial import *

class section:
    sec_num = 1
    def __init__(this, name):
        print(f'--------======|||======--------\n{section.sec_num}.\t{name}\n')
        section.sec_num+=1

a = np.array([[1],[2],[3]])
b = np.array([[1,2,3]])
c = np.array([1,2,3], ndmin=2).T
print(a)
print(b)
print(a*b)
print(b*a)
print(a@b)
print(b@a)
print(c)
print(c[:, 0])
print((c[::-1,0])[1:])
print(np.array(range(1,len(c)))[::-1])

section('Derivative testing')

c = np.array([1,2,3,4,5], ndmin=2).T
print(c)
print(c[:, 0])
print(c[:, 0][:-1])
print(np.array(range(1,len(c)))[::-1])
print(c[:, 0][:-1] * np.array(range(1,len(c)))[::-1])
print(np.array(c[:, 0][:-1] * np.array(range(1,len(c)))[::-1], ndmin=2).T)
# prim.__coef = np.array(((self.__coef[::-1,0])[1:] * np.array(range(1,len(self.__coef))))[::-1], ndmin=2).T

section('Derivatives')

W = Polynomial(1, -5, 6)
zero = Polynomial(order=2)
print(W)
print(W(2))
print(zero)
print(W.derivative())
print(W.derivative(d=2))

# W.plot()
# W.derivative().plot()

Big = Polynomial(-1, -4, 7, 0, 1, 40)
print(Big)
# Big.plot()

section("Root finding")

print(W.rootNewtown(6))
print(Big(2))
print(Big.rootHalley(6))
print(Big(2.0159798079799884))

wsm = Polynomial(1,2,1)
# wsm.plot()
print(wsm(2))
print(wsm.rootNewtown())

# print(W+wsm)

# print( np.reshape(np.reshape(np.array([1,2,3]), (3,1)), (4,1)))

q = np.reshape(np.array([1,2,3]), (3,1))
w = np.reshape(np.array([1,2,3,4]), (4,1))

print(np.pad(q, (max(q.size, w.size)-q.size,0))[0:, -1:])
print(np.pad(w, (max(q.size, w.size)-w.size,0))[0:, -1:])
print(
    np.pad(q, (max(q.size, w.size)-q.size,0))[0:, -1:] +
    np.pad(w, (max(q.size, w.size)-w.size,0))[0:, -1:]
)

print(Polynomial(1,2) + Polynomial(2,1,3))

print((Polynomial(1,2,3,4) * 2))

section("Integral testing")

print(Polynomial(1,0,0).integralRiemman(0,1))

# 1x^2 + 0x + 0 
# 1/3(x^3) + 0x^2 + 0x + 0
# ax^n => a/n+1(x^n+1)
# [a,b,c] => [a/3, b/2, c, 0]
# ([3, 2, 1 :: c])/[3, 2 ,1 ,1] = 1, 1, 1, c
# ()/ np.array(range(1, len(j)))
co = np.array([[3],[2],[1]])
# print(len(co))
j = co[:,0]
# print(j)
c = 4
j = np.append(co[:,0], c)
# print(j)
i = np.append([1],np.array(range(1, len(j))))
# print(i)
i = i[::-1]
print(np.array(j/i,ndmin=2).T)

print(Polynomial(3,2,1).integral(4))

section('Exceptions')

try:
    wsm.rootHausholder(3)
except Exception as exc:
    print(exc)


section('interpolation')

pointsDict = { # set of points for y = (x+3)(x+2)
    1: 12,
    -1: 2,
    3: 30,
    0: 6
}
print(pointsDict)
for (x, y) in pointsDict.items():
    print(x, y)

pointsList = [6, 12]
# for (x, y) in pointsList.items():
#     print(x, y)

tabXY = [
    [1, 12],
    [-1, 2],
    [3, 30],
    [0, 6]
]
for (x, y) in tabXY:
    print(x, y)



section('No section?')

print(Polynomial(1,2,3,4).getArray())
print(Polynomial(1,2,3)*2.5)
print((Polynomial(1,2,3)+Polynomial(order=45)).o)
print(np.convolve([1,2][::-1],[1,2,3]))# (1+2x)(1+2x+3x2)=(1+4x+)
print(Polynomial(1,2)*2)
print(Polynomial(1,2)*Polynomial(1,2,3))
print(Polynomial(1,2,3)*Polynomial(1,2))

Polynomial(1,2,3)

print(2*Polynomial(12,3))
print(Polynomial(10, 2)-1)
print(-Polynomial(1,2,3))
print(Polynomial(10, 2)-Polynomial(12,3))
print(2-Polynomial(12,3))

section("interpolation")

a = Polynomial().interpolateLagrange([[2, 30], [6, 0], [-3, 0]])
print(a)
print(a(2))
print(a(6))
# a.plot()
print(a.rootNewtown())
b=(a / Polynomial(1,3))
print(b[0])

section('solving')

a = Polynomial(1, -5, 6)
rr = a.solve()
print(rr)