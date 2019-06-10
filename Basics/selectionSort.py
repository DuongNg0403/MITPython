def selSort(L):#selection sort
    """Assumes that L is a list of elements that can be
    compared using >.
    Sorts L in ascending order"""
    suffixStart = 0
    while suffixStart != len(L):
        #look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
            #swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1

L = [ 2,4,53,3,0,5,9,8,54,7,89,49]
selSort(L)
print(L)

# inefficient because there are 2 loops of O(n) -> O(n*n) -> quadratic 