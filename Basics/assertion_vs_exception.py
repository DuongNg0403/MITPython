def return_x():
    try:
        x = int(input("Enter a positive number "))
        assert x>0, "x should be greater than zero"
        return x
    except AssertionError:
        return "AssertionError"

print(return_x())