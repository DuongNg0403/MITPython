def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    sum = 0
    try:
        for num in s:
            if num.isdigit():
                sum += int(num)
        return sum
    except TypeError: 
        print("Data type has to be string")

s = "aJKD3426dsfs775"
print(sumDigits(s))