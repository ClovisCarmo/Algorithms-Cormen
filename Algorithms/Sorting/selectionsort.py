import numpy as np

# selection sort implementation
def selection_sort(A):

    for j in np.arange(len(A) - 1):
        min, indx = A[j], j
        
        # finding the least element starting from j
        for i in np.arange(j, len(A)):
            if A[i] < min:
                min, indx = A[i], i
                
        # swapping the least element with index j
        A[indx] = A[j]
        A[j] = min
        
    return
