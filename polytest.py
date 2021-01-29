from polynomial import *

global sec_num
sec_num = 1
def section(name):
    global sec_num
    print(f'--------======|||======--------\n{sec_num}.\t{name}\n')
    sec_num+=1

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
zero = Polynomial(degree=2)
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

print(W.rootNewtown(6))
print(Big(2))
print(Big.rootHalley(6))
print(Big(2.0159798079799884))

wsm = Polynomial(1,2,1)
# wsm.plot()
print(wsm(2))
print(wsm.rootNewtown())