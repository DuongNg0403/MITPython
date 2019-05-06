def return_x():
    x=int(input("Enter a positive number "))
    if (x>0)!=1:
        raise Exception("x should be a positive number.The value of x was {}".format(x))
    return x

print(return_x())


