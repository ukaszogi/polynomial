from polynomial import Polynomial

W = Polynomial(1, -5, 6)
G = Polynomial([1,2,3])
F = Polynomial(degree=1)
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