def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1,2,5,7]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print(L1)