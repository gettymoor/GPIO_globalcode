def fib_rec(n):
    if n <= 1:
        return n
    else:
        return (fib_rec(n-1)+fib_rec(n-2))


nterm = int(input("num:"))

for x in range(nterm):
    print(fib_rec)