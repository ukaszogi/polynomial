import matrix_handler as mh

class Matrix:
    pass

class DerivativeMatrix(Matrix):
    def __mul__(self, w):
        n = len(w)
        matrix = mh.MatrixMake(n-1, n)
        vector = mh.MatrixMake(n, 1)
        for i in range(1, n):
            matrix[i-1][i] = i
            vector[i][0] = w[i]
        mh.MatrixPrint(matrix)
        mh.MatrixPrint(vector)
        return mh.MatrixMulti(matrix, vector)

class IdentityMatrix(Matrix):
    pass