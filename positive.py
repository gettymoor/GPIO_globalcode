def positive (a):
    if a > 0:
        return True
    
    else:
        return False
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]  

print (list(filter(positive, numbers)))

