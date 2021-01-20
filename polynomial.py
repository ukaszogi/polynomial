import numpy as np

class Polynomial:
    """Polynomial is standard callable polynomial class. Saves coefficients in a NumPy array, witch allows to easly make advanced libear algebra.

    Args:
        *coeff (float): Coefficients a_n, a_n-1, ... , a_1, a_0
        degree (uint): If given creates zeroed coefficients vector with certain degree

    Returns:
        Polynomial: Object of a Polynomial class
    """
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
    
    def getArray(self):
        """Access to coefficients vector 

        Returns:
            ndarray: array vector of coefficients, shape (degree, n)
        """
        return self.__coef.copy()

    def derivative(self, d=1):
        """Derivative of a polynomial.

        Args:
            d (int, optional): order of derivative (recc.). Defaults to 1.

        Returns:
            Polynomial: the derivative of the polynomial
        """
        prim = Polynomial()
        prim.__coef = np.array(self.__coef[:, 0][:-1] * np.array(range(1,len(self.__coef)))[::-1], ndmin=2).T # wut
        if d > 1:
            return prim.derivative(d = d-1)
        else:
            return prim