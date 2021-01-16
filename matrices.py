import matrix_handler as handler

class Matrix:
    """Matrix (and vector) class.

    Parameters: 
        size (typle [int, int]): Size of a matrix. Vector is a matrix sized (n, 1)
    """
    def __init__(self, size = ('auto', 'auto')):
        self.__size = size

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