def findAnEven(l):
        """Assumes l is a list of integers
        Returns the first even number in l
        Raises ValueError if l does not contain an even number"""
        for num in l:
                if num%2==0:
                        break
        if num%2!=0:
                raise Exception(ValueError)           
        return num
l = [3,5,3]    
print(findAnEven(l)) 

#the takeaway: both break and return skip whatever the f is after it