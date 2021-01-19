from polynomial import *

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
print(np.linspace(1,c.shape[0]-1,num=c.shape[0]-1))
print((c[::-1,0])[1:] * np.linspace(1,c.shape[0]-1,num=c.shape[0]-1))

W = Polynomial(1, -5, 6)
zero = Polynomial(degree=2)
print(W)
print(W(2))
print(zero)
print(W.derivative())
print(W.derivative(d=2))