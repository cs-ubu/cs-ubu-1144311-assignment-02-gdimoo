from mat import *
import numpy as np
A = readm('A.csv')
b = readm('b.csv')
def solve(A, b):
    """
    using Gauss method with numpy
    1.  กำจัดจุดอ่อน-eliminate
    2. แทนค่าย้อนกลับ-back substitution
    """
    a,b = np.array(A),np.array(b)
    #1. elimination
    n=len(a[0])
    for k in range(n-1): #pivot eq
        for j in range(k+1, n):
            if a[j,k] != 0.0:
                lam = a[j,k]/a[k,k]
                #update A[j][k เป็นต้นไป]
                a[j,k:n] = a[j, k:n] - lam*a[k,k:n]#ไล่ลูปแบบเวกเตอร์
                b[j] = b[j] - lam*b[k]#update b[j]

    #2. back substitution

    x=np.array([0]*n)
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]

    return x.flatten()

printm(A)
printm(b)    
print(solve(A,b))
