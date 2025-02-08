import numpy as np

# this class is used to simulate the infinity sentinels in Cormen's implementation of merge sort
class infinity:
    def __init__(self):
        return
    def __le__(self, other):
        return False
        
    def __ge__(self, other):
        return True


# merge function, used to merge lists in our recursive calls (the combination part of divide and conquer)
def merge(A, p, q, r):

    # defining left and right halves of the list
    n1 = q - p + 1
    n2 = r - q
    L, R = [], []

    # filling the list with our ordered halves
    for i in np.arange(n1):
        L.append(A[p + i])

    for j in np.arange(n2):
        R.append(A[q + j + 1])

    # adding sentinels to the end of the lists
    L.append(infinity())
    R.append(infinity())

    i = 0
    j = 0

    # merging the lists by selecting the least element between the two at each step
    for k in np.arange(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

# merge sort implementation
def merge_sort(A, p, r):
    if p < r:
        q = (p + r)//2

        # divide and conquer
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)

        #combine
        merge(A, p, q, r)
