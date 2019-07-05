def split_char(string):
    ''' 
    Return a list of lowercase character in a string'''
    L = []
    for char in string.lower():
        if char != " ":
            L.append(char)
    return L


