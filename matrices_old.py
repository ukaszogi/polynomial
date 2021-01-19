import matrix_handler as handler

class Matrix:
    """Matrix (and vector) class.

    Parameters: 
        vals (list [list]): values of a matrix
        size (tuple [int, int]): Size of a matrix. Vector is a matrix sized (n, 1)
    
    Returns:
        Matrix: object of a Matrix class
    """
    def __init__(self, vals = 0, size = ('auto', 'auto')):
        if hasattr(vals, '__iter__'):
            if hasattr(vals[0], '__iter__'):
                self.__size = (len(vals), len(vals[0]))
            else:
                self.size = (1, len(vals))
            self.__vals = vals.copy()
        else:
            self.__size = size
            if size != ('auto', 'auto'):
                self.__vals = handler.MatrixMake(size[0], size[1])
    
    def __getitem__(self, ind):
        if self.__size[1] == 1:
            return(self.__vals[ind][0])
        return(self.__vals[ind[0]][ind[1]])

class DerivativeMatrix(Matrix):
    def __mul__(self, w):
        if len(w) - 1:
            n = len(w)
            matrix = handler.MatrixMake(n-1, n)
            vector = handler.MatrixMake(n, 1)
            for i in range(1, n):
                matrix[i-1][i] = i
                vector[i][0] = w[i]
            # handler.MatrixPrint(matrix)
            self.size = (n-1, n)
            handler.MatrixPrint(vector, "pętla")
            handler.MatrixPrint(w.getVector(), "metoda")
            return handler.MatrixMulti(matrix, vector)
        else:
            return [[0]]

class IdentityMatrix(Matrix):
    pass