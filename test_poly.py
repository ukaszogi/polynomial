from polynomial import *
from matrices import *

W = Polynomial(1, -5, 6)
G = Polynomial(*[1,2,3])
g = Polynomial([1,2,3])
F = Polynomial(degree=1)
HGhaha = Polynomial()
print(W)
print(W(2))
print(G)
print(F)
print(W+G)
print(W+F)
print(W+2)
F += G
print(F)
tester = W.copy()
Wprim = W.derivative()
print(Wprim)

handler.MatrixPrint(DerivativeMatrix() * W)
