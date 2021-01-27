import numpy as np
import matplotlib.pyplot as plt

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

    def plot(self, sub = -10, sup = 10, num = 200):
        """Plots and shows polynomial in real-time usig matplotlib

        Args:
            sub (int, optional): Start of domain. copy of start parameter in linspace. Defaults to -10.
            sup (int, optional): End of domain. copy of stop parameter in linspace. Defaults to 10.
            num (int, optional): Sample size. Copy of num parameter in linspace. Defaults to 200.
        """
        x = np.linspace(sub,sup,num)
        y = self.__call__(x)
        plt.plot(x, y)
        plt.show()
    
    def rootNewtown(self, x=0, tolerance=0.00000001):
        """Newton's method of root finding

        Polynomial must have contionous derivative. This works only for polynomial of a degree above 0 (so 1 and greater).

        Args:
            x (float, optional): strating value of x. Function usually returns closest root to x. Defaults to 0.
            tolerance (float, optional): tolerance of algorythm. Since polynomials are continous, algorythm is destinded to work continously, thus tolerance is used to terminate it early. Defaults to 0.00000001.

        Returns:
            float: root of the Polynomial
        """
        t = tolerance+1
        while t > tolerance:
            x1 = x - self.__call__(x) / self.derivative().__call__(x)
            t = abs(x1 - x)
            x = x1
        return x
    
    def rootHalley(self, x=0, tolerance=0.00000001):
        """Halley's method of root finding

        Polynomial must have contionous second derivative. This works only for polynomial of a degree above 1 (so 2 and greater).

        Args:
            x (float, optional): strating value of x. Function usually returns closest root to x. Defaults to 0.
            tolerance (float, optional): tolerance of algorythm. Since polynomials are continous, algorythm is destinded to work continously, thus tolerance is used to terminate it early. Defaults to 0.00000001.

        Returns:
            float: root of the Polynomial
        """
        t = tolerance+1
        f = lambda x: self.__call__(x)
        fprim = lambda x: self.derivative().__call__(x)
        fbis = lambda x: self.derivative(2).__call__(x)
        while t > tolerance:
            x1 = x - (2*f(x) * fprim(x)) / (2 * (fprim(x))**2 - f(x)*fbis(x))
            t = abs(x1 - x)
            x = x1
        return x

