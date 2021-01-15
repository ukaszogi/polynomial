class Polynomial:
    """Polynomial is standard callable polynomial class. Saves coefficients in a vector, witch allows to easly make advanced libear algebra.

    Parameters:
        *coef (float): Tuple/list of coefficients a_n, a_n-1, ... , a_1, a_0
        degree (uint): If given creates zeroed coefficients vector with certain degree

    Returns:
        Polynomial: Object of a Polynomial class
    """
    def __init__(self, *coef, degree = -1):
        if (degree + 1):
            self.__coef = [0]*(degree+1)
        elif len(coef) == 0:
            self.__coef = [0]
        elif hasattr(coef[0], '__iter__'):
            self.__coef = list(coef[0])
        else:
            self.__coef = list(reversed((coef)))
    
    def __call__(self, x):
        y = 0
        for coef in reversed(self.__coef):
            y = y*x + coef
        return y
    
    def copy(self):
        return Polynomial(self.__coef.copy())

    def __str__(self):
        w = ''
        if len(self.__coef)-1:
            for i in range(len(self.__coef)-1):
                w += str(self.__coef[~i])+'x^'+str(len(self.__coef)+ ~i)+' + '
        w += str(self.__coef[0])
        return w

    def __add__(self, w):
        if isinstance(w, (int, float)):
            c = self.copy()
            c.__coef[0] += w
        else:
            if len(self.__coef) <= len(w.__coef):
                c = w.copy()
                for i in range(len(self.__coef)):
                    c.__coef[i] += self.__coef[i]
            else:
                c = self.copy()
                for i in range(len(w.__coef)):
                    c.__coef[i] += w.__coef[i]
        return c
    
    def __iadd__(self, w):
        if isinstance(w, (int, float)):
            self.__coef[0] += w
        else:
            if len(self.__coef) >= len(w.__coef):
                for i in range(len(self.__coef)):
                    self.__coef[i] += w.__coef[i]
            else:
                temp = self.__coef.copy()
                self.__coef = w.__coef.copy()
                for i in range(len(temp)):
                    self.__coef[i] += temp[i]
        return self

    def __len__(self):
        return(len(self.__coef))

    def __getitem__(self, ind):
        return(self.__coef[ind])
    
    def getVector(self):
        vector = []
        for coeff in self.__coef:
            vector.append([coeff])
        return vector

    def derivative(self, d=1):
        coeff = self.__coef.copy()
        while(d):
            coeff.pop(0)
            for i in range(1, len(coeff)):
                coeff[~i] = coeff[~i]*(len(coeff)+ ~i)
            d -= 1
        return(Polynomial(coeff))