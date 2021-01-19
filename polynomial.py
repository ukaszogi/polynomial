import numpy as np

class Polynomial:
    def __init__(self, *coeff, degree=-1):
        if degree:=degree+1:
            self.__coef = np.array([0]*(degree), dtype=float, ndmin=2).T
        elif len(coeff) == 0:
            self.__coef = np.array([[0.]])
        else:
            self.__coef = np.array(coeff, dtype=float, ndmin=2).T
        
    def __str__(self):
        s = ''
        for i in range(len(self.__coef)-1):
            s += str(self.__coef[i, 0]) + 'x^' + str(len(self.__coef)+ ~i) + ' + '
        s +=  str(self.__coef[len(self.__coef)-1, 0])
        return s

    def __call__(self, x):
        y = 0
        for coeff in self.__coef[:, 0]:
            y *= x
            y += coeff
        return y
    
    def derivative(self, d=1):
        prim = Polynomial()
        prim.__coef = np.array(((self.__coef[::-1,0])[1:] * np.linspace(1,self.__coef.shape[0]-1,num=self.__coef.shape[0]-1))[::-1], ndmin=2).T # wut
        if d > 1:
            return prim.derivative(d = d-1)
        else:
            return prim