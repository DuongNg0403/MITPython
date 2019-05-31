def split_char(string):
    ''' 
    Return a list of lowercase character in a string'''
    L = []
    string.lower
    for char in string:
        if char != " ":
            L.append(char)
    return L