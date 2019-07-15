def factorial(f):
    l=1
    
    
    while f > 1:
       l = l*f
       f = f-1
       print(l)
    
    
factorial(9)

#Altanative

def factorial(f):
    if f== 1:
        return 1
    else:
        return f *factorial(f-1)
print(factorial(10))
    