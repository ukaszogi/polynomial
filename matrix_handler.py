import math
def MatrixMake(n,m):
    c = [[0.0]]
    for i in range(n):
        c.append([0.0])
        for _ in range(m):
            c[i].append(0.0)
    c.pop()
    for i in range(len(c)):
        c[i].pop()
    return c

def MatrixIdentity(n):
    i = MatrixMake(n,n)
    for j in range(n):
        i[j][j] = 1
    return i
    
def MatrixAdd(a,b):
    c = MatrixMake(len(a),len(a[0]))
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j]+b[i][j]
    return c

def MatrixMulti(a,b):
    c = MatrixMake(len(a),len(b[0]))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for p in range(len(b)):
                c[i][j] += a[i][p]*b[p][j]
    return c

def MatrixScale(a,k):
    c = MatrixMake(len(a),len(a[0]))
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j]*k
    return c 

def MatrixTrans(a):
    c = MatrixMake(len(a[0]),len(a))
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[j][i] = a[i][j]
    return c 

def MatrixPrint(a, msg=""): # msg 
    print(msg,end=" ")
    print(len(a),"x",len(a[0]))
    for i in range(len(a)):
        print(a[i])
    print()

def perm(v,a):
    w = MatrixMake(len(a)+1,len(a)+1)
    for i in range(len(a)+1):
        for j in range(len(a)+1):
            if j>i:
                w[i][j] = a[j-1]
            elif j==i:
                w[i][j] = v
            else:
                w[i][j] = a[j]
    return w

def PermNat(n):
    n-=1
    a = MatrixMake(n+2,1)
    a[0] = [[0]]
    for p in range(n+1):
        for i in range(len(a[p])):
            for j in range(len((perm(p+1,a[p][i])))):
                a[p+1].append((perm(p+1,a[p][i]))[j])
        a[p+1].pop(0)
    return a[n]

def InversionCount(a):
    w = 0
    for i in range(len(a)):
        for j in range(i):
            if a[i]<a[j]:
                w+=1
    return w

def MatrixDet(a):
    per=PermNat(len(a))
    det = 0.0
    for i in range(len(per)):
        diag = 1.0
        for j in range(len(per[0])):
            diag*= a[j][per[i][j]]
        diag*=(-1)**InversionCount(per[i])
        det+=diag
    return det

def MatrixMinor(a,n,m):
    b = MatrixMake(len(a)-1,len(a)-1)
    for i in range(len(b)):
        for j in range(len(b)):
            if i>=n:
                if j>=m:
                    b[i][j]=a[i+1][j+1]
                else:
                    b[i][j]=a[i+1][j]
            else:
                if j>=m:
                    b[i][j]=a[i][j+1]
                else:
                    b[i][j]=a[i][j]
    return b

def Cofactor(a,n,m):
    cf = float((-1)**(n+m)*MatrixDet(MatrixMinor(a,n,m)))
    return cf

def MatrixInverse(a):
    b = MatrixMake(len(a),len(a))
    for i in range(len(a)):
        for j in range(len(a)):
            b[j][i]=Cofactor(a,i,j)/MatrixDet(a)
    return b

def Test():
    a = [[2.5,2],[2,2]]
    b = [[3,3],[3,3]]
    c = [[1],[1]]
    MatrixPrint(MatrixAdd(a,b))
    MatrixPrint(MatrixMulti(a,b))
    MatrixPrint(MatrixAdd(b,MatrixScale(a,-1)))
    MatrixPrint(MatrixTrans(c))
    MatrixPrint(MatrixMulti(a,c))
    MatrixPrint(a)
    MatrixPrint(b)
    a = [[1,1,2],[2,1,2],[3,2,1]]
    print(MatrixDet(a))
    MatrixPrint(a)
    MatrixPrint(MatrixMinor(a,1,0))
    print(Cofactor(a,1,0))
    MatrixPrint(MatrixInverse(a))
    d = MatrixInverse(a)
    MatrixPrint(MatrixMulti(a,d))
    
#Test()