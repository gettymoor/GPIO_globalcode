def fib_rec(e):
    if e<=1:
        return e
    else:
        return(fib_rec(e-1) + fib_rec(e-2))
#print(fib_rec(5))
    
    
nterm = int(input("number:"))
for s in range(nterm):
    print(fib_rec(s))    









