import numpy as np
from typing import List, Tuple, Union
import matplotlib.pyplot as plt

class Polynomial:
    """Polynomial is standard callable polynomial class. Saves coefficients in a NumPy array, witch allows to easly make advanced linear algebra.
    
    Args:
        *coeff (float): Coefficients a_n, a_n-1, ... , a_1, a_0
        order (uint): If given creates zeroed coefficients vector with certain length (order)
    
    Returns:
        Polynomial: Object of a Polynomial class
    """
    def __init__(self, *coeff, order=-1):
        if order:=order+1:
            self.__coef = np.array([0]*(order), dtype=float, ndmin=2).T
        elif len(coeff) == 0:
            self.__coef = np.array([[0.]])
        else:
            self.__coef = np.array(coeff, dtype=float, ndmin=2).T
        
    @property
    def o(self):
        """Current order of an polynomial. This does call refract method (all leading zeroes will be trimmed).

        Returns:
            int: order
        """
        self.refract()
        return len(self.__coef)-1

    # TODO: add order setter (np.pad and what not)
        
    def __str__(self):
        s = ''
        for i in range(len(self.__coef)-1):
            s += str(self.__coef[i, 0]) + 'x^' + str(len(self.__coef)+ ~i) + ' + '
        s +=  str(self.__coef[len(self.__coef)-1, 0])
        return s
    
    def __call__(self, x) -> float:
        """Horner's method

        Args:
            x (float): argument

        Returns:
            float: value
        """
        y = 0
        for coeff in self.__coef[:, 0]:
            y *= x
            y += coeff
        return y

    def __add__(a, b):
        c = Polynomial()
        if isinstance(b, (int, float)):
            c.__coef = a.__coef.copy()
            c.__coef[-1,0]+=b
        elif isinstance(b, Polynomial):
            m = max(a.__coef.size, b.__coef.size)
            c.__coef = np.pad(a.__coef, (m-a.__coef.size,0))[0:, -1:] + np.pad(b.__coef, (m-b.__coef.size,0))[0:, -1:]
        else:
            raise TypeError(f"Unknown operation for type {type(b)}")
        return c
    
    __radd__ = __add__

    def __neg__(a):
        b = Polynomial()
        b.__coef = a.__coef*-1
        return b

    def __sub__(a, b):
        return a+(-b)

    def __rsub__(a, b):
        return -(a-b)
         
    def __mul__(a, k):
        if isinstance(k, (int, float)):
            b = Polynomial()
            b.__coef = a.__coef.copy()*k
            return b
        elif isinstance(k, Polynomial):
            b = k
            c = Polynomial()
            a_c = a.getArray()[:, 0]
            b_c = b.getArray()[:, 0]
            c.__coef = np.array(np.polymul(b_c, a_c), dtype=float, ndmin=2).T
            return c
        else:
            raise TypeError(f"Unknown operation for type {type(k)}")

    __rmul__ = __mul__

    def __truediv__(a,k):
        if isinstance(k, (int, float)):
            b = Polynomial()
            b.__coef=a.__coef.copy()/k
            return b
        elif isinstance(k, Polynomial):
            b = k
            c = Polynomial()
            d = Polynomial()
            a_c = a.getArray()[:, 0]
            b_c = b.getArray()[:, 0]
            temp = np.polydiv(a_c, b_c)
            c.__coef = np.array(temp[0], dtype=float, ndmin=2).T
            d.__coef = np.array(temp[1], dtype=float, ndmin=2).T
            return c, d
        else:
            raise TypeError(f"Unknown operation for type {type(k)}")

    __div__ = __truediv__

    def refract(self):
        """Really complitated name for deleting leading zeroes
        """
        self.__coef = np.array(np.trim_zeros(self.__coef[:, 0], 'f'), dtype=float, ndmin=2).T

    def getArray(self):
        """Access to coefficients vector 
        
        Returns:
            ndarray: array vector of coefficients, shape (order, n)
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
        for _ in range(d):
            prim.__coef = np.array(self.__coef[:, 0][:-1] * np.array(range(1,len(self.__coef)))[::-1], ndmin=2).T # wut
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
    
    def rootNewtown(self, x=0, tolerance=0.00000001) -> float:
        """Newton's method of root-finding

        Polynomial must have contionous derivative. This works only for polynomial of a order above 0 (so 1 and greater).

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
    
    def rootHalley(self, x=0, tolerance=0.00000001) -> float:
        """Halley's method of root-finding

        Polynomial must have contionous second derivative. This works only for polynomial of a order above 1 (so 2 and greater).

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
    
    def rootHausholder(self, d, x=0, tolerance=0.00000001):
        """Hausholder method of root-finding
        
        Polynomial must have contionous d-th derivative. This works only for polynomial of a order above d-1 (so d and greater).

        Args:
            x (int, optional): strating value of x. Function usually returns closest root to x. Defaults to 0.
            d (int): maximal order of derivative (order of convergance).
            tolerance (float, optional): tolerance of algorythm. Since polynomials are continous, algorythm is destinded to work continously, thus tolerance is used to terminate it early. Defaults to 0.00000001.
        
        Returns:
            float: approximated root of a polynomial
        """
        '''
        x_{n+1} = x_n + d\frac{{1/f}^{(d-1)}(x_n)}{{1/f}^{(d)}(x_n)}
        '''
        raise Exception("Function 'rootHausholder' is not complete. Use 'rootNewtown' or 'rootHalley'")
    
    def solve(self, tolerance=0.00000001):
        """Solving polynomial. Returning set of roots

        Args:
            tolerance (float, optional): tolerance of algorythm. Since polynomials are continous, algorythm is destinded to work continously, thus tolerance is used to terminate it early. Defaults to 0.00000001.

        Returns:
            List[float]: Roots
        """
        if self.o == 0:
            return []
        rr = []
        x = self.rootNewtown(tolerance=tolerance)
        rr.append(x)
        y = self/Polynomial(1, -x)
        rr.extend(y[0].solve(tolerance=tolerance))
        return rr
        
    def interpolateLagrange(self, points: List[Tuple[Union[int, float], Union[int, float]]]):
        """Creates Lagrange interpolation polynomial with given set of pairs of points

        Args:
            points (List[Tuple[Union[int, float], Union[int, float]]]): Set of points presented in a specific way

        Returns:
            Polynomial: interpolation polynomial

        points is structured like this
        >>> points = [
            [x_1, y_1],
            [x_2, y_2],
                ...
            [x_n, y_n]
        ]
        and will result in polynomial of n-th order.
        """
        w = Polynomial()
        for i in range(len(points)):
            li = Polynomial(1)
            for j in range(len(points)):
                if i==j:
                    continue
                li *= Polynomial(1,-points[j][0]) / (points[i][0]-points[j][0])
            w += li*points[i][1]
        return w
