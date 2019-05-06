def print_move(fr, to):
    print("Move from %s to %s" % (str(fr), str(to)))

def tow_of_HN(n,fr,aux,to):
    if n==1:
        print_move(fr, to)
    else:
        tow_of_HN(n-1,fr,to,aux)
        tow_of_HN(1,fr,aux,to)
        tow_of_HN(n-1,aux,fr,to)

tow_of_HN(5,"A","B","C")