import numpy as np
import matplotlib.pyplot as plt

class Polynomial:
    """Polynomial is standard callable polynomial class. Saves coefficients in a NumPy array, witch allows to easly make advanced linear algebra.
    
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

    def __add__(a, b): # since naming isn't obligatory, i named how i please
        c = Polynomial()
        m = max(a.__coef.size, b.__coef.size)
        c.__coef = np.pad(a.__coef, (m-a.__coef.size,0))[0:, -1:] + np.pad(b.__coef, (m-b.__coef.size,0))[0:, -1:]
        return c
    
    def __mul__(a, k):
        b = Polynomial()
        b.__coef *= k
        return b
    
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
            Polynomial: the derivative of a polynomial
        """
        prim = Polynomial()
        prim.__coef = np.array(self.__coef[:, 0][:-1] * np.array(range(1,len(self.__coef)))[::-1], ndmin=2).T # wut
        if d > 1:
            return prim.derivative(d = d-1)
        else:
            return prim

    def integral(self, c=0):
        """Integral of a polynomial (antiderivative).

        Args:
            c (float, optional): constant of integration. Defaults to 0.
        
        Returns:
            Polynomial: the antiderivative of a polynomial
        """
        intl = Polynomial()
        intl.__coef = np.array(np.append(self.__coef[:,0], c) / np.append([1],np.array(range(1, len(self.__coef)+1)))[::-1], ndmin=2).T # wut v2
        return intl

    def defIntegral(self, a, b):
        """Definite integral numeric value calculated using Newton-Leibniz theorem.

        Args:
            a (float): lower bound of the integral
            b (float): upper bound of the integral

        Returns:
            float: numeric value of a integral
        """
        intl = self.integral()
        return intl(b) - intl(a)

    def integralRiemman(self,a,b,c=1000):
        """Numeric integral using rectangles method

        It's very bad. I highly advise not using it. Please use defIntegral

        Args:
            a (float): lower bound of the integral
            b (float): upper bound of the integral
            c (int, optional): sample size density. NUmber of sumples per 1 unit. Defaults to 1000000.
        
        Returns:
            float: numeric value of a integral
        """
        samples = (b-a)*c
        w = 0
        for i in range(samples):
            w += self.__call__(i*(b-a)/samples + a) 
        w *= (b-a)/samples
        return w

    def plot(self, sub = -10, sup = 10, num = 200):
        """Plots and shows polynomial in real-time usig matplotlib

        Args:
            sub (float, optional): Start of domain. copy of start parameter in linspace. Defaults to -10.
            sup (float, optional): End of domain. copy of stop parameter in linspace. Defaults to 10.
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
            float: approximated root of a polynomial
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
            float: approximated root of a polynomial
        """
        t = tolerance+1
        f = lambda x: self.__call__(x)
        fprim = lambda x: self.derivative().__call__(x)
        fbis = lambda x: self.derivative(2).__call__(x)
        while t > tolerance:
            x1 = x - (2 * f(x) * fprim(x)) / (2 * (fprim(x))**2 - f(x)*fbis(x))
            t = abs(x1 - x)
            x = x1
        return x