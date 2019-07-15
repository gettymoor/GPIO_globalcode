def hp(a):
    if a % 2 is 0:
        return True
    
    else:
        return False
words = ["hello", "my", "name", "is", "Sam"]

print (list(filter(hp, words)))


