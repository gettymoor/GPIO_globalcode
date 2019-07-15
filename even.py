def even (a):
    if a % 2 is 0:
        return True
    
    else:
        return False
numbers =  [12, 54, 33, 67, 24, 89, 11, 24, 47] 

print (list(filter(even, numbers)))

