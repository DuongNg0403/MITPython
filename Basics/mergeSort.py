def merge(left, right, compare):
        """Assumes left and right are sorted lists and
        compare defines an ordering on the elements.
        Returns a new sorted (by compare) list containing the
        same elements as (left + right) would contain."""
        result = []
        i,j = 0, 0
        while i < len(left) and j < len(right):
                if compare(left[i], right[j]):
                        result.append(left[i])
                        i += 1
                else:
                        result.append(right[j])
                        j += 1
        while (i < len(left)):
                result.append(left[i])
                i += 1
        while (j < len(right)):
                result.append(right[j])
                j += 1
        return result
import operator
def mergeSort(L, compare = operator.lt):
        """Assumes L is a list, compare defines an ordering
        on elements of L
        Returns a new sorted list containing the same elements as L"""
        if len(L) < 2:
                return L[:]
        else:
                middle = len(L)//2
                left = mergeSort(L[:middle], compare)
                right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
L1 = [ 2,4,53,3,0,5,9,8,54,7,89,49]

def lastNameFirstName(name1, name2):
    name1.split()
    name2.split()
    if name1[1] != name2[1]:
        return name1[1] < name2[1]
    else: #last names the same, sort by first name
        return name1[0] < name2[0]
def firstNameLastName(name1, name2):
    import string
    name1 = string.split(name1, ' ')
    name2 = string.split(name2, ' ')
    if name1[0] != name2[0]:
        return name1[0] < name2[0]
    else: #first names the same, sort by last name
        return name1[1] < name2[1]
L = ['Chris Terman', 'Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
newL = mergeSort(L, lastNameFirstName)
print(newL)