import numpy as np

# insertion sort python implementation
def insertion_sort(A):
    # iterating over each element starting from the second
    for j in np.arange(1, len(A)):
        key = A[j]
        i = j - 1
        # for each element larger than the key, we bump the element up one spot
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1  
        # once i == -1 or we find an element <= key, key gets copied to the position of the last element that got bumped up
        A[i+1] = key
        
    return
