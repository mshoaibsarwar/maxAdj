import numpy as np

def maxAdj(A):

    A = np.array(A)

    r, c = A.shape

    if r == c:
        # Row-wise product of adjacent elements
        prodRow = []
        for n, m in enumerate(A):
            prodRow.append(np.prod(m))

        # Column-wise product of adjacent elements
        prodCol = []
        i = 0
        while i <= len(A)-1:
            AA = [row[i] for row in A]
            prodCol.append(np.prod(AA))
            i += 1

        # Diagonal-wise product of adjacent elements
        prodDiag = []
        j = 0
        p = 1
        for n, m in enumerate(A):
            p *= m[j]
            prodDiag.append(p)
            j += 1

        # Anti diagonal-wise product of adjacent elements
        prodAnti = []
        k = 0
        q = 1
        for n, m in enumerate(A[::-1]):
            q *= m[k]
            prodAnti.append(q)
            k += 1

        maxProd = max([max(prodRow), max(prodCol), max(prodDiag), max(prodAnti)])

    else:
        maxProd = 'Input matrix does not have nxn dimensions.'

    return maxProd
